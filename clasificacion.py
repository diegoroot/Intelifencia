import csv
#Diego Alejandro Cifuentes Buitrago
#1 mammal 41 huesos y pelo
#2 bird 20 plumas huesos
#3 reptile 5 respira nopelo nopluma noacuatico vertebrados
#4 fish 13 norespira nopelo nopluma acuatico invertebrado
#5 amphibian 4 nohuevos norespira nopelo nopluma acuatico invertebrado
#6 bug 8 noacuatico nopluma invertebrado respira noleche nopredadores masde0patas
#7 Invertebrate 10 norespira nopelo nopluma acuatico invertebrado
#Para categorizar el objeto animal del mundo real usaré proposiciones
#por ejemplo tiene_pelo(x) and es_vertebrado(x) -> es_mammal
#vamos a clasificar animales para que un agente externo pueda usar este dataset y no tenga que realizar todo el proceso
#por ejemplo el proceso ontologico, establecer medias, hacer lógica descriptiva para categorizar
def entorno():
    print('ingrese los siguientes datos para un animal y te diremos qué clase de animal');
nombre = input('ingrese el nombre: ')
plumas = int(input('tiene plumas: '))
pelo = int(input('tiene pelo: '))
invertebrado = int(input('es invertebrado: '))
respira = int(input('respira por pulmones: '))
acuatico = int(input('es acuatico: '))
pata = int(input('tiene más de una pata: '))
reg = int(input('Desea registar el animal: '))
def logica_des():
    if respira == 1 and invertebrado == 0 and plumas == 0:
        return "it's mammal"

    if plumas == 1:
        return "it's bird"
    if respira == 1 and pelo == 0 and plumas == 0 and acuatico == 0 and invertebrado ==0:
        return "it's reptile"
    if respira == 0 and pelo == 0 and plumas == 0 and acuatico == 1 and invertebrado ==0:
        return "it's fish"
    if acuatico == 0 and plumas == 0 and invertebrado == 1 and respira == 1 and pata>0:
        return "it's bug"
    if invertebrado == 1:
        return "it's Invertebrate"
cat = logica_des()
print()
print(cat)
print()
if reg ==1 :
    huevos = int(input('pone huevos: '))
    leche = int(input('produce leche: '))
    aereo = int(input('vuela: '))
    predator = int(input('es predador: '))
    toothed = int(input('es dentado: '))
    venomous = int(input('es venenoso: '))
    fins = int(input('tiene aletas: '))
    ta =  int(input('tiene cola: '))
    dom = int(input('es domestico: '))
    with open('/home/diego/Descargas/zoo-animal-classification/zoo.csv', newline='') as File:
        reader = csv.reader(File)
        for row in reader:
            if nombre == row[0]:
                print('ya está en el dataset: ', row)
            else:
                anima = [nombre,pelo,plumas,huevos,leche,aereo,acuatico,predator, toothed, invertebrado,respira,venomous, fins, pata, ta, dom, cat ]
                writer = csv.writer(File)
                writer.writerows(anima)
                pass
else:
    print('Gracias')
