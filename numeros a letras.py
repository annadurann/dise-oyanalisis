unidades = ['', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve']
decenas = ['', 'diez', 'veinte', 'treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa']
especiales = ['diez', 'once', 'doce', 'trece', 'catorce', 'quince', 'dieciséis', 'diecisiete', 'dieciocho', 'diecinueve']
cientos = ['', 'ciento', 'doscientos', 'trescientos', 'cuatrocientos', 'quinientos', 'seiscientos', 'setecientos', 'ochocientos', 'novecientos']

def numeros_letras(texto):
    try:
        numero = int(texto)
    except ValueError:
        return "Error, ingresa un número"

    numero_texto = ''

    if numero == 0:
        numero_texto = 'cero'

    elif numero < 10:
        numero_texto = unidades[numero]

    elif numero < 20:
        numero_texto = especiales[numero - 10]

    elif numero < 100:
        decena, unidad = divmod(numero, 10)
        if unidad == 0:
            numero_texto = decenas[decena]
        else:
            numero_texto = decenas[decena] + ' y ' + unidades[unidad]

    elif numero < 1000:
        centena, resto = divmod(numero, 100)
        if resto == 0:
            numero_texto = cientos[centena]
        else:
            numero_texto = cientos[centena] + ' ' + numeros_letras(resto)

    elif numero < 1000000:
        millar, resto = divmod(numero, 1000)
        if resto == 0:
            numero_texto = numeros_letras(millar) + ' mil'
        else:
            numero_texto = numeros_letras(millar) + ' mil ' + numeros_letras(resto)

    elif numero < 1000000000:
        millon, resto = divmod(numero, 1000000)
        if resto == 0:
            numero_texto = numeros_letras(millon) + ' millones'
        else:
            numero_texto = numeros_letras(millon) + ' millones ' + numeros_letras(resto)

    elif numero < 1000000000000:
        billon, resto = divmod(numero, 1000000000)
        if resto == 0:
            numero_texto = numeros_letras(billon) + ' mil millones'
        else:
            numero_texto = numeros_letras(billon) + ' mil millones ' + numeros_letras(resto)

    elif numero < 1000000000000000:
        trillon, resto = divmod(numero, 1000000000000)
        if resto == 0:
            numero_texto = numeros_letras(trillon) + ' billones'
        else:
            numero_texto = numeros_letras(trillon) + ' billones ' + numeros_letras(resto)

    elif numero < 1000000000000000000:
        cuatrillon, resto = divmod(numero, 1000000000000000)
        if resto == 0:
            numero_texto = numeros_letras(cuatrillon) + ' trillones'
        else:
            numero_texto = numeros_letras(cuatrillon) + ' trillones ' + numeros_letras(resto)

    return numero_texto

texto = input("Número: ")
letras = numeros_letras(texto)
print(letras)
