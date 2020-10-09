def es_palindromo(frase):
    """
    Funcion que determina si una frase ingresada es un palindromo.

    Args:
        frase (String): Texto correspondiente a la frase a evaluar.

    Returns:
        Boolean: Es o no es un palindromo.
    """
    frase = frase.replace(" ","")
    if frase == frase[::-1]:
        return True
    else:
        return False


def main():
    salir = False
    while not salir:
        frase_ingresada = input("\nIngrese una frase, oración o palabra: ").strip()
        largo_texto = len(frase_ingresada) + 25
        print("\n" + "*" * largo_texto)
        if es_palindromo(frase_ingresada):
            print(f"'{frase_ingresada}' SI es un palindromo")
        else:
            print(f"'{frase_ingresada}' NO es un palindromo")
        print("*" * largo_texto)
        while True:
            desicion_salir = input("\nIngrese una opcion:\n\n1 - Salir\n2 - Continuar e ingresar otra frase\n\n"
                                   "Desea seguir? ")
            if desicion_salir == "1":
                print("\nHasta luego!\n")
                salir = True
                break
            elif desicion_salir == "2":
                break
            else:
                print("\nIngrese una opción válida")


if __name__ == '__main__':
    main()