def frecuencia(numero,digito):
   cantidad=0
   while numero!=0:
       ultDigito=numero%10
       if ultDigito==digito:
           cantidad+=1
       numero=numero//10
   return cantidad

 
num=int(input("Numero: "))
un_digito=int(input("Digito: "))
print("Frecuencia del digito en el numero:",frecuencia(num,un_digito))