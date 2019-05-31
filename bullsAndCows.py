
# modulo que va a permitir elegir numeros aleatoriamente
import random

# el conjunto de simbolos validos en el codigo*
digitos = ('0','1','2','3','4','5','6','7','8','9')

# "elegimos" el codigo
cantDigitos = 4
codigo = ''
for i in range(cantDigitos):
    candidato = random.choice(digitos)
    # vamos eligiendo digitos no repetidos
    while candidato in codigo:
        candidato = random.choice(digitos)
    codigo = codigo + candidato

# iniciamos interaccion con el usuario
print ("Bienvenido/a Bulls & Cows!")
print ("Tienes que adivinar un numero de", cantDigitos, 
      "cifras")
propuesta = input("¿Que codigo propones?: ")

# procesamos las propuestas e indicamos aciertos y coincidencias
intentos = 1
while propuesta != codigo and propuesta != "me doy":
    intentos = intentos + 1
    aciertos = 0
    coincidencias = 0

    # recorremos la propuesta y verificamos en el codigo
    for i in range(cantDigitos):
        if propuesta[i] == codigo[i]:
            aciertos = aciertos + 1
        elif propuesta[i] in codigo:
            coincidencias = coincidencias + 1
    print ("Tu propuesta (", propuesta, ") tiene", aciertos, \
          "aciertos y ", coincidencias, "coincidencias.")
    # pedimos siguiente propuesta
    propuesta = input("Propón otro codigo: ")

if propuesta == "Me doy":
    print ("El codigo era", codigo)
    print ("Suerte la proxima vez!")
else:
    print ("Felicitaciones! Adivinaste el codigo en", \
    intentos, "intentos.")