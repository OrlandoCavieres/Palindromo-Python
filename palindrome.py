def esPalindromo(frase):
    frase = frase.replace(" ","")
    if frase == frase.reverse():
        return True
    else:
        return False

def main():
    pass

if __name__ == '__main__':
    main()