import unittest 

class TestExample(unittest.TestCase):
    def setUp(self):
        self.test_list=[1,2,3]
        print("setup: Initialize resources")
        
    def tearDown(self):
        self.test_list=None
        print("Teardown: Clean up resources")
        
    def test_append(self):
        self.test_list.append(4)
        self.assertEqual(self.test_list, [1,2,3,4])
        
    def test_pop(self):
        item=self.test_list.pop()
        self.assertEqual(item, 3)
        self.assertEqual(self.test_list, [1,2])
        
    def test_clear(self):
        self.test_list.clear()
        self.assertCountEqual(self.test_list, [])
        
if __name__=="__main__":
    unittest.main()