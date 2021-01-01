from os import system, name
from sys import exit
from time import sleep
from sys import stdout
from csv import writer


def clear():
    system("cls" if name == "nt" else "clear")


def creds():
    clear()
    print("\n\n")
    print("-------------------------------------------")
    print("BIENVENIDO AL CALZADOR DE NUEVOS RAMOS v1.0")
    print("      made by: Vicente Silva @_vcnt.3      ")
    print("-------------------------------------------")
    print("\n***por ahora solo funciona para teologicos***\n\n\n")
    return


def escribir1(vel, str):
    for letter in str:
        stdout.write(letter)
        stdout.flush()
        sleep(float(vel))


def escribir(vel, str):
    escribir1(vel, str)
    print("")


creds()
sleep(1)
creds()
print("          *                                  ")
sleep(1)
creds()
print("          *           *                      ")
sleep(1)
creds()
print("          *           *           *          ")
sleep(1)
creds()
input("        Presiona ENTER para continuar        ")
clear()
print("¿Has usado el CALZADOR antes? (si/no)")
tuto = input()
clear()
if tuto == "no":
    escribir(0.3, "hmmmmm... un novato")
    sleep(0.4)
    print("perkin")
    sleep(1)
    clear()
    print("¿En que horario tienes catedra?")
    input("> ")
    tuto = 1
    print("ERROR, INTENTA DENUEVO")
    sleep(3)
    escribir(0.1, "te la creiste?")
    yn1 = input("si/no\n")
    if yn1 == "si":
        escribir(0.1, "Puta que eris wn")
    elif yn1 == "no":
        escribir(0.1, "No te creo, wn chanta lsdjfhkg")
    else:
        escribir(0.1, "Uhhh no entendi, sorry no hablo universitario pretencioso")
    sleep(2)
    clear()
    escribir(0.1, "Ya mira tranqui, es tu primera vez asi que te guiare.")
    sleep(0.5)
    escribir(0.1, "Cuando te pida los horarios tienes que poner el dia y modulo")
    escribir(0.5, "JUNTOS.")
    sleep(1)
    escribir(0.1, "Si tuvieras el lunes en el primer modulo seria L1,")
    escribir(0.1, "miercoles en el tercer modulo seria W3 y asi...")
    escribir(0.3, "Por favor recuerda ingresarlos UNO A UNO")
    escribir(0.1, "Vamos denuevo.")
    sleep(3)
    clear()

# -------------------------------------- FEATURE EN DESARROLLO -----------------------------------------------------------
# tipo=input('\n¿Que tipo de ramos quieres calzar?\n> bio=Biologico\n> ttf=Teologico\n> presiona ENTER para ramos personalizados\n')
# if len(tipo)==0:
#    print('---------------------------------------------------------------------------------------------')
#    print('Para priorizar una lista personalizada de ramos recuerda que debe tener el siguiente formato:')
#    print('NRC\tSIGLA\tNOMBRE\tPROFESOR\tHORARIO BUSCACURSOS\n*los espacios son una tabulacion simple*')
#    print('---------------------------------------------------------------------------------------------\n')
#    print('¿Como se llama tu archivo de origen?\n*dejar vacio para volver*')
#    orig=input('> ')
# ------------------------------------------------------------------------------------------------------------------------

# cat=['L1','L2','M1','M3', 'W1','W2','J1','J3']
# lab=['L3','L5','J4']
# ayu=['M4','W3','W5','V1']

cat = []
lab = []
ayu = []

ciclo1 = 0
print("¿En que horario tienes catedra? (formato L1)")
print("Presiona ENTER si no tienes catedra")
sleep(2)
escribir(0.1, "o si no las quieres considerar. Sospechoso...")
fallos = 0
check = 0
procheck = 0
procount = 0
# cat
while ciclo1 == 0:
    entry = input("> ")
    if fallos >= 5 and check == 0:
        escribir(0.1, "Te equivocaste demasiadas veces.")
        escribir(0.2, "CERRANDO PROGRAMA")
        sleep(2)
        escribir(0.1, "jijibromis")
        sleep(1.5)
        escribir(0.1, "Si aun no entiendes cierrame y abreme (7u7) denuevo,")
        escribir(0.1, "asi puedes leer el tutorial otra vez.")
        sleep(1)
        print("Vamos, intenta denuevo")
        check = 1
    elif len(entry) == 0:
        ciclo1 = 1
        print("Registraste todas tus catedras.\n")
    elif len(entry) == 2 and (
        entry[0] in "LMWJVSlmwjvs"
        and entry[1] not in "12345678"
        and entry[1].isnumeric()
    ):
        escribir(
            0.1,
            "¿De verdad tienes clases tan tarde? Me estai mintiendo wn eso no se hace",
        )
        escribir(0.7, ":'(")
        sleep(0.3)
        print("Vamos, intenta denuevo")
    elif len(entry) == 2 and (
        entry[0] not in "LMWJVSlmwjvs" or entry[1] not in "12345678"
    ):
        escribir(0.1, "¿Que estas pasandome? Sosio se equivoco de programa")
        print("Vamos, intenta denuevo")
        fallos += 1
    elif len(entry) != 2:
        escribir(0.1, "Formato incorrecto, bro.")
        sleep(0.3)
        escribir(0.1, "Tampoco es tan dificil,")
        escribir(0.1, "recuerda que el formato es el dia, seguido del modulo")
        escribir(0.5, "JUNTOS.")
        sleep(0.3)
        escribir(
            0.1,
            "Podria ser L1, W4 o V7 (si es que no te respetas, quien cresta toma un ramo un viernes en la tarde???)",
        )
        sleep(0.3)
        print("Vamos, intenta denuevo")
        fallos += 2
    elif entry.upper() in cat:
        escribir(0.1, "Esa ya estaba registrada.")
        escribir(0.1, "Si ya terminaste apreta ENTER nms, con confianza.")
    else:
        cat.append(entry.upper())
        if procheck == 0:
            escribir(0.1, "Wena, la siguiente catedra porfa.")
            escribir(0.1, "Si ya terminaste apreta ENTER nms, con confianza.")
            procount += 1
            if procount >= 2:
                procheck = 1
        elif procheck == 1:
            print("Wena, la siguiente catedra porfa.")
            print("Si ya terminaste apreta ENTER nms, con confianza.")

