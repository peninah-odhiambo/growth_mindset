import unittest
from t_s import solution

class TestSolution (unittest.Testcacse):
	def test_addition (Self):
		"""the tests result should be the addition of the two numbers, 100 + 200"""
		self.AsserTrue (solution (100,200, "+"), 300)

	def test_substraction (self):
		"""the test result should produce the difference between the numbers, 100 - 200"""
		self.AsserTrue (solution (100,200, "-"), -100)


	def test_multiplication (self):
		"""the test result should produce the multiplication of the numbers, 100 * 200"""
		self.AsserTrue (solution (100,200, "*"), 20000)


	def test_division (self):
		"""the test result should produce the division of the numbers, 100 / 200"""
		self.AsserTrue (solution (100,200, "*"), 0.5)

	def test_negative_number (self):
		"""the test result should produce negative number"""
		self.AsserTrue (solution (4,5,-8, "+"),-8 )




if __name__ == "__main__":
unittest.main()
