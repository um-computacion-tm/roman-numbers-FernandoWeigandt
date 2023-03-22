import unittest

def decimal_to_roman(decimal):
    #diccionario con los numeros romanos
    romanos = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}
    #lista de los numeros romanos
    lista = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    #variable para almacenar los numeros romanos
    romano = ''
    #ciclo para recorrer la lista
    for i in lista:
        #ciclo para obtener los numeros romanos del 1 al 1000
        while decimal >= i:
            #variable para almacenar los numeros romanos
            romano += romanos[i]
            #variable para obtener los numeros romanos
            decimal -= i
    #retornar el decimal romano
    return romano

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

    def test_14(self):
            
            resultado = decimal_to_roman(14)
    
            self.assertEqual(resultado, "XIV")

    def test_15(self):
        
        resultado = decimal_to_roman(15)

        self.assertEqual(resultado, "XV")

    def test_16(self):
        
        resultado = decimal_to_roman(16)

        self.assertEqual(resultado, "XVI")

    def test_17(self):
        
        resultado = decimal_to_roman(17)

        self.assertEqual(resultado, "XVII")

    def test_18(self):
        
        resultado = decimal_to_roman(18)

        self.assertEqual(resultado, "XVIII")

    def test_19(self):
        
        resultado = decimal_to_roman(19)

        self.assertEqual(resultado, "XIX")

    def test_20(self):

        resultado = decimal_to_roman(20)

        self.assertEqual(resultado,"XX")

    def test_30(self):

        resultado = decimal_to_roman(30)

        self.assertEqual(resultado,"XXX")

    def test_60(self):

        resultado = decimal_to_roman(60)

        self.assertEqual(resultado,"LX")

    def test_70(self):

        resultado = decimal_to_roman(70)

        self.assertEqual(resultado,"LXX")

    def test_80(self):

        resultado = decimal_to_roman(80)

        self.assertEqual(resultado,"LXXX")

    def test_90(self):

        resultado = decimal_to_roman(90)

        self.assertEqual(resultado,"XC")

'''
class TestDecimalToRoman(unittest.TestCase):

    def test_n(self):
        for i in range(1, 1000):
            resultado = decimal_to_roman(i)

            self.assertEqual(resultado, )
'''

#Como lo generalizo??

if __name__ == "__main__":
    unittest.main()