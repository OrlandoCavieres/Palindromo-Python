def esPalindromo(frase):
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
        fraseIngresada = input("\nIngrese una frase, oración o palabra: ").strip()
        largoTexto = len(fraseIngresada) + 25
        print("\n" + "*" * largoTexto)
        if esPalindromo(fraseIngresada):
            print(f"'{fraseIngresada}' SI es un palindromo")
        else:
            print(f"'{fraseIngresada}' NO es un palindromo")
        print("*" * largoTexto)
        while True:
            desicionSalir = input("\nIngrese una opcion:\n\n1 - Salir\n2 - Continuar e ingresar otra frase\n\nDesea seguir? ")
            if desicionSalir == "1":
                print("\nHasta luego!\n")
                salir = True
                break
            elif desicionSalir == "2":
                break
            else:
                print("\nIngrese una opción válida")

if __name__ == '__main__':
    main()