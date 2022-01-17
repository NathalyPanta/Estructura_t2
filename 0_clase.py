
from tkinter import E


class Tarea2:
    def Ejercicio1 (self):
        # 1: TIPO DE DATOS
        print("===> TIPOS DE DATOS <===")
        a = 100/5  
        print(type(a))
        b = 7/2  
        print(type(b))
        c = 7//2 
        print(type(c))
        d = 7%2  
        print(type(d))
        e = "tiza"+"."  
        print(type(e))
        f = "hola"[1+1]  
        print((type(f)))
        g= len("hola") 
        print(type(g))
        h= int("145") 
        print(type(h))
        i=float("145")  
        print(type(i))
        j=float(145)  
        print(type(j))
        k=str(32) 
        print(type(k))
        l=1+2!=3  
        print(type(l))
        m=177%2==0  
        print(type(m))
        n=len("nube")<=20 
        print(type(n))
        
    def Ejercicio2 (self):
        #     Ejercicios resueltos (STRINGS)
        print("\n===> Strings <===")
        cadena = "si, profe, es cierto... yo me comi la tarea"
        x = cadena[10]
        y = cadena[-1]
        z = cadena[0:9]
        k = cadena[::3]
        l = cadena [::-1] # para obtener la cadena al revés
        print(cadena)
        print(x)
        print(y)
        print(z)
        print(k)
        print(l)
    
    def Ejercicio3 (self):
        #Solicitar al usuario que ingrese su nombre en una variable N
        #se debe mostrar en pantalla el texto "Ahora estás en la matrix, [usuario]"
        #reemplazar usuario por el nombre almacendao en N
        print("===> Matrix <===")
        N = str(input("Ingrese su nombre: "))
        print("Ahora estás en la matrix, ", N)
                
    def Ejercicio4 (self):
        #Solicitar al usuario costo de una cena en un restaurante, sumarle un 6.2%
        #Imprimir en pantalla el monto final a pagar 
        print("\n===> cena <===")
        costo_cena=float(input("Ingrese el valor de la cena: "))
        total=costo_cena + (costo_cena*0.162)
        print("EL valor total a pagar incluido el servicio es: {}" .format(total))
        
    def Ejercicio5 (self):
        #Solicitar al usuario que ingrese el dia, mes y año de su nacimiento y almacenar como entero
        #Mostrar la fecha en formato dd/mm/aaaa
        #Hacer otra version del programa, pero esta vez almacenando todo una unica variable numerico, en la forma DDMMAAAA.
        print("\n===> fecha <===")
        dia=int(input("Dia de tu nacimiento: "))
        mes=int(input("Mes de tu nacimiento: "))
        anio=int(input("Año de tu nacimiento: "))
        print(dia,"/",mes,"/",anio)
    
    def Ejercicio6(self):
                
        print("\n===> fecha2 <===")
        fecha=input("Fecha en formato DDMMAAAA: ")
        dia=fecha[:2]
        mes=fecha[2:4]
        anio=fecha[4:]
        print(dia,"/",mes,"/",anio)
        
    def Ejercicio6_1 (self):
        #     Ejercicios de if-else y (elif)
        # Escribir un programa que, dado un numero entero, muestre su valor absoluto. 

        print("\n===> valor absoluto <===")
        numero=int(input("Numero: "))
        if numero<0:
            numero=numero*-1
        print("EL valor absoluto es ", numero)

    def Ejercicio7 (self):
        # Solicitar al usuario que ingrese los nombres de dos personas, en 2 variables distintas.
        # Imprimir "coincidencia" si los nombres comienzan con la misma letra o si terminan con la misma letra. 
        # Si no es asi, imprimir "no hay coincidencia". 
        print("\n===> coincidencia <===")
        nombre1=input("Un nombre: ")
        nombre2=input("Otro nombre: ")
        indice_final_nombre1=len(nombre1)-1
        indice_final_nombre2=len(nombre2)-1
        if nombre1[0]==nombre2[0] or nombre1[indice_final_nombre1]==nombre2[-1]:
            print("Coincidencia")
        else:
            print("No hay coincidencia")
    
    def Ejercicio8 (self):
        # Solicitar una letra y si es una vocal, mostrar el mensaje "es vocal". 
        # Validar que el usuario ingrese solo un caracter. 
        # Si ingresa un string de mas de un caracter, informar que no se puede procesar el dato. 
        print("\n===> vocal <===")
        letra=input("letra: ")
        if len(letra)!=1:
            print("Debe ser solo una letra")
        else:
            if letra.lower() in "aeiou":
                print("Es vocal")
                
    def Ejercicio9 (self):
        # Imprimir todos los dígitos decimales, del 0 al 9, utilizando una repetición.
        print("\n===> valor absoluto <===")
        for y in range(10):
            print(y)
            
    def Ejercicio10 (self):
        # Imprimir todos los números entre el 100 y el 199.
        print("\n===> * <===")
        for x in range(100,200):
            print(x)
            
    def Ejercicio11 (self):
        #Pedir al usuario que ingrese un número entero positivo
        #Imprimir todos los números correlativos entre el ingresado por el usuario y uno menos del doble del mismo.
        print("\n===> Num <===")
        n=int(input("INGRESE NUMERO: "))
        for x in range(n, n*2):
            print(x)
            
    def Ejercicio12 (self):
        #Ingresar una frase e imprimir un listado de las vocales que aparecen sin repetirlas.
        print("\n===> vocales <===")
        f=input("Ingrese su frase: ")
        print("Estas son las vocales que aparecen en su frase:")
        for x in "aeiou":
            if x in f:
                print(x)
                
    def Ejercicio13 (self):
    #cantidad de vocales
        print("\n===> cantidad de vocales <===")
        fr=input("Ingrese su frase: ")
        cant=0
        for x in fr:
            if x in "aeiou":
                cant+=1
        print("La cantidad de vocales que hay en su frase son: {}" .format (cant))
        
    def Ejercicio14 (self):
         # sumatoria de todos los números entre el 0 y el 100.
        print("\n===> sumatoria <===")
        total=0
        for i in range(101):
            total=total+i
        print("Sumatoria:", total)

    def Ejercicio15 (self):
        # Sumatoria de los múltiplos de 3 encontrados entre el 0 y el 100
        print("\n===> sumatoria multiplos de 3 <===")
        total=0
        for i in range(101):
            if i%3==0:
                total=total+i
        print("Sumatoria:", total)

    def Ejercicio16 (self):
        # Dado un número entero positivo, mostrar su factorial. 
        # El factorial de un número se obtiene multiplicando todos los números enteros positivos que hay entre el 1 y ese número.
        print("\n===> factorial <===")
        num=int(input("INGRESE NUMERO:"))
        f=1
        if num!=0:
            for i in range(1,num+1):
                f=f*i
        print("Factorial: {}" .format(f))

    def Ejercicio17 (self):
        # Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. 
        # La sucesión comienza con los números 0 y 1 y, 
        # a partir de éstos, cada elemento es la suma de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…
        print("\n===> sucesion de Fibonacci  <===")
        n1=0
        n2=1
        print(n1)
        print(n2)
        for i in range(8):
            n3=n1+n2
            print(n3)
            n1=n2
            n2=n3
    
    def Ejercicio18(self):
        # Escribir un programa que permita al usuario ingresar 6 números enteros, que pueden ser positivos o negativos. 
        # Mostrar la sumatoria de los números negativos y el promedio de los positivos.
        # No es posible dividir por cero. Es necesario evitar que el programa arroje un error si no se ingresaron números positivos.
        print("\n===> sumatoria <===")
        sumpo = 0
        cantpo = 0
        sumne = 0
        for i in range(6):
            nro = int(input("Número: "))
            if nro > 0:
                sumpo = sumpo+nro
                cantpo = cantpo+1
            else:
                sumne = sumne+nro
        print("Sumatoria de los negativos: ", sumne)
        if cantpo != 0:
            print("Promedio de los positivos: ", sumpo/cantpo)
        else:
            print("No se ingresaron números positivos")
            
Excr = Tarea2()
Excr.Ejercicio1()
Excr.Ejercicio2()
Excr.Ejercicio3()
Excr.Ejercicio4()
Excr.Ejercicio5()
Excr.Ejercicio6()
Excr.Ejercicio6_1()
Excr.Ejercicio7()
Excr.Ejercicio8()
Excr.Ejercicio9()
Excr.Ejercicio10()
Excr.Ejercicio11()
Excr.Ejercicio12()
Excr.Ejercicio13()
Excr.Ejercicio14()
Excr.Ejercicio15()
Excr.Ejercicio16()
Excr.Ejercicio17()
Excr.Ejercicio18()