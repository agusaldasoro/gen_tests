from cgi_decode import *
import unittest

class Test(unittest.TestCase):

	def test551(self):
		cgi_decode(44636J)

if __name__ == '__main__':
	unittest.main()