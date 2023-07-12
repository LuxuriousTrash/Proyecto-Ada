from random import choice

listaPal = ['jaja','nelson', 'mandela']
pal = ''
letUn = ''
let = ''
res = []
vid = 5
num = int


def elegir_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))
    return palabra_elegida, letras_unicas


pal, letUn = elegir_palabra(listaPal)


def compara(letra, palabra, resultado):
    letra = letra.lower()
    palabra = palabra.lower()
    for i in range(len(palabra)):
      if letra == palabra[i]:
        resultado[i] = palabra[i]
      else:
        if resultado[i] != '-' and resultado[i] != letra:
          resultado[i]=resultado[i]
        else:
          resultado[i] = '-'

def buenoMalo(letra, palabra):
  if letra.lower() in palabra.lower():
    return 0
  else:
    return 1


def juegoTerminado(resultado):
  return not any(filter(lambda x: (x == '-'), resultado))


print('Juego nuevo! \n')

for k in range(len(pal)):
  res.append('-')

while vid >= 1 and juegoTerminado(res) == False:

  jres = ''.join(res)
  print(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
  print(f'La palabra es \'{jres}\' \n')
  print(f'La palabra tiene {len(pal)} letras.')
  print(f'La palabra tiene {letUn} letras unicas')
  print(f'Tiene {vid} vidas \n')

  let = input('Introduzca una letra: ')
  while let.isalpha() == False:
    let = input('Introduzca una letra: ')


  compara(let, pal, res)
  vid -= buenoMalo(let, pal)

  if buenoMalo(let, pal) == 0:
    print(f'\nAcertado! Va por buen camino \n')
  else:
    print(f'\nIncorrecto, usted pierde una vida \n')
  print(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

if juegoTerminado(res) == True:
  print(f'Fin del juego\n\nFelicidades, ha conseguido adivinar la palabra')
elif vid == 0:
  print(f'Fin del juego\n\nNo ha conseguido adivinar la palabra \n\nA que la proxima lo consigue!')




