""" Elabora un algoritmo que permita ingresar un número entero de 1 a 10 y muestre su equivalente escrito en número romano.
"""
numero = int(input("Digite un número: "))

if numero == 1:
    print("I")
else:
    if numero == 2:
        print("II")
    else:
        if numero == 3:
            print("III")
        else:
            if numero == 4:
                print("IV")
            else:
                if numero == 5:
                    print("V")
                else:
                    if numero == 6:
                        print("VI")
                    else:
                        if numero == 7:
                            print("VII")
                        else:
                            if numero == 8:
                                print("VIII")
                            else:
                                if numero == 9:
                                    print("Ix")
                                else:
                                    if numero == 10:
                                        print("x")