ciclo2 = 0
print("¿En que horario tienes laboratorio? (formato L1)")
print("Presiona ENTER si no tienes lab")
if fallos - 2 >= 0:
    fallos -= 2
# lab
while ciclo2 == 0:
    entry = input("> ")
    if fallos >= 5 and check == 0:
        escribir(0.1, "Te equivocaste demasiadas veces.")
        escribir(0.2, "CERRANDO PROGRAMA")
        sleep(2)
        escribir(0.1, "jijibromis")
        sleep(1.5)
        escribir(0.1, "Si aun no entiendes cierrame y abreme (7u7) denuevo,")
        escribir(0.1, "asi puedes leer el tutorial otra vez.")
        sleep(1)
        print("Vamos, intenta denuevo")
        check = 1
    elif len(entry) == 0:
        ciclo2 = 1
        print("Registraste todos tus laboratorios.\n")
    elif len(entry) == 2 and (
        entry[0] in "LMWJVSlmwjvs"
        and entry[1] not in "12345678"
        and entry[1].isnumeric()
    ):
        escribir(
            0.1,
            "¿De verdad tienes clases tan tarde? Me estai mintiendo wn eso no se hace",
        )
        escribir(0.7, ":'(")
        sleep(0.3)
        print("Vamos, intenta denuevo")
    elif len(entry) == 2 and (
        entry[0] not in "LMWJVSlmwjvs" or entry[1] not in "12345678"
    ):
        escribir(0.1, "¿Que estas pasandome? Sosio se equivoco de programa")
        print("Vamos, intenta denuevo")
        fallos += 1
    elif len(entry) != 2:
        escribir(0.1, "Formato incorrecto, bro.")
        sleep(0.3)
        escribir(0.1, "Tampoco es tan dificil,")
        escribir(0.1, "recuerda que el formato es el dia, seguido del modulo")
        escribir(0.5, "JUNTOS.")
        sleep(0.3)
        escribir(
            0.1,
            "Podria ser L1, W4 o V7 (si es que no te respetas, quien cresta toma un ramo un viernes en la tarde???)",
        )
        sleep(0.3)
        print("Vamos, intenta denuevo")
        fallos += 2
    elif entry.upper() in lab:
        escribir(0.1, "Ese ya estaba registrado.")
        escribir(0.1, "Si ya terminaste apreta ENTER nms, con confianza.")
    else:
        lab.append(entry.upper())
        if procheck == 0:
            escribir(0.1, "Wena, el siguiente laboratorio porfa.")
            escribir(0.1, "Si ya terminaste apreta ENTER nms, con confianza.")
            procount += 1
            if procount >= 2:
                procheck = 1
        elif procheck == 1:
            print("Wena, el siguiente laboratorio porfa.")
            print("Si ya terminaste apreta ENTER nms, con confianza.")

ciclo3 = 0
print("¿En que horario tienes ayudantia? (formato L1)")
print("Presiona ENTER si no tienes ayudantias")
if fallos - 2 >= 0:
    fallos -= 2
