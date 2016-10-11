'''
Created on Aug 10, 2016

@author: galeotti
'''
import unittest
import cgi_decode
import coverage 
import ast
import sys

class TestCGIDecode(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.c = coverage.TotalCoverage("cgi_decode")    
        cls.c.total_lines = line_counter()
        cls.c.branches_lines = branch_lines()
        cls.c.total_branches = branch_counter()
        sys.settrace(cls.c.traceit)
        cls.c.setUp()

    def test0(self):
        pass
    
    def test1(self):
        decoded_str = cgi_decode.cgi_decode("test")
        self.assertEquals(decoded_str, "test")
 
    @unittest.expectedFailure
    def test2(self):
        cgi_decode.cgi_decode("+%0d+%4j")
 
    def test3(self):
        decoded_str = cgi_decode.cgi_decode("abc")
        self.assertEquals(decoded_str,"abc")
    
    @classmethod
    def tearDownClass(cls): 
        cls.c.tearDown()
        cls.c.printCoverage()

class LineCounter(ast.NodeVisitor):
    def __init__(self):
        self.lines = set()

    def generic_visit(self, node):
        if hasattr(node, "lineno"):
            self.lines.add(node.lineno)
        ast.NodeVisitor.generic_visit(self, node)

class BranchCounter(ast.NodeVisitor):
    def __init__(self):
        self.branches = 0
        self.branches_lines = set()

    def visit_If(self, node):
        self.branches += 2
        self.branches_lines.add(node.body[0].lineno)
        self.branches_lines.add(node.orelse[0].lineno)
        self.generic_visit(node)

    def visit_While(self, node):
        self.branches += 2
        self.branches_lines.add(node.body[0].lineno)
        self.generic_visit(node)

# ejercicios

def ej1_run_tests():
    if __name__ == "__main__":
        unittest.main()

def ej2_parse_ast():
    root = ast.parse(open("cgi_decode.py").read())
    print ast.dump(root)

def line_counter():
    root = ast.parse(open("cgi_decode.py").read())
    v = LineCounter()
    v.visit(root)
    return len(v.lines)

def branch_counter():
    root = ast.parse(open("cgi_decode.py").read())
    v = BranchCounter()
    v.visit(root)
    return v.branches

def branch_lines():
    root = ast.parse(open("cgi_decode.py").read())
    v = BranchCounter()
    v.visit(root)
    return v.branches_lines

