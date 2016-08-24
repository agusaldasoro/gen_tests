'''
Abstract class that represents an object
to report the coverage of statements or branches
'''
import ast

class Coverage:

    '''
    Constructor, module_name is the 
    module to read lines and branches from
    '''
    def __init__(self, module_name=None):
        pass

    '''
    Set-up coverage before running any tests
    '''
    def setUp(self):
        pass
    
    '''
    Tear-down all tracing configuration
    '''
    def tearDown(self):
        pass

    '''
    Returns a float between 0 and 1 representing 
    the obtained coverage during test execution
    '''
    def get_coverage(self):
        pass
    
    '''
    Override this method to customize the 
    final message to the user
    '''
    def printCoverage(self):
        pass
    
'''
Reports the statement Coverage
'''
class LineCoverage(Coverage):
    def __init__(self, module_name=None):
        self.lines_visited = set()
        pass

    def printCoverage(self):
        print("Line Coverage is " + str(self.get_coverage()) + "%")

    def traceit(self, frame, event, arg):
        if event == "line" and frame.f_code.co_filename == "/home/aaldasoro/Documentos/gen_tests/taller2/Taller02-python-src/python/src/cgi_decode.py":
            self.lines_visited.add(frame.f_lineno)
        return self.traceit
    
    def get_coverage(self):
        return 100 * float(len(self.lines_visited)) / self.total_lines

'''
Reports the branch Coverage
'''
class BranchCoverage(Coverage):
    def __init__(self, module_name=None):
        self.branches_visited = set()
        pass
    
    def printCoverage(self):
        print("Branch Coverage is " + str(self.get_coverage())+ "%")

    def traceit(self, frame, event, arg):
        if event == "line" and frame.f_code.co_filename == "/home/aaldasoro/Documentos/gen_tests/taller2/Taller02-python-src/python/src/cgi_decode.py":
            if frame.f_lineno in self.branches_lines:
                self.branches_visited.add(frame.f_lineno)
        return self.traceit

    def get_coverage(self):
        return 100 * float(len(self.branches_visited)) / self.total_branches

