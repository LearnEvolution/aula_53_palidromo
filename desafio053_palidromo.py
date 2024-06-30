# Crie um programa que leia uma frase qualquer 
# e diga se ela é um palidromo,
# desconsiderando os espaços 

z = str(input("DIGITE UMA FRASE OU UMA PALAVRA PALIDROMO >>> ")).upper()   
f = z.strip().split()                                                    
b = "".join(f)
a = b[::-1]
print("O INVERSO DE {} É {} ".format(z , a))
if b == a :
 print(" {} \033[34mÉ UMA FRASE PALIDROMO ".format(z)) 
else:
 print(" {} \033[31mNÃO É UMA PALAFRA PALIDROMO".format(z))

 