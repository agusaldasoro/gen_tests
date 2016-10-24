from levenshtein_sequence import *
import unittest

class Test(unittest.TestCase):

	def test350(self):
		levenshtein_sequence(395, 0)

if __name__ == '__main__':
	unittest.main()