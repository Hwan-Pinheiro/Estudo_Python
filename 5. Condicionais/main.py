#Exemplo de Condicionais
salario = float(input("Informa seu salario:"))

if salario <= 3000:
   print("programador junior")
elif salario > 3000 and salario < 6000:
     print("programador pleno")
elif salario > 6000 and salario < 15000:
     print("programador senior")