import unittest

def is_primo(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

class TestPrimos(unittest.TestCase):
    def test_1(self):
        result = is_primo(1)
        self.assertEqual(result, False)
    
    def test_2(self):
        result = is_primo(2)
        self.assertEqual(result, True)

    def test_3(self):
        result = is_primo(3)
        self.assertEqual(result, True)

    def test_4(self):
        result = is_primo(4)
        self.assertEqual(result, False)

    def test_5(self):
        result = is_primo(5)
        self.assertEqual(result, True)

    def test_6(self):
        result = is_primo(6)
        self.assertEqual(result, False)
    def test_7(self):
        result = is_primo(7)
        self.assertEqual(result, True)

    def test_11(self):
        result = is_primo(11)
        self.assertEqual(result, True)

    def test_13(self):
        result = is_primo(13)
        self.assertEqual(result, True)

    def test_17(self):
        result = is_primo(17)
        self.assertEqual(result, True)

    def test_19(self):
        result = is_primo(19)
        self.assertEqual(result, True)

    def test_23(self):
        result = is_primo(23)
        self.assertEqual(result, True)    

def correr_pruebas()
     suite = unittest.TestLoader().loadTestsFromTestCase(TestPrimos)
     
     corredor = unittest.TextTestRunner()

     resultado = corredor.run(suite)
    
     return resultado

if __name__ == '__main__':
    correr_pruebas()
    
 unittest.main()
