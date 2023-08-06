#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
# Copyright (C) MKO575, 2023
# Distributed under the terms of the CeCILL license, as published by the CEA,
# CNRS and INRIA. For more information, refer to the LICENSE file or to:
# * https://www.cecill.info/licences/Licence_CeCILL_V2.1-en.html
# * https://opensource.org/license/cecill-2-1/
# * https://choosealicense.com/licenses/cecill-2.1/
################################################################################

"""
Creates or shows a diagram representing the dependencies declared in a set of module-info.java files.
"""

from __future__ import annotations # For circular dataclass declarations

import sys, os, glob
import argparse
import re

from dataclasses import dataclass, field
from enum import Enum
from collections import deque

import graphviz # or pygraphviz or pydot

################################################################################

moduleLineRE = re.compile(r"^\s*module\s*(?P<moduleName>\S+?)\s*{\s*$")
requiresLineRE = re.compile(r"^\s*requires\s*(?P<reqModuleName>\S+?)\s*;\s*$")
exportsLineRE = re.compile(r"^\s*exports\s*(?P<expPackageName>\S+?)\s*;\s*$")
usesLineRE = re.compile(r"^\s*uses\s*(?P<useInterfaceName>\S+?)\s*;\s*$")
providesLineRE = re.compile(r"^\s*provides\s*(?P<provInterfaceName>\S+?)\s*with\s*(?P<withClassName>\S+?)\s*;\s*$")

@dataclass
class ProjectElement:
    project: Project

@dataclass
class NamedEntity:
    name: str
    
    def __eq__(self, other):
        return (self.name == other.name)
    
    def __hash__(self):
        return hash(self.name)

@dataclass
class Project(NamedEntity):
    name: str = None
    modules: dict[str,Module] = field(default_factory=dict)
    packages: dict[str,Package] = field(default_factory=dict)
    interfaces: dict[str,Package] = field(default_factory=dict)
    classes: dict[str,Package] = field(default_factory=dict)
    serviceUsers: dict[Interface, set[Module]] = field(default_factory=dict)
    
    def __hash__(self):
        return NamedEntity.__hash__(self)

    def processDependencies(self, fileName: str) -> Project:
        module = None
        with open(fileName, 'r', encoding='UTF-8') as file:
            while (line := file.readline()):
                line = line.rstrip('\n')
                
                match = moduleLineRE.match(line)
                if match :
                    moduleName = match.group("moduleName")
                    if args.verbose: print(f"In '{fileName}': definition of module '{moduleName}'!")
                    module = self.modules.get(moduleName, Module(self, moduleName, fileName))
                    module.infoFile = fileName
                    self.modules[moduleName] = module
                    
                match = requiresLineRE.match(line)
                if match :
                    reqModuleName = match.group("reqModuleName")
                    if args.verbose: print(f"In '{fileName}': '{moduleName}' requires '{reqModuleName}'!")
                    reqModule = self.modules.get(reqModuleName, Module(self, reqModuleName))
                    self.modules[reqModuleName] = reqModule
                    module.requires.add(reqModule)
                    
                match = exportsLineRE.match(line)
                if match :
                    expPackageName = match.group("expPackageName")
                    if args.verbose: print(f"In '{fileName}': '{moduleName}' exports '{expPackageName}'!")
                    expPackage = self.packages.get(expPackageName, Package(self, expPackageName))
                    self.packages[expPackageName] = expPackage
                    module.exports.add(expPackage)
                    
                match = usesLineRE.match(line)
                if match :
                    useInterfaceName = match.group("useInterfaceName")
                    if args.verbose: print(f"In '{fileName}': '{moduleName}' uses '{useInterfaceName}'!")
                    useInterface = self.interfaces.get(useInterfaceName, Interface(self, useInterfaceName))
                    self.interfaces[useInterfaceName] = useInterface
                    module.uses.add(useInterface)
                    serviceUsers = self.serviceUsers.get(useInterfaceName, set())
                    serviceUsers.add(module)
                    self.serviceUsers[useInterfaceName] = serviceUsers
                    
                match = providesLineRE.match(line)
                if match :
                    provInterfaceName = match.group("provInterfaceName")
                    withClassName = match.group("withClassName")
                    if args.verbose: print(f"In '{fileName}': '{moduleName}' provides '{provInterfaceName}' with '{withClassName}'!")
                    provInterface = self.interfaces.get(provInterfaceName, Interface(self, provInterfaceName))
                    self.interfaces[provInterfaceName] = provInterface
                    withClass = self.classes.get(withClassName, Class(self, withClassName))
                    self.interfaces[withClassName] = withClass
                    module.provides.add(ProvideRelation(provInterface, withClass))

        return self

    def generateDependenciesGraph(self):
        gvGraph = graphviz.Digraph(
            'module-dependencies',
            comment = f'Graph representing the Java Modules dependencies of the { self.name if self.name else "" } project.',
            engine = G_engine
        )
        gvGraph.node_attr['colorscheme'] = G_colorScheme
        # gvGraph.edge_attr['len'] = "2"
        
        deque(map(
            lambda x: x.addNodeToGraph(gvGraph),
            set(self.modules.values()) | set(self.packages.values()) | set(self.interfaces.values()) | set(self.classes.values())
        ), maxlen=0)
        
        for module in self.modules.values():
            module.addDependenciesToGraph(gvGraph)
            
        return gvGraph


