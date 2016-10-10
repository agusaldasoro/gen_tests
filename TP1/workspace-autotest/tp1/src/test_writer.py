import os

class TestWriter:
    """Writes a given test sequence into a single python unit test"""
    def __init__(self, new_out_dir, module_name):
        self.__outDir = new_out_dir
        self.__module = module_name
    
    def writeToFile(self, test_call, test_suffix):
        with open(os.path.join(self.__outDir, 'tests'+str(test_suffix)+'.py'), 'w') as f:
            f.write('from ')
            f.write(self.__module)
            f.write(' import *\n')
            f.write('import unittest\n\n')
            f.write('class Test(unittest.TestCase):\n')
            f.write("\n\tdef test")
            f.write(str(test_suffix))
            f.write("(self):\n")
            
            f.write("\t\t")
            f.write(test_call.toCode())
            f.write("\n")

            f.write("\nif __name__ == '__main__':\n")
            f.write("\tunittest.main()")