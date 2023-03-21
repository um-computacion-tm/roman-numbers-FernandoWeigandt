import unittest

def decimal_to_roman(decimal):

    if decimal <= 3:
       return "I" * decimal
    elif decimal == 5:
        return "V"
    elif decimal == 4:
        return "IV"
    elif decimal>=6 and decimal<=8:
        return "V"+((int(decimal)-5)*"I") 
    elif decimal==9:
        return "IX"
    elif decimal==10:
        return "X"
    elif decimal>=11 and decimal <=13:
        return 'X'+(int(decimal)-10)*'I'
    elif decimal==20:
        return 'XX'
class TestDecimalToRoman(unittest.TestCase):

    def test_1(self):

        resultado = decimal_to_roman(1)

        self.assertEqual(resultado, "I")
    
    def test_2(self):

        resultado = decimal_to_roman(2)

        self.assertEqual(resultado, "II")
    
    def test_3(self):

        resultado = decimal_to_roman(3)

        self.assertEqual(resultado, "III")
    
    def test_4(self):
        resultado = decimal_to_roman(4)

        self.assertEqual(resultado,'IV')

    def test_5(self):
        
        resultado = decimal_to_roman(5)

        self.assertEqual(resultado, "V")
    
    def test_6(self):
        resultado = decimal_to_roman(6)

        self.assertEqual(resultado,'VI')

    def test_7(self):
        resultado = decimal_to_roman(7)

        self.assertEqual(resultado,'VII')

    def test_8(self):
        resultado = decimal_to_roman(8)

        self.assertEqual(resultado,'VIII')

    def test_9(self):
        resultado = decimal_to_roman(9)

        self.assertEqual(resultado,"IX")

    def test_10(self):
        
        resultado = decimal_to_roman(10)

        self.assertEqual(resultado, "X")

    def test_11(self):
        
        resultado = decimal_to_roman(11)

        self.assertEqual(resultado, "XI")

    def test_12(self):
        
        resultado = decimal_to_roman(12)

        self.assertEqual(resultado, "XII")
    def test_13(self):
        
        resultado = decimal_to_roman(13)

        self.assertEqual(resultado, "XIII")

if __name__ == "__main__":
    unittest.main()
