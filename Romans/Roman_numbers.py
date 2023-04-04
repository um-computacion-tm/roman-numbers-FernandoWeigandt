
def decimal_to_roman(decimal):
    cifras_romanas = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    cifras_decimales = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    
    romano = ""
    i = 0

    while decimal > 0:
        if decimal >= cifras_decimales[i]:
            romano += cifras_romanas[i]
            decimal -= cifras_decimales[i]
        else:
            i += 1

    return romano


def romano_a_decimal(romano):
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    resultado = 0
    previo = 0
    
    for letra in romano[::-1]:
        valor = valores[letra]
        if valor < previo:
            resultado -= valor
        else:
            resultado += valor
        previo = valor
    
    return resultado