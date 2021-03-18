#TODO'S:
  # Contar los 1's con una REGEX.
from random import randint

def dec_to(num, sistema = 2):
  valores_hexa = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
  if (sistema > 1 and sistema < 17):
    valor_ret = []
    while num:
      num, residuo = divmod(num, sistema)
      valor_ret.append(valores_hexa[residuo]) if (residuo > 9) else valor_ret.append(str(residuo))
    return ''.join(valor_ret[::-1])
  return 'Verifica que el sistema al que deseas convertir sea válido'

individuos = int(input("Por favor ingrese el número de individuos: "))

count = 0

poblacion = []
total = 0
while count < individuos:

    num = randint(0, 1023)

    poblacion.append({
        'id_individuo': count,
        'decimal': num,
        'binario': dec_to(num),
        'aptitud': 0
    })

    for item in poblacion[count]["binario"]:
        if int(item) == 1:
            poblacion[count]["aptitud"] += 1

    total += poblacion[count]["aptitud"]
    count += 1

count = len(poblacion)
padres = []
aptitud_total = 0
r = 0

while count > 0:
    r = randint(0, total)
    for ind in poblacion:
        
        aptitud_total += ind["aptitud"]

        if aptitud_total >= r:
            break
           
    padres.append(ind)
    aptitud_total = 0
    count -= 1

for padre in padres:
    print(padre)
