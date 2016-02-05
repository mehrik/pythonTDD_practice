import unittest
from insert_value import insertValAt

class InsertValueTest(unittest.TestCase):
    def setUp(self):
        self.testList = [0, 1, 2, 3, 4]

    def testInsertAtIndexTwo(self):
        self.result = insertValAt(2, self.testList, 100)
        return self.assertEqual([0, 1, 100, 2, 3, 4], self.result)

    def testReturnFalseForInvalidIndex(self):
        self.result = insertValAt(111, self.testList, 100)
        return self.assertEqual(False, self.result)

if __name__ == "__main__":
    unittest.main()