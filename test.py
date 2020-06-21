import unittest
import guessGame as gsm

class TestMain(unittest.TestCase):
    
    def test_input(self):
        answer = 5
        guess = 5
        result = gsm.guessAns(guess, answer)
        self.assertTrue(result)

    def test_input2(self):
        answer = 5
        guess = 7
        result = gsm.guessAns(guess, answer)
        self.assertFalse(result)

    def test_input3(self):
        answer = 7
        guess = 12
        result = gsm.guessAns(guess, answer)
        self.assertFalse(result)

    def test_input4(self):
        answer = 7
        guess = '11'
        result = gsm.guessAns(guess, answer)
        self.assertFalse(result)
        
    

if __name__ == "__main__":
    unittest.main()