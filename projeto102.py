print("1- Somar")
print("2- subtrair")
print("3- Dividir")
print("4- multiplicar")
print("5- baskara")
acao = int(input("O que você deseja fazer?"))

def Somar(x,y):
    resultado = x + y
    print(resultado)
def Subtrair(x,y):
    resultado = x - y
    print(resultado)
def Dividir(x,y):
    resulado = x/y
    print(resulado)
def Multiplicar(x,y):
    resulado = x*y
    print(resulado)
def bhaskara(a,b,c):
  delta = (b**2 - 4*a*c)
  if(delta >= 0):
    print("O valor de delta é:")
    print(delta)
    x1 = (-b + delta**(1/2))/(2*a)
    print("O valor de x1 é:")
    print(x1)
    x2 =(-b - delta**(1/2))/(2*a)
    print("O valor de x2 é:")
    print(x2)
    print("")
  else:
    print("O valor de Delta é negativo.")
if acao == 1:  
    somar1 = int(input("Você deseja somar, O "))
    print("com")
    somar2 = int(input())
    Somar(somar1, somar2)
elif acao == 2:
    subtrair1 = int(input("Você deseja subtrair, O "))
    print("com")
    subtrair2 = int(input())
    Subtrair(subtrair1, subtrair2)
elif acao == 3:
    dividir1 = int(input("Você deseja dividir, O "))
    print("com")
    dividir2 = int(input())
    Dividir(dividir1, dividir2)
elif acao == 4:
    multiplicar1 = int(input("Você deseja multiplicar, O "))
    print("com")
    multiplicar2 = int(input())
    Multiplicar(multiplicar1, multiplicar2)
elif acao == 5:
    x1 =  int(input("Qual o valor de a?"))
    x2 =  int(input("Qual o valor de b?"))
    x3 =  int(input("Qual o valor de c?"))
    bhaskara(x1,x2,x3)


