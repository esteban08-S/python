print("ingrese una nota de examen entre 0 y 10")
nota1=int(input())

print("ingrese una nota de TP entre 0 y 10")
nota2=int(input())

print("ingrese una nota de un examen integrador entre 0 y 10")
nota3=int(input())

notaFinal = nota1 * 30/100 + nota2 * 20/100 + nota3 * 50/100
print("la nota final es:", notaFinal)