print("ingrese una fecha con dia,mes y año")
fecha=int(input())

año = fecha % 10000

mes = fecha // 10000 % 100

dia = fecha / 1000000


print("dia :", dia)
print("mes :", mes)
print("año :", año)
