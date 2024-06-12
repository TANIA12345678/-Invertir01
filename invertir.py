

def invertir_cadena(cadena):
    return cadena[::-1]

# Solicitar al usuario que ingrese una cadena
cadena_original = input("Ingrese una cadena de caracteres: ")

# Invertir la cadena usando la función invertir_cadena
cadena_invertida = invertir_cadena(cadena_original)

# Imprimir la cadena invertida
print("La cadena invertida es:", cadena_invertida)