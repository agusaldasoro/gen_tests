import time

startTime = time.time()

# stdlib imports
import sys
import pyntch_wrapper
import pyntch
import os
import test_generator
import test_executor

class RandPy:
    def __init__(self):
        pass

    def generate_tests(self, targetPyFile, maxIterations, maxTime, output_dir, random_seed):
        pyntch_wrapper.setup()
        pyFilename = os.getcwd()[:-3] + targetPyFile
        module = pyntch_wrapper.addFile(pyFilename)
        pyntch_wrapper.runAnalysis()
        
        limitTime = time.time() + maxTime
        iterCount = 0
        # line_branch_coverage = 0
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
                    # newCoverage
            iterCount += 1

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
    