# ayu
while ciclo3 == 0:
    entry = input("> ")
    if fallos >= 5 and check == 0:
        escribir(0.1, "Te equivocaste demasiadas veces.")
        escribir(0.2, "CERRANDO PROGRAMA")
        sleep(2)
        escribir(0.1, "jijibromis")
        sleep(1.5)
        escribir(0.1, "Si aun no entiendes cierrame y abreme (7u7) denuevo,")
        escribir(0.1, "asi puedes leer el tutorial otra vez.")
        sleep(1)
        print("Vamos, intenta denuevo")
        check = 1
    elif len(entry) == 0:
        ciclo3 = 1
        print("Registraste todas tus ayudantias.\n")
    elif len(entry) == 2 and (
        entry[0] in "LMWJVSlmwjvs"
        and entry[1] not in "12345678"
        and entry[1].isnumeric()
    ):
        escribir(
            0.1,
            "¿De verdad tienes clases tan tarde? Me estai mintiendo wn eso no se hace",
        )
        escribir(0.7, ":'(")
        sleep(0.3)
        print("Vamos, intenta denuevo")
    elif len(entry) == 2 and (
        entry[0] not in "LMWJVSlmwjvs" or entry[1] not in "12345678"
    ):
        escribir(0.1, "¿Que estas pasandome? Sosio se equivoco de programa")
        print("Vamos, intenta denuevo")
        fallos += 1
    elif len(entry) != 2:
        escribir(0.1, "Formato incorrecto, bro.")
        sleep(0.3)
        escribir(0.1, "Tampoco es tan dificil,")
        escribir(0.1, "recuerda que el formato es el dia, seguido del modulo")
        escribir(0.5, "JUNTOS.")
        sleep(0.3)
        escribir(
            0.1,
            "Podria ser L1, W4 o V7 (si es que no te respetas, quien cresta toma un ramo un viernes en la tarde???)",
        )
        sleep(0.3)
        print("Vamos, intenta denuevo")
        fallos += 2
    elif entry.upper() in ayu:
        escribir(0.1, "Esa ya estaba registrada.")
        escribir(0.1, "Si ya terminaste apreta ENTER nms, con confianza.")
    else:
        ayu.append(entry.upper())
        if procheck == 0:
            escribir(0.1, "Wena, la siguiente ayudantia porfa.")
            escribir(0.1, "Si ya terminaste apreta ENTER nms, con confianza.")
            procount += 1
            if procount >= 2:
                procheck = 1
        elif procheck == 1:
            print("Wena, la siguiente ayudantia porfa.")
            print("Si ya terminaste apreta ENTER nms, con confianza.")

escribir(0.1, "Revisando los teologicos existentes y ajustando la prioridad.")
sleep(0.5)
clear()
print("Revisando los teologicos existentes y ajustando la prioridad.")


def progress(percent=0, width=30):
    left = width * percent // 100
    right = width - left
    print(
        "\r[",
        "#" * left,
        " " * right,
        "]",
        f" {percent:.0f}%",
        sep="",
        end="",
        flush=True,
    )


for i in range(101):
    progress(i)
    sleep(0.1)
print("")
escribir(0.1, "Exportando archivo...")
sleep(1)


def prioridad(ramo):
    return -ramo[5]


try:
    with open("ramos.txt", "r", encoding="utf-8") as ram:
        ramos = ram.readlines()
except FileNotFoundError:
    exit("No tienes ramos.txt en la misma carpeta. Por favor intenta de nuevo uwu")

for i in range(len(ramos)):
    ramos[i] = ramos[i].strip("\n").split("\t")
    ramos[i][4] = ramos[i][4].split(":")
    if "-" in ramos[i][4][0]:
        ramos[i][4] = [
            f"{ramos[i][4][0][0]}{ramos[i][4][1]}",
            f"{ramos[i][4][0][2]}{ramos[i][4][1]}",
        ]
    elif "," in ramos[i][4][1]:
        ramos[i][4] = [
            f"{ramos[i][4][0]}{ramos[i][4][1][0]}",
            f"{ramos[i][4][0]}{ramos[i][4][1][2]}",
        ]
    ramos[i].append(int(4))
    # print(ramos[i])
    for clase in ramos[i][4]:
        if clase in cat:
            ramos[i][5] = 0
        elif clase in ayu and ramos[i][5] == 4:
            ramos[i][5] = 3
        elif clase in lab and ramos[i][5] == 4:
            ramos[i][5] = 2
        if clase in ayu and ramos[i][5] == 2:
            ramos[i][5] = 1
        elif clase in lab and ramos[i][5] == 3:
            ramos[i][5] = 1
# print(ramos)
ramos.sort(key=prioridad)
# with open("teoFinal.txt","w", encoding='utf-8') as fin:
with open("teoFinal.csv", "w", newline="") as write_obj:
    csv_writer = writer(write_obj)
    csv_writer.writerow(
        ["NRC", "Sigla", "Nombre del ramo", "Profesor", "Horario", "Prioridad"]
    )
    for i in range(len(ramos)):
        ramos[i][4] = ",".join(ramos[i][4])
        ramos[i][5] = str(ramos[i][5])
        csv_writer.writerow(ramos[i])
    csv_writer.writerow([""])
    csv_writer.writerow(["Prioridad", "Significado"])
    csv_writer.writerow(["4", "No topa con nada"])
    csv_writer.writerow(["3", "Topa con ayudantia"])
    csv_writer.writerow(["2", "Topa con laboratorio"])
    csv_writer.writerow(["1", "Topa con ayudantia y con laboratorio"])
    csv_writer.writerow(["0", "Topa con catedra (y no lo puedes tomar)"])
escribir(
    0.1, 'Archivo "TeologicoFinalEstesiiiiiiiHD4K real siquesi FINAL.csv" exportado.'
)
escribir(0.1, "Gracias por preferirme :)")
sleep(3)
clear()
