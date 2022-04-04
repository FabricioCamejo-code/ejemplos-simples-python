# -*- coding: utf-8 -*-

print("-----------------------------------baby2.2-------------------------------------")
print("-------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------")
print("-----------  *       *      ***********     *            *********  -----------")
print("-----------  *       *      *         *     *            *  1    *  -----------")
print("-----------  *********      *         *     *            *********  -----------")
print("-----------  *       *      *         *     *            *       *  -----------")
print("-----------  *       *      ***********     ********     *       *  -----------")
print("-------------------------------------------------------------------------------")
print("  -----------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------")
print(" ------------------------------------------------------------------------------")
print("----------------------------------Año-2022-------------------------------------")
print("----------------------------Bienvenido a Python 3.8----------------------------")


import time

def personales():
    while 1:
        try:
            a = str(input("Cual es tu nonmbre:"))
            if a.isnumeric():
                print("error desde la evaluacion",(a))
                if a.isnumeric():
                    print("Ingrese un nombre valido")
                    a = str(input("Cual es tu nonmbre:"))
                    if a.isnumeric():
                        print("in-correcto")
                        a = str(input("Cual es tu nonmbre nuevamente:"))
                        if a.isnumeric():
                            print("Losiento terminado por  mal ingresos")
                            return a
                        else:
                            print("Correcto el nombre",(a))
                    else:
                        print("correcto-nombre",(a))
                else:
                    print("Error Terminado")
            elif a == int:
                a = str(input("Ingresa un nonmbre:"))
            else:
                print("Todo ok",(a))
        except:
            print("Error por favor ingresa un valor numerico")
            


        
        try:
            b = int(input("Cual es tu edad:"))
            if b >= 18:
                print("Todo ok",(b),"años")
            else:
                print("Tenes que ser mayor de 18 años", (a))
                b = int(input("Cual es tu edad:"))
                if b >=18:
                    print("correcto Eres mayor de 18")
                else:
                    print("Termina")
        except ValueError:
            print("Error ingrese numero desde personales")
            break
        

            

        try:
            c = str(input("Cual es tu localidad:"))
            if c.isnumeric():
                print("Error en localidad", (c))
                if c.isnumeric():
                    print("Ingresa Localidad")
                    c = str(input("Cual es tu localidad:"))
                    if c.isnumeric():
                        print("Terminado por varios intentos sin exito")
                        return c
                    else:
                         print("Correcta Localidad")
                else:
                    print("Correcto el localidad",(c))
            elif c == int:
                c = str(input("Ingresa un Localidad:"))
                break
            else:
                 print("Correcto con la  localidad de ",(c))
        except:
             print("error")



             

        try:
            d = str(input("Cual es tu pais:"))
            if d.isnumeric():
                print("Eerror en pais", (d))
                return d
            elif d == int:
                d = str(input("Ingresa un Pais:"))
            else:
                print("Correcto pais:",(d))
        except:
            print("Error")



        list(a)
        list(c)
        list(d)
        print("------------------Bienvenido a las preguntas Generales,Mundiales-----------------")
        print("Bienvenido  sñor/ar",(a),"de Edad",(b),"de la Localidad de ",(c)," y del Pais de",(d))
        print("------------------¡¡Comenzaremos con las preguntas!!-----------------\n")
        timeuno = time.ctime()
        print(timeuno)
        print("¿¿Cuando fue fundada-declarada la ciudad de Rosario??")        
                    
        

        def nueva():
            try:
                s = int(input("desea continuar precione 1 para continuar tiene 15 segundos:"))
                if s == 1:
                    print("Correcto 1")
                else:
                    print("termmina")
                    
                    if s >= 2:
                        print("incorect")
                    else:
                         print("Terminado")
                    return

                    if s <= 0:
                              print("incorect")
                    else:
                         print("Terminado")
                    return
                
                print("marque 1 = 5 de agosto de 1852")
                print("marque 2 = 21 de abril de 1752")
                print("marque 3 = 11 de nobienbre de 1862")
                print("marque 4 = 12 de febrero de 1552")
                r = range(0,15)
                for x in r:
                    r = 15
                    x -= 15
                    time.sleep(1)
                    print("Ingresa",(x))
                else:
                     print("Tiempo terminado")

                p = int(input("Bien Cual es su respuesta:"))                           
                if p == 1:
                    print("Correcto eres un genio")
                else:
                     print("Incorrecto")
            
            except ValueError:
                print("Incorrecto Error")
                   
        nueva()
        
            
        

        
        


        try:
            s = int(input("desea continuar precione 1 para continuar tiene 15 segundos:"))
            if s == 1:
                print("Correcto 1")
            else:
                print("termmina")
                    
                if s >= 2:
                    print("incorect")
                else:
                    print("Terminado")
                return

                if s <= 0:
                        print("incorect")
                else:
                    print("Terminado")
                    return

            print("¿¿Cuantas provincias hay en Argentina??")        
            print("Ingrese la opcion1 = 14")
            print("Ingrese la opcion2 = 30")
            print("Ingrese opcion3 = 24")
            print("Ingrese la opcion4 = 32")
            r = range(0,15)
            for x in r:
                r = 15
                x -= 15
                time.sleep(1)
                print("Ingresa",(x))
            else:
                print("Tiempo terminado")

            pa = int(input("Ingresa una Respuesta: "))
            if pa == 24:
                print("Correcto eres un genio")
            else:
                print("Incorrecto")
            
        except:
            print("Error")






            
                  

        try:
            s = int(input("desea continuar precione 1 para continuar tiene 15 segundos:"))
            if s == 1:
                print("Correcto 1")
            else:
                print("termmina")
                    
                if s >= 2:
                    print("incorect")
                else:
                    print("Terminado")
                return

                if s <= 0:
                        print("incorect")
                else:
                    print("Terminado")
                    return

            print("¿¿Cuál es el sistema de gobierno en Argentina??")        
            print("Ingrese 1 si es correcto = republica representativa")
            print("Ingrese 2 si es correcto  = dictadura")
            print("Ingrese 3 si es correcto = monarquia constitucional")
            print("Ingrese 4 si es correcto = ninguna")

            r = range(0,15)
            for x in r:
                r = 15
                x -= 15
                time.sleep(1)
                print("Ingresa",(x))
            else:
                print("Tiempo terminado")

            pa = int(input("Ingresa una Respuesta: "))
            if pa == 1:
                print("Correcto eres un genio")
            else:
                print("Incorrecto")
            
        except:
            print("Error")

personales()



