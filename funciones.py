import os
import json
def read_json():
    with open ('datos.json','r') as archivo:
        datos=json.load(archivo)
    return datos
def terminar():
    terminar1=None
    while terminar1==None or terminar1!='no' or terminar1!='si':
        print('Desea TERMINAR')
        terminar1=input('\t')
        terminar1=terminar1.lower()
    return terminar1
def terminar2():
    os.system('cls')
    terminar1=None
    while terminar1==None and terminar1!='no' and terminar1!='si':
        print('Esta seguro de que quiere reiniciar la informacion')
        terminar1=input('\t')
        terminar1=terminar1.lower()
    return terminar1
def write_json(datos):
    with open('datos.json','w') as archivo:
        json.dump(datos,archivo)
def mini_menu():
    opc=None
    while opc==None or opc<0 or opc>5:
        try:
            print("\t0.Salir\n\t1.Añadir notas\n\t2.Autoevaluación\n\t3.Final\n\t4.Ver notas\n\t5.Eliminar notas del 85%")
            opc=int(input())
        except:
            os.system('cls')
    return opc
def añadir_notas(materia,datos):
    materia=datos.get(materia)
    os.system('cls')
    notas=materia.get('notas')
    nota=int(input('Nota: '))
    notas.append(nota)
    return datos
def añadir_auto(materia,datos):
    materia=datos.get(materia)
    os.system('cls')
    nota=int(input('Autoevaluación: '))
    materia['auto']=nota
    return datos
def añadir_final(materia,datos):
    materia=datos.get(materia)
    os.system('cls')
    nota=int(input('Final: '))
    materia['final']=nota
    return datos
def eliminar_notas(materia,datos):
    materia=datos.get(materia)
    os.system('cls')
    notas=materia.get('notas')
    if len(notas)>0:
        print('Eliminar notas\n\n\tEscriba la nota que desea eliminar -->',end=' ')
        nota_eliminar=int(input())
        notas.remove(nota_eliminar)
    else:
        print('Eliminar notas\n\n\tNo hay notas para eliminar\n')
        os.system('pause')
    return datos
def ver_notas(materia,datos):
    materia=datos.get(materia)
    notas=materia.get('notas')
    auto=materia.get('auto')
    final=materia.get('final')
    contador=0
    if len(notas)>0:
        print('85%')
        suma=0
        for h in notas:
            contador+=1
            print(f'\tNota {contador} : {h}')
            suma+=h
        promedio=suma/contador
        print(f'\tEl promedio del 85% es: {promedio}')
        promedio=promedio*0.85
        print(f'\tLa nota del 85% es: {promedio}')
        if auto!=0:
            print('05%')
            print(f'\tLa autoevaluacion es: {auto}')
            auto=auto*0.05
            print(f'\tLa nota del 05% es: {auto}')
        if final!=0:
            print('10%')
            print(f'\tLa final es: {final}')
            final=final*0.1
            print(f'\tLa nota del 10% es: {final}')
        if len(notas)>0 and auto!=0 and final==0:
            sumatoria=promedio+auto
            print(f'\nLa nota del 90% es de: {sumatoria}')
        if len(notas)>0 and auto!=0 and final!=0:
            sumatoria=promedio+auto+final
            print(f'\nLa nota definitiva es de: {sumatoria}')
    os.system('pause')
def menu(datos):
    rojo="\033[31m"
    verde="\033[32m"
    normal="\033[39m"
    amarillo = '\033[33m'
    azul='\033[36m'
    contador=0
    print('0.Salir')
    for materia in datos:
        contador+=1
        promedio=0
        suma=0
        materia1=datos.get(materia)
        notas=materia1.get('notas')
        auto=materia1.get("auto")
        final=materia1.get('final')
        if len(notas)>0:
            suma=0
            contador1=0
            for h in notas:
                contador1+=1
                suma+=h
            promedio=suma/contador1
            if  auto!=0 and final==0:
                sumatoria=(promedio*0.85)+(auto*0.05)+0.1
            elif auto!=0 and final!=0:
                sumatoria=(promedio*0.85)+(auto*0.05)+(final*0.1)
            else:
                sumatoria=promedio
            if sumatoria>=48:
                print(verde+f"\t{contador}. {materia}")
                materia1['color']="verde"
            if sumatoria<48 and sumatoria>=41:
                print(azul+f"\t{contador}. {materia}")
                materia1['color']="azul"
            if sumatoria<41 and sumatoria>=35:
                print(amarillo+f"\t{contador}. {materia}")
                materia1['color']="amarillo"
            if sumatoria<35:
                print(rojo+f"\t{contador}. {materia}")
                materia1['color']="rojo"
        else:
            print(normal+f"\t{contador}. {materia}")
            materia1['color']="normal"
def ultima_opcion(datos):
    print('  Blanco--85%  //  Azul--05%  //  Verde--10%')
    verde="\033[32m"
    normal="\033[39m"
    azul='\033[36m'
    contador=0
    for materia in datos:
        contador+=1
        area=datos.get(materia)
        notas=area.get('notas')
        auto=area.get('auto')
        final=area.get('final')
        print(normal+f'{contador}. {materia} ')
        if len(notas)>0:
            print(notas,end='--//--')
            print(azul,auto,end=' --//--')
            print(verde,final)
            print(normal)
        else:
            print('S.F.\n')
    os.system('pause')
def opc(materia, opcion, datos):
    if opcion==1:
        datos=añadir_notas(materia,datos)
    if opcion==2:
        datos=añadir_auto(materia,datos)
    if opcion==3:
        datos=añadir_final(materia,datos)
    if opcion==4:
        os.system('cls')
        ver_notas(materia,datos)
        os.system('cls')
    if opcion==5:
        datos=eliminar_notas(materia,datos)
    os.system('pause')