@dataclass
class Module(NamedEntity, ProjectElement):
    infoFile: str = None
    requires: set[Module] = field(default_factory=set)
    uses: set[Interface] = field(default_factory=set)
    exports: set[Package] = field(default_factory=set)
    provides: set[ProvideRelation] = field(default_factory=set)

    classId: str = "Module"

    def __hash__(self):
        return NamedEntity.__hash__(self)

    def toBeDisplayed(self):
        return self.classId in G_entitiesToBeDisplayed and (self.infoFile or G_displayExternalModules)

    def gvId(self):
        return self.name

    def addNodeToGraph(self, gvGraph):
        if self.toBeDisplayed():
            gvGraph.node(self.gvId(), self.name, shape="component", style="filled", fillcolor=G_colorModule)

    def addDependenciesToGraph(self, gvGraph):
        if self.toBeDisplayed():
            for m in self.requires:
                if m.toBeDisplayed():
                    gvGraph.edge(self.gvId(), m.gvId(), style="bold")
            for i in self.uses:
                if i.toBeDisplayed():
                    gvGraph.edge(i.gvId(), self.gvId(), dir="back", arrowtail="dottee", arrowsize="1.1")
            for p in self.exports:
                if p.toBeDisplayed():
                    gvGraph.edge(self.gvId(), p.gvId(), dir="back", arrowtail="diamond", style="dashed", penwidth="0.75")
            for pr in self.provides:
                # If intermediate entities (interface provided and class implementing it) are not displayed ...
                if not pr.provided.toBeDisplayed() and not pr.implementation.toBeDisplayed():
                    for m in set(m for m in self.project.serviceUsers.get(pr.provided.name) if m.toBeDisplayed()):
                        # ... for all module using it and displayed, display the transitive "dependency"
                        gvGraph.edge(self.gvId(), m.gvId(), dir="back", style="dashed", penwidth="1.5")
                # Otherwise ...
                else:
                    # if implementing class is to be displayed, ...
                    if pr.implementation.toBeDisplayed():
                        # ... display the "half-dependency" from implementing class to the providing module
                        gvGraph.edge(self.gvId(), pr.implementation.gvId(), dir="both", arrowtail="diamond", arrowhead="dot")
                        # ... and if the defining interface is to be displayed, ...
                        if pr.provided.toBeDisplayed():
                            # ... display the "half-dependency" from the provided service interface to the implementing class
                            gvGraph.edge(pr.implementation.gvId(), pr.provided.gvId(), arrowsize="1.25", arrowhead="empty")
                        # ... otherwise
                        else:
                            for m in set(m for m in self.project.serviceUsers.get(pr.provided.name) if m.toBeDisplayed()):
                                # ... for all module using it and displayed, display the transitive "dependency"
                                gvGraph.edge(pr.implementation.gvId(), m.gvId(), dir="back", style="dashed", penwidth="1.5")
                    # otherwise, defining interface IS to be displayed (and link to using module already displayed if it is to be)
                    else:
                        # ... so just display the transitive "half-dependency" from the provided service interface to the providing module
                        gvGraph.edge(self.gvId(), pr.provided.gvId(), dir="back", style="dashed", penwidth="1.5")
            
    
@dataclass
class ProvideRelation:
    provided: Interface
    implementation: Class
    
    def __hash__(self):
        return hash(f"Provides {hash(self.provided)} with {hash(self.implementation)}")

@dataclass
class Package(NamedEntity, ProjectElement):
    
    classId: str = "Package"

    def __hash__(self):
        return NamedEntity.__hash__(self)

    def toBeDisplayed(self):
        return (self.classId in G_entitiesToBeDisplayed)

    def gvId(self):
        return self.name

    def addNodeToGraph(self, gvGraph):
        if self.toBeDisplayed():
            gvGraph.node(self.gvId(), self.name, shape="tab", style="filled", fillcolor=G_colorPackage)
    
