def primo(num):

   div = num
   cont = 0

   while div != 0:
       resto = num % div
       if resto == 0:
           cont += 1
       div -= 1
	   
   if cont != 2:
       return False
   else:
       return True

qtd = int(input("Digite a quantidade de números primos desejados:"))

cont = 0
num = 2
while qtd > cont:
	if primo(num):
		print(num)
		cont += 1
	
	num += 1
        
