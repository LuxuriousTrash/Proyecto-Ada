from random import choice

listaPal = ['murcielago','prueba', 'origen', 'almuerza']
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


print('\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\nJuego nuevo! \n')

for k in range(len(pal)):
  res.append('-')

letCorr = []

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

  if (let in letCorr):
    print(f'\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\nYa has adivinado esa letra, esoge otra\n')

  elif buenoMalo(let, pal) == 0:
    letCorr.append(let)
    print(f'\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\nAcertado! Va por buen camino\n')
  
  else:
    print(f'\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\nIncorrecto, usted pierde una vida\n')
  print(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

if juegoTerminado(res) == True:
  print(f'\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\nFin del juego\n\nFelicidades, ha conseguido adivinar la palabra\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')
elif vid == 0:
  print(f'\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\nFin del juego\n\nNo ha conseguido adivinar la palabra \n\nA que la proxima lo consigue!\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')


