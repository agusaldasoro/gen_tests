import os

import pyntch
from pyntch.typenode import TypeNode, CompoundTypeNode, TypeChecker
from pyntch.frame import ExecutionFrame, ExceptionCatcher
from pyntch.expression import MustBeDefinedNode
from pyntch.namespace import Namespace
from pyntch.module import Interpreter, IndentedStream, ModuleNotFound
from pyntch.config import ErrorConfig

def setup():
    """This method performs the setup for pyntch. You should call it once before you use pyntch for the first time. """
    TypeNode.debug = False
    TypeNode.verbose = False
    Interpreter.debug = False
    Interpreter.verbose = False
    stubdir = os.path.join(os.path.dirname(pyntch.__file__), 'stub')
    Interpreter.initialize(stubdir)
    TypeChecker.reset()
    MustBeDefinedNode.reset()
    ExceptionCatcher.reset()

def addFile(targetPyFile):
    (name,_) = os.path.splitext(os.path.basename(targetPyFile))
    module = Interpreter.load_file(name, targetPyFile, [os.path.dirname(targetPyFile)])
    return module

def runAnalysis():
    TypeNode.run()
    TypeChecker.check()
    MustBeDefinedNode.check()
    ExceptionCatcher.check()
    TypeNode.run()