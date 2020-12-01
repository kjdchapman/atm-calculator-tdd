import unittest

def withdraw(input):
  hundreds = 0
  fifties = 0
  twenties = 0

  divides_by_hundred = input % 100 == 0
  divides_by_fifty = input % 50 == 0
  divides_by_twenty = input % 20 == 0

  if divides_by_twenty:
    if input == 20: twenties += 1
    if input == 40: twenties += 2
    if input == 60: twenties += 3

  if divides_by_fifty:
    if divides_by_hundred:
      hundreds += input / 100
    else:
      fifties += 1
      hundreds += (input - 50) / 100

  # not exactly divisible?
  if input == 70:
    twenties += 1
    fifties += 1

  if input == 90:
    twenties += 2
    fifties += 1

  if input == 120:
    hundreds += 1
    twenties += 1

  if input == 140:
    hundreds += 1
    twenties += 2

  if input == 160:
    hundreds += 1
    twenties += 3

  return [hundreds, fifties, twenties]

# [100s, 50s, 20s]
class TestATMCalculator(unittest.TestCase):
    def testEmptyInput(self):
        result = withdraw(0)
        self.assertEqual(result, [0, 0, 0])

    def testSingleHundred(self):
        result = withdraw(100)
        self.assertEqual(result, [1, 0, 0])

    def testTwoHundred(self):
        result = withdraw(200)
        self.assertEqual(result, [2, 0, 0])

    def testThreeHundred(self):
        result = withdraw(300)
        self.assertEqual(result, [3, 0, 0])

    def testSingleFifty(self):
        result = withdraw(50)
        self.assertEqual(result, [0, 1, 0])

    def testThreeTwenties(self):
        result = withdraw(60)
        self.assertEqual(result, [0, 0, 3])

    def testSingleTwenty(self):
        result = withdraw(20)
        self.assertEqual(result, [0, 0, 1])

    def testTwoTwenties(self):
        result = withdraw(40)
        self.assertEqual(result, [0, 0, 2])

    def testSeventy(self):
        result = withdraw(70)
        self.assertEqual(result, [0, 1, 1])

    def testNinety(self):
        result = withdraw(90)
        self.assertEqual(result, [0, 1, 2])

    def testHundredAndTwenty(self):
        result = withdraw(120)
        self.assertEqual(result, [1, 0, 1])

    def testHundredAndForty(self):
        result = withdraw(140)
        self.assertEqual(result, [1, 0, 2])

    def testHundredAndFifty(self):
        result = withdraw(150)
        self.assertEqual(result, [1, 1, 0])

    def testHundredAndSixty(self):
        result = withdraw(160)
        self.assertEqual(result, [1, 0, 3])

    def testTwoFifty(self):
        result = withdraw(250)
        self.assertEqual(result, [2, 1, 0])
