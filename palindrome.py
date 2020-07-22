def esPalindromo(frase):
    """
    Funcion que determina si una frase ingresada es un palindromo.
    Args:
        frase (String): Texto correspondiente a la frase a evaluar.
    Returns:
        Boolean: Es o no es un palindromo.
    """
    frase = frase.replace(" ","")
    if frase == frase.reverse():
        return True
    else:
        return False

def main():
    pass

if __name__ == '__main__':
    main()