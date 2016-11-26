import time

startTime = time.time()

# stdlib imports
import sys
import pyntch_wrapper
import pyntch
import os
import test_generator
import test_executor
import test_writer
import coverage 
import ast
import random


populationSize = 50

eliteSize = 1

testSuiteLength= 40

crossoverProbability=0.75

mutationProbability=0.75

addNewTestProbability=0.33

modifyExistingTestProbability=0.33

removeExistingTestProbability=0.33

class EvoPy:
    def __init__(self):
        pass

    def generate_tests(self, targetPyFile, maxGenerations, maxTime, output_dir, random_seed):
        # TODO COMPLETAR!
        pass
    
if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage <targetPyFile> <maxIterations> <maxTime> <outputDir> <randomSeed>")
        sys.exit()
    
    # load the cli arguments
    targetPyFile = sys.argv[1]
    maxGenerations = int(sys.argv[2])
    maxTime = float(sys.argv[3])
    output_dir = sys.argv[4]
    random_seed = int(sys.argv[5])

    evoPy = EvoPy()
    evoPy.generate_tests(targetPyFile, maxGenerations, maxTime, output_dir, random_seed)
    