@dataclass
class Interface(NamedEntity, ProjectElement):
    
    classId: str = "Interface"

    def __hash__(self):
        return NamedEntity.__hash__(self)

    def toBeDisplayed(self):
        return self.classId in G_entitiesToBeDisplayed

    def gvId(self):
        return self.name

    def addNodeToGraph(self, gvGraph):
        if self.toBeDisplayed():
            gvGraph.node(self.gvId(), self.name, shape="ellipse", style="filled", fillcolor=G_colorInterface)
    
@dataclass
class Class(NamedEntity, ProjectElement):
    
    classId: str = "Class"

    def __hash__(self):
        return NamedEntity.__hash__(self)

    def toBeDisplayed(self):
        return self.classId in G_entitiesToBeDisplayed

    def gvId(self):
        return self.name

    def addNodeToGraph(self, gvGraph):
        if self.toBeDisplayed():
            gvGraph.node(self.gvId(), self.name, shape="box", style="filled", fillcolor=G_colorClass)
    
################################################################################

def retrieveModuleinfoFiles(inputs: list[str]) -> set[str] :
    result = set()

    for i in inputs: #type: str
        i:str
        if os.path.isfile(i):
            result.add(i)
        if os.path.isdir(i):
            result.update(glob.glob('**/module-info.java', recursive=True))
    return result

################################################################################

# Global parameters
G_displayExternalModules = False
G_entitiesToBeDisplayed = set( x.classId for x in [ Module, Interface, Class ] )
G_engine = "dot"
G_colorScheme = "pastel14"
G_colorModule = "1"
G_colorPackage = "4"
G_colorInterface = "3"
G_colorClass = "2"

# CLI parameters
CLIP_defaultOutputName = "java-modules-dependencies"
CLIP_defaultImageFileType = "pdf"
CLIP_choicesImageFileTypes = ['pdf', 'png', 'svg']
CLIP_choicesEntities = [ x.classId for x in [ Module, Package, Interface, Class ] ]
CLIP_choicesEngines = ['dot', 'neato', 'fdp', 'sfdp', 'circo', 'twopi', 'osage', 'patchwork']

# Actions for parameters requiring special treatment (incuding evluation in order)
class SetDisplayedEntitiesTypeAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        global G_entitiesToBeDisplayed
        G_entitiesToBeDisplayed = set(values)

class IncludeEntitiesTypeAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        global G_entitiesToBeDisplayed
        G_entitiesToBeDisplayed.update(values)

class ExcludeEntitiesTypeAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        global G_entitiesToBeDisplayed
        G_entitiesToBeDisplayed.difference_update(values)

# General CLI parameters pocessing function
def processArguments(args):
    global G_displayExternalModules, G_entitiesToBeDisplayed
    global G_engine, G_colorScheme, G_colorModule, G_colorPackage, G_colorInterface, G_colorClass
    
    # print(f"Args: {args}")
    if args.show_externals:
        G_displayExternalModules = True
    if args.include_module != None:
        if args.include_module: G_entitiesToBeDisplayed.add(Module.classId)
        else: G_entitiesToBeDisplayed.remove(Module.classId)
    if args.include_package != None:
        if args.include_package: G_entitiesToBeDisplayed.add(Package.classId)
        else: G_entitiesToBeDisplayed.remove(Package.classId)
    if args.include_interface != None:
        if args.include_interface: G_entitiesToBeDisplayed.add(Interface.classId)
        else: G_entitiesToBeDisplayed.remove(Interface.classId)
    if args.include_class != None:
        if args.include_class: G_entitiesToBeDisplayed.add(Class.classId)
        else: G_entitiesToBeDisplayed.remove(Class.classId)
    if args.engine:
        G_engine = args.engine
    if args.color_scheme:
        G_colorScheme = args.color_scheme
    if args.color_module:
        G_colorModule = args.color_module
    if args.color_package:
        G_colorPackage = args.color_package
    if args.color_interface:
        G_colorInterface = args.color_interface
    if args.color_class:
        G_colorClass = args.color_class

