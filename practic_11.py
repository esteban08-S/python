print("ingrese la cantidad de autos q se vendieron")
autosVendidos=int(input())

print("ingrese el valor de los autos")
valorAuto=float(input())

salarioTotal = 5500 + 200 * autosVendidos + valorAuto * 5/100

print("el salario total es", salarioTotal)
