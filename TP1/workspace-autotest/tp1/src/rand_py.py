import time

startTime = time.time()

# stdlib imports
import sys
import pyntch_wrapper
import pyntch
import os

class RandPy:
    def __init__(self):
        pass

    def generate_tests(self, targetPyFile, maxIterations, maxTime, output_dir, random_seed):

        pyntch_wrapper.setup()
        pyFilename = os.getcwd() + module_name
        module = pyntch_wrapper.addFile(targetPyFile)
        pyntch_wrapper.runAnalysis()
        # display all functions of pyntch_example
        res = ""
        for f in module.children:
            if isinstance(f, pyntch.function.FuncType):
                res += "Function " + f.name
                for argname in f.argnames:
                    res += " argName:" + argname
                    argTypes = f.space[argname].types
                    types_str = print_pyntch_types(argTypes)
                    res += " argTypes: " + types_str
            
        iteracionesFaltantes = maxIterations   
        tests = list()
        branch_coverage = 0
        line_coverage = 0
        while(time.time() <= maxTime and (maxIterations == -1 or iteracionesFaltantes > 0)):
            t = generate_new_test_call(targetPyFile, random_seed)
            r = execute(t)
            # aumento branches o lineas
            if r.branch_coverage <= branch_coverage:
                pass
            endif
            if r.line_coverage <= line_coverage:
                pass
            endif
            line_coverage = r.line_coverage
            branch_coverage = r.branch_coverage
            tests.add(t)
            write_test_to_file(output_dir, test)
            output_dir.save(t)

            iteracionesFaltantes -= 1
        endwhile

def print_pyntch_types(ts):
    type_str = "["
    for t in ts:
        if not type_str == "[":
            type_str += ","
        type_str += print_pyntch_type(t)
    type_str += "]"
    return type_str

""" Returns a string for a single type declaration """
def print_pyntch_type(t):
    if isinstance(t, pyntch.aggregate_types.ListObject):
        elem_types = t.elemall.types
        return "list" + print_pyntch_types(elem_types) 
    elif isinstance(t, pyntch.aggregate_types.DictObject):
        key_types = t.key.types
        value_types = t.value.types
        key_types_str = print_pyntch_types(key_types)
        value_types_str = print_pyntch_types(value_types)
        return "dict(" + key_types_str + "->" + value_types_str + ")"
    elif isinstance(t, pyntch.aggregate_types.TupleObject):
        elem_types = t.elemall.types
        return "tuple" + print_pyntch_types(elem_types)
    elif isinstance(t, pyntch.aggregate_types.SetObject):
        elem_types = t.elemall.types
        return "set" + print_pyntch_types(elem_types) 
    else:
        type_str = str(t) 
        if type_str == "<int>":
            return "<int>"
        elif type_str == "<bool>":
            return "<bool>"
        elif type_str == "<float>":
            return "<float>"
        elif type_str == "<long>":
            return "<long>"
        elif type_str == "<basestring>" or type_str=="<unicode>" or type_str=="<str>":
            return type_str
        else:
            raise Exception("Unknown Pyntch primitive type" + str(t))

    
if __name__ == "__main__":
    if len(sys.argv) != 5:
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
    
