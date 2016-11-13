from cgi_decode import *
import unittest

class Test(unittest.TestCase):

	def test450(self):
		cgi_decode(946245)

if __name__ == '__main__':
	unittest.main()