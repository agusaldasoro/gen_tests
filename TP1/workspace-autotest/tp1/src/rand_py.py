import time

startTime = time.time()

# stdlib imports
import sys
import pyntch_wrapper
import pyntch
import os
import test_generator
import test_executor
import coverage 
import ast

class RandPy:
    def __init__(self):
        pass



    def generate_tests(self, targetPyFile, maxIterations, maxTime, output_dir, random_seed):
        pyntch_wrapper.setup()
        pyFilename = os.getcwd() + targetPyFile
        module = pyntch_wrapper.addFile(pyFilename)
        pyntch_wrapper.runAnalysis()
        
        limitTime = time.time() + maxTime
        iterCount = 0
        line_branch_coverage = 0
        tests = []
        
        total_lines = line_counter(pyFilename)
        branches_lines = branch_lines(pyFilename)
        total_branches = branch_counter(pyFilename)
        lines_visited = set()
        branches_visited = set()   
        
        while (iterCount < maxIterations and time.time() < limitTime):    
            for f in module.children:
                if isinstance(f, pyntch.function.FuncType):
                    g = test_generator.TestGenerator(f,random_seed)
                    func_tuple = g.generate_new_test_call()
                    testCall = test_executor.TestCall(func_tuple[0], func_tuple[1])
                    testExecutor = test_executor.TestExecutor(pyFilename)
                    res = testExecutor.execute(testCall)
                    if res is TypeError:
                        continue
                    testsWithNew = tests
                    testsWithNew.append(testExecutor)
                    
                    totalCoverage = coverage.TotalCoverage(pyFilename)    
                    totalCoverage.total_lines = line_counter(pyFilename)
                    totalCoverage.branches_lines = branch_lines(pyFilename)
                    totalCoverage.total_branches = branch_counter(pyFilename)
                    sys.settrace(totalCoverage.traceit)
                    new_lines_visited = lines_visited
                    new_lines_visited.union(totalCoverage.lines_visited)
                    new_branches_visited = branches_visited
                    new_branches_visited.union(totalCoverage.branches_visited)
                    
                    if len(new_lines_visited) > len(lines_visited) or len(new_branches_visited) > len(branches_visited):
                        lines_visited = new_lines_visited
                        branches_visited = new_branches_visited
                        tests.add(testExecutor)
            iterCount += 1
        print("Line Coverage:", 100*len(lines_visited)/total_lines)
        print("Branch Coverage:", 100*len(branches_visited)/total_branches)
        return line_branch_coverage

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

def line_counter(pyFilename):
    root = ast.parse(open(pyFilename).read())
    v = LineCounter()
    v.visit(root)
    return len(v.lines)

def branch_counter(pyFilename):
    root = ast.parse(open(pyFilename).read())
    v = BranchCounter()
    v.visit(root)
    return v.branches

def branch_lines(pyFilename):
    root = ast.parse(open(pyFilename).read())
    v = BranchCounter()
    v.visit(root)
    return v.branches_lines

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage <targetPyFile> <maxIterations> <maxTime> <outputDir> <randomSeed>")
        sys.exit()
    
    # load the cli arguments
    targetPyFile = sys.argv[1]
    maxIterations = int(sys.argv[2])
    maxTime = float(sys.argv[3])
    output_dir = sys.argv[4]
    random_seed = int(sys.argv[5])

    randPy = RandPy()
    randPy.generate_tests(targetPyFile, maxIterations, maxTime, output_dir, random_seed)
    