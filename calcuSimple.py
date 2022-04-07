# -*- coding: utf-8 -*-
print("-----------------------------------baby2.2-------------------------------------")
print("-------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------")
print("-----------  *       *      ***********     *            *********  -----------")
print("-----------  *       *      *         *     *            *       *  -----------")
print("-----------  *********      *         *     *            *********  -----------")
print("-----------  *       *      *         *     *            *       *  -----------")
print("-----------  *       *      ***********     ********     *       *  -----------")
print("-------------------------------------------------------------------------------")
print("  -----------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------")
print(" ------------------------------------------------------------------------------")
print("----------------------------------Año-2022-------------------------------------")
print("----------------------------Bienvenido a Python 3.8----------------------------")


a = (int(input("Ingresa el numero 1 si eres una persona: ")))
b = (int(input("Ingresa el numero un numero para seguir!!: ")))
t = input("Ingrese s si quiere + o n para cancelar, div si quiere / , res para - , mul *: ")

c = a + b
s = False
d = s
n = True
f = n
div = n


while 1:        
    if t == "n":
        t = input("Quiere restar preciona s , n para cancelar, div para dividir , res para restar ??: ")
        if t == "s":
            a = (int(input("Ingrese el numero: ")))
            b = (int(input("Ingrese el numero: ")))
            q = a - b
            print(q)
            break
        elif t == "n":
                print("Resta terminada")
                break
            
    if t == "div":
        print("Bienvenido -----Ingresamos ala division --------")
        t = input("Quiere dividir preciona s , n para cancelar, div para dividir, res para restar??: ")
        if t == "s":
            a = (int(input("Ingrese el numero: ")))
            b = (int(input("Ingrese el numero: ")))
            z = a / b
            print("El Resultado es :",(z))
            break
        elif t == "n":
            print("terminado div")
            break
        
    if t == "s":
        print("Bienvenido ------------------------Ingresamos ala suma -------------------------------")
        t = input("Quiere sumar preciona s , n para cancelar, div para dividir, res para restar??: ")
        if t == "s":
            a = (int(input("Ingrese el numero: ")))
            b = (int(input("Ingrese el numero: ")))
            c = a + b
            print("El resultado es: ",(c))
            break
        elif t == "n":
            print("Suma Terminada")
            print("--------------------------------------------------------")
            break

    if t == "res":
        print("Bienvenido -----Ingresamos ala resta --------")
        t = input("Quiere restar preciona s , n para cancelar, div para dividir, res para restar??: ")
        if t == "s":
            a = (int(input("Ingrese el numero: ")))
            b = (int(input("Ingrese el numero: ")))
            c = a - b
            print("El resultado es: ",(c))
            break
        elif t == "n":
            print("resta Terminada")
            break
        
    if t == "mul":
        print("Bienvenido -----Ingresamos ala mul --------")
        t = input("Quiere mul preciona s , n para cancelar, div para dividir, res para restar??: ")
        if t == "s":
            a = (int(input("Ingrese el numero: ")))
            b = (int(input("Ingrese el numero: ")))
            j = a * b
            print("El resultado es: ",(j))
            break
        elif t == "mul":
            print("mul Terminada")
            break
    


            b = int(input("Cual es tu edad:"))
            if b >= 18:
                print("Todo ok",(b),"años")            
            elif b <= 17:
                b = int(input("Cual es tu edad:"))
                print("Tienes que ser mayor de 17")
                if b >=18:
                    print("correcto")
                else:
                    print("error")
                    break
            else:
                print("Tenes que ser mayor de 18 años", (a))
                break