# CLI parameters definition
def parse_CLIArgs():
    p = argparse.ArgumentParser(description=__doc__)

    p.add_argument("input", metavar="PATH", type=str,
                   help="module-info.java file or directory from which to recusively retrieve such files", nargs='+')

    g = p.add_argument_group('Selection of displayed entities')
    g.add_argument("-x", "--show-externals", default=False, action="store_true",
                   help="display external modules (not described by the provided files)")
    g.add_argument("-d", "--displayed-entities", metavar="ETYPE", nargs='+', action=SetDisplayedEntitiesTypeAction,
                   type=str, choices=CLIP_choicesEntities, 
                   help=f"display entities iff they are of the provided type (potential values are {CLIP_choicesEntities})")
    for t in [ Module, Package, Interface, Class ]:
        g.add_argument(f"--{t.classId.lower()}", action=argparse.BooleanOptionalAction,
                       dest=f"include_{t.classId.lower()}",
                       help=f"display or not entities of type {t.classId}")
    g.add_argument("--include-entities", metavar="ETYPE", nargs='+', action=IncludeEntitiesTypeAction,
                   type=str, choices=CLIP_choicesEntities, 
                   help=f"display entities of the provided type (potential values are {CLIP_choicesEntities})")
    g.add_argument("--exclude-entities", metavar="ETYPE", nargs='+', action=ExcludeEntitiesTypeAction,
                   type=str, choices=CLIP_choicesEntities, 
                   help=f"do not display entities of the provided type (potential values are {CLIP_choicesEntities})")

    g = p.add_argument_group('Look & feel configuration')
    g.add_argument("-e", "--engine", metavar="ENGINE", type=str,
                   choices=CLIP_choicesEngines, default=G_engine,
                   help=f"engine to use to render the graph (potential values are {CLIP_choicesEngines}, default value is '{G_engine}')")
    g.add_argument("-c", "--color-scheme", metavar="COLORSCHEME", type=str,
                   default=G_colorScheme,
                   help=f"set the colorscheme to use (default is '{G_colorScheme}', see https://graphviz.org/docs/attrs/colorscheme/ for potential values)")
    for t in [ Module, Package, Interface, Class ]:
        g.add_argument(f"--color-{t.classId.lower()}", metavar="COLOR", type=str,
                       help=f"display color of entities of type {t.classId}")

    g = p.add_argument_group('Output options')
    g.add_argument("-o", "--output-name", metavar="FILENAME", type=str, dest="outputFileName",
                   default=CLIP_defaultOutputName,
                   help=f"basename (without suffixes) used for output files (default is '{CLIP_defaultOutputName}')")
    g.add_argument(f"--save", action=argparse.BooleanOptionalAction, default=False,
                   help=f"do or do not save the graphviz source file")
    g.add_argument(f"--render", action=argparse.BooleanOptionalAction, default=False,
                   help=f"do or do not render the graph into an image file")
    g.add_argument("-t", "--output-type", metavar="FILETYPE", type=str, dest="imageOutputFileType",
                   choices=CLIP_choicesImageFileTypes, default=CLIP_defaultImageFileType,
                   help=f"image output file type (potential values are {CLIP_choicesImageFileTypes}, default is '{CLIP_defaultImageFileType}')")
    g.add_argument(f"--view", action=argparse.BooleanOptionalAction, default=True,
                   help=f"do or do not display the graph")

    g = p.add_argument_group('General options')
    g.add_argument("-p", "--progress", default=False, action="store_true",
                   help="emit progress information")
    g.add_argument("-v", "--verbose", default=False, action="store_true",
                   help="increase verbosity")

    return p.parse_args()

################################################################################

def main():
    global args
    args = parse_CLIArgs()

    processArguments(args)

    if args.progress: print(f"\n  >> Parsed arguments!\n")

    moduleInfoFiles = retrieveModuleinfoFiles(args.input)

    if args.progress: print(f"\n  >> module-info.java files retrieved!\n")
    if args.verbose: print(f"\nThe following module-info.java files have been found: {moduleInfoFiles}\n")

    p = Project()
    for f in moduleInfoFiles:
        p.processDependencies(f)

    if args.progress: print(f"\n  >> Dependencies processed!\n")
    if args.verbose: print(f"\nProject: {p}\n")

    gvGraph = p.generateDependenciesGraph()

    if args.progress: print(f"\n  >> Dependencies graph generated!\n")

    if args.save:
        gvGraph.save(filename=f"{args.outputFileName}.gv")

    # match (args.render, args.view):
    #     case (True, True):
    #         gvGraph.render(format=args.imageOutputFileType, filename=args.outputFileName, view=True, cleanup=True)
    #     case (True, False):
    #         gvGraph.render(format=args.imageOutputFileType, filename=args.outputFileName, view=False, cleanup=True)
    #     case (False, True):
    #         gvGraph.view(filename=args.outputFileName, cleanup=True)
    # My version of Python is not 3.10 or above yet (probably like many people), so ...
    if args.render:
        gvGraph.render(format=args.imageOutputFileType, filename=args.outputFileName, view=args.view, cleanup=True)
    else:
        if args.view:
            gvGraph.view(filename=args.outputFileName, cleanup=True)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
