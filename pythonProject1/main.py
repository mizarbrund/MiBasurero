from random import seed
from random import randint
import time
sujetos =["John el Caza Recompensas" , "el sucio Dan" , "Loreta, La posadera" , "Denis, El veterano" , "Enola, El apache"]
armas = ["El rifle henry" , "Un revolver" , "La escopeta" , "la Bayoneta" , "La Tomahawk"]
locaciones = ["el bar" , "la sala de juegos" , "el pasillo" , "la bodega" , "el sotano"]

lugarIndex=randint(0,4)
lugar = locaciones[lugarIndex]
asesIndex=randint(0,4)
asesino = sujetos[asesIndex]

sujetos.remove(asesino)
muertoIndex=randint(0,3)
muerto = sujetos[muertoIndex]
#print("el muerto es ", muerto)
#print ("y el asesino es", asesino)
#print('lo mato en', lugar)
dialogo1 = "Ha sido un invierno terrible, las nevadas han sepultado a los menos afortunados con todo y sus carrozas, y a los mas afortunados, los ha mantenidos encerrados durante dias en cualquier lugar en el que lugar en el que puedan escapar del frio, en las pocas cabanas que hay en los largos caminos de un pueblo a otro, algunos afortunados desafortunados viajeros se quedan atrapados por los metros de nieve y las bajas temperaturas, usualmente en estas cabanas se la suelen pasar en armonia, usualmente"
dialogo2="Esta vez los inquilinos que se quedaron atrapados fueron varios, permiteme presentartelos, el primero es  Jhon el caza recompensas, se mueve a traves de todo el oeste recolectando las recompensas ofrecidas por cazar criminales, su rifle henry podra ser viejo, pero sigue igual de preciso que cuando nuevo."
dialogo3="Ya que estamos hablando de Jhon, hablemos de su acompanante, el sucio Dan, buscado en varios condados por asaltar bancos con su revolver peace maker, tiene encima una recompensa de 150 dolares"
dialogo4="La posada siempre es un lugar lindo para pasar las tormetas invernales, Loreta la posadera es una persona de lo mas amable, y su sazon es muy dificil de superar, pero no te dejes enganar, puede que sea muy amable, pero si te intentas pasar te hara dos hoyos en el torzo con su escopeta."
dialogo5="Uno de los residentes que tiene mas tiempo es el viejo denis, el veterano, no vive muy lejos de la posada, pero pasa la mayor parte de sus dias en esta, para tener alguien con quien platicar y de paso mantener el orden ahi, muchos se la pensaran en alterar el orden habiendo un exmilitar que solia pelear cuerpo a cuerpo con su bayoneta durante la guerra civil."
dialogo6="Por ultimo tenemos a nuestro inquilino mas misterioso, no suele hablar mucho, lo que sabemos es que se hacer llamar Enola, es un apache, yo me la pensaria dos veces antes de hacerlo enojar, no quieres que te arranquen la cabellera con un Tomahawk jaja"
print (dialogo1)
time.sleep(5)
print(dialogo2)
time.sleep(5)
print(dialogo3)
time.sleep(5)
print(dialogo4)
time.sleep(5)
print(dialogo5)
time.sleep(5)
print(dialogo6)
time.sleep(5)
print('alguien ha matado a ')
print(muerto)
print (' durante la noche')
time.sleep(5)
print('Tienes 3 oportunidades para encontrar el lugar donde lo mataron')
print('Donde quieres buscar primero? \n 0-El bar \n 1-La sala de juegos \n 2-El pasillo \n 3-La bodega \n 4-El sotano')

for x in range(3):
	searchPlace = int(input('escribe tu eleccion:'))
	if searchPlace == locaciones.index(lugar):
		print ('hay rastros de sangre en el piso, este puede ser el lugar')
		break
	else: print('el lugar esta limpio, y en orden, no hay rastros de sangre o pelea, intenta de nuevo')
print ('okay, ahora vamos a buscar el arma con la que lo mataron, vayamos a checar el baul de armas')
time.sleep(3)
arma=armas[asesIndex]
armas.remove(arma)
print ('paraciera que en el baul estan', armas)
print ('falta una, y a quien pertenecia?')
time.sleep(5)
print('no importa, seguro que ya lo has decifrado, hora de reconstruir la escena del crimen')
print('Quien es el asesino?')
print("0-John el Caza Recompensas" , "\n 1-el sucio Dan" , "\n 2-Loreta, La posadera" , "\n 3-Denis, El veterano" , "\n 4-Enola, El apache")
pickSuspect=int(input())
print('ahora, donde fue el asesinato? ',locaciones)
pickPlace=int(input())
if pickSuspect==asesIndex and pickPlace==lugarIndex:
	print ('felicidades, resolviste el asesinato')
else:
	print('No has dado con el asesino, y este ha escapado despues de la tormenta')
	print('el asesino es ',asesino)
	print('y el lugar es',locaciones[lugarIndex])
time.sleep(15)