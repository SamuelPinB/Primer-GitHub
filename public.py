import os
import funciones

os.system('cls')
datos=funciones.read_json()
opc=None
RESET="\033[39m"
while(opc==None or opc!=0):
    opc=None
    while(opc==None or opc<0 or opc>18):
        try:
            funciones.menu(datos)
            print(RESET+'\t17. Ver Notas')
            opc=int(input('Opción--> '))
        except:
            os.system('cls')
    if opc==1:
        os.system('cls')
        print('Matemáticas')
        opcion=funciones.mini_menu()
        funciones.opc("Matematicas",opcion,datos)
    if opc==2:
        os.system('cls')
        print('Lengua Castellana')
        opcion=funciones.mini_menu()
        funciones.opc("Lengua castellana",opcion,datos)
        os.system('pause')
    if opc==3:
        os.system('cls')
        print('Inglés')
        opcion=funciones.mini_menu()
        funciones.opc("Ingles",opcion,datos)
    if opc==4:
        os.system('cls')
        print('Economía')
        opcion=funciones.mini_menu()
        funciones.opc("Economia",opcion,datos)
    if opc==5:
        os.system('cls')
        print('Ciencias Sociales')
        opcion=funciones.mini_menu()
        funciones.opc("Sociales",opcion,datos)
    if opc==6:
        os.system('cls')
        print('Química')
        opcion=funciones.mini_menu()
        funciones.opc("Quimica",opcion,datos)
    if opc==7:
        os.system('cls')
        print('Física')
        opcion=funciones.mini_menu()
        funciones.opc("Fisica",opcion,datos)
    if opc==8:
        os.system('cls')
        print('Biología')
        opcion=funciones.mini_menu()
        funciones.opc("Biologia",opcion,datos)
    if opc==9:
        os.system('cls')
        print('Ética')
        opcion=funciones.mini_menu()
        funciones.opc("Etica",opcion,datos)
    if opc==10:
        os.system('cls')
        print('Filosofía')
        opcion=funciones.mini_menu()
        funciones.opc("Filosofia",opcion,datos)
    if opc==11:
        os.system('cls')
        print('Religión')
        opcion=funciones.mini_menu()
        funciones.opc("Religion",opcion,datos)
    if opc==12:
        os.system('cls')
        print('Agustinología')
        opcion=funciones.mini_menu()
        funciones.opc("Agustinologia",opcion,datos)
    if opc==13:
        os.system('cls')
        print('Tecnología')
        opcion=funciones.mini_menu()
        funciones.opc("Tecnologia",opcion,datos)
    if opc==14:
        os.system('cls')
        print('Artes')
        opcion=funciones.mini_menu()
        funciones.opc("Artes",opcion,datos)
    if opc==15:
        os.system('cls')
        print('Música')
        opcion=funciones.mini_menu()
        funciones.opc("Musica",opcion,datos)
    if opc==16:
        os.system('cls')
        print('Educación Física')
        opcion=funciones.mini_menu()
        funciones.opc("Educacion Fisica",opcion,datos)
    if opc==17:
        os.system('cls')
        funciones.ultima_opcion(datos)
        os.system('cls')
    if opc==18:
        print('Reiniciar')
        reiniciar=funciones.terminar2()
        if reiniciar=='si':
            datos={"Matematicas": {"notas": [], "auto": 0, "final": 0}, "Lengua castellana": {"notas": [], "auto": 0, "final": 0}, "Ingles": {"notas": [], "auto": 0, "final": 0}, "Economia": {"notas": [], "auto": 0, "final": 0}, "Sociales": {"notas": [], "auto": 0, "final": 0}, "Quimica": {"notas": [], "auto": 0, "final": 0}, "Fisica": {"notas": [], "auto": 0, "final": 0}, "Biologia": {"notas": [], "auto": 0, "final": 0}, "Etica": {"notas": [], "auto": 0, "final": 0}, "Filosofia": {"notas": [], "auto": 0, "final": 0}, "Religion": {"notas": [], "auto": 0, "final": 0}, "Agustinologia": {"notas": [], "auto": 0, "final": 0}, "Tecnologia": {"notas": [], "auto": 0, "final": 0}, "Artes": {"notas": [], "auto": 0, "final": 0}, "Musica": {"notas": [], "auto": 0, "final": 0}, "Educacion Fisica": {"notas": [], "auto": 0, "final": 0}}
            print('Reinicio exitoso')
            os.system('pause')
            os.system('cls')
            opc=0
        if reiniciar=='no':
            os.system('cls')
funciones.write_json(datos)
os.system('pause')
os.system('cls')