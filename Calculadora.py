# %%
def soma (x,y):
  print(f"A soma de {x} + {y} é {x+y}")
def multi (x,y):
  print(f"O produto de {x} x {y} é {x*y}")
def divi (x,y):
  print(f"A divisão entre {x} e {y} é {x/y}")
def sub (x,y):
  print(f"A subtração de {x} - {y} é {x-y}")
while True:
 oper = input("Digite o número da operação desejada \n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n")
 if oper.isnumeric():
   oper=int(oper)
   if oper >= 1 and oper <= 4:
    break
   else:
     print("Digite um caractere válido.")
 elif oper.isalpha():
   print("Digite um caractere válido.")
while True:
  valor1 = input("Digite o primeiro valor \n")
  if valor1.isnumeric():
    valor1=int(valor1)
    break
  if valor1.isalpha():
    print("Digite um caractere válido.")
while True:
  valor2 = input("Digite o segundo valor \n")
  if valor2.isnumeric():
    valor2=int(valor2)
    break
  if valor2.isalpha():
    print("Digite um caractere válido")
if oper == 1:
  soma(valor1,valor2)
if oper == 2:
  sub(valor1,valor2)
if oper == 3:
  multi(valor1,valor2)
if oper == 4:
  divi(valor1,valor2)


