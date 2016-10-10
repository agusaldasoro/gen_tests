'''
Created on Sep 1, 2016

@author: galeotti
'''
import pyntch_wrapper
import pyntch
import os

""" Returns a string with a sequence of type declarations """
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
                
if __name__ == '__main__':
    # use pyntch to get type information
    pyntch_wrapper.setup()
    module = pyntch_wrapper.addFile(os.getcwd() + "/../examples/pyntch_example.py")
    pyntch_wrapper.runAnalysis()
    
    # display all functions of pyntch_example
    for f in module.children:
        if isinstance(f, pyntch.function.FuncType):
            print("Function " + f.name)
            for argname in f.argnames:
                print("  argName:" + argname)
                argTypes = f.space[argname].types
                types_str = print_pyntch_types(argTypes)
                print("  argTypes: " + types_str)