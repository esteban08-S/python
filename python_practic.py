def practic_1():
 print ("ingrese dos numeros")

num1=int(input())
num2=int(input())

R= num1 + num2
print("la suma del numero ingresado es", R)
#defpractic_1()

def practic_2():
    print ("ingrese 4 numeros para saber su suma")

num1=int(input())
num2=int(input())
num3=int(input())
num4=int(input())

R = num1 + num2 + num3 + num4
 
print("la suma de sus numeros son", R)

#defpractic_2()

def practic_3():
     print ("pone los dos lados de un rectangulo")
num1=int(input())
num2=int(input())

R = num1 * num2

print("la superficie del rectangulo es", R)
#defpractic_3()

def practic_4():
     print("pon un numero q represente el lado de un cuadrado")
num1=float(input())

R= num1 * num1

print("la superficie de un cuadrado es", R)
#defpractic_4():

def practic_5():
      print("ingrese hora")
hora=int(input())
print("ingrese minuntos")
minutos=int(input())
print("ingrese segundos")
segundos=int(input())

R= hora * 3600 + minutos * 60 * segundos

print("el resultado es", R, "segundos")
#defpractic_5()

def practic_6():
    print ("ingrese base")
base=int(input())
print ("ingrese altura")
altura=int(input())

R = base * altura /2
print("la superficie de su triangulo es", R)
#defpractic_6():

def practic_7():

   print("ingresa numero")
num1=int(input())
print("ingresa numero")
num2=int(input())
print("ingresa numero")
num3=int(input())
print("ingresa numero")
num4=int(input())
print("ingresa numero")
num5=int(input())
print("ingresa numero")
num6=int(input())

R = num1 + num2 + num3 + num4 + num5 + num6 /6

print("el promedio de estos numeros es", R)
#defpractic_7()

def practic_8():
    print("ingrese un numero")
num1=int(input())
print("ingrese otro numero")
num2=int(input())

R = num1 * 100 / num2

print("el percentaje q representa el primero numero del segundo es", R,"%")
#defpractic_8()

def practic_9():
 print("ingrese una fecha con dia,mes y año")
fecha=int(input())

año = fecha % 10000

mes = fecha // 10000 % 100

dia = fecha // 1000000


print("dia :", dia)
print("mes :", mes)
print("año :", año)
#def practic_9():

def practic_10():
   print("ingrese una nota de examen entre 0 y 10")
nota1=int(input())

print("ingrese una nota de TP entre 0 y 10")
nota2=int(input())

print("ingrese una nota de un examen integrador entre 0 y 10")
nota3=int(input())

notaFinal = nota1 * 30/100 + nota2 * 20/100 + nota3 * 50/100
print("la nota final es:", notaFinal)
#defpractic_10()

def practic_11():
   print("ingrese la cantidad de autos q se vendieron")
autosVendidos=int(input())

print("ingrese el valor de los autos")
valorAuto=float(input())

salarioTotal = 5500 + 200 * autosVendidos + valorAuto * 5/100

print("el salario total es", salarioTotal)
#defpractic_11():







