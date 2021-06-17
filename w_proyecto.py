#!/usr/bin/env python
'''
Práctico Integrador de Python Inicial
---------------------------
Autor: Ludueña Marcos
Version: 1.0

Descripcion:
Programa creado para registrar las transacciones de una pyme de productos de artesania
'''

__author__ = "Ludueña Marcos"
__email__ = "marcosluduea89@gmail.com"
__version__ = "1.0"

import csv
import re
import datetime
import numpy as np


def datos_personales():
    nombre = str(input('Ingrese su nombre:\n' ))
    apellido =str(input('Ingrese su apellido:\n' ))
    dni = int(input('Ingrese su dni:\n' ))
    telefono = int(input('Ingrese el numero telefónico:\n'))

    return nombre, apellido , dni, telefono

def compra():
    cantidad= int(input('ingrese la cantidad de productos que desea comprar: '))
    precio = int(input('ingrese el monto por cada producto: '))
    precio_total = (cantidad*precio)
    
    return cantidad,precio,precio_total



def framework():
    
    #header = ['NOMBRE_CLIENTE','APELLIDO_CLIENTE','DNI_CLIENTE','TELEFONO']
    #csvfile = open('cliente.csv', 'w', newline='')
    #writer = csv.DictWriter(csvfile, fieldnames=header)
    #writer.writeheader()
    #csvfile.close()
    while True: 
       
        print('''
            1- Venta
            2- Consulta
            3- Cerrar programa
            ''') 
            

        opcion = int(input('ingrese la operación deseada:\n'))
        if opcion == 1:
            opcion_cliente = int(input('¿Es un cliente nuestro?: 1:SI, 2:NO \n'))
            atras_true = False
            while True:
                if atras_true == True:
                    break
                else:
                    False
                if opcion_cliente == 1:                                 
                    csvfile = open ('cliente.csv')
                    data = list(csv.DictReader(csvfile))
                    DNI = int(input('ingrese el DNI:'))
                    Verificacion = []
                    nombre = []
                    for i in range(len(data)):
                        clientes = data[i]
                        for k,v in clientes.items():
                            if k =='DNI_CLIENTE':
                                    Verificacion.append(int(v))
                            if k =='NOMBRE_CLIENTE':
                                    nombre.append(str(v))

                    #INGRESAMOS A UN NUEVO CSV CON LA INFORMACION SOLO DE LAS OPERACIONES
                    if DNI in Verificacion:
                        precio_final = []
                        print('')
                        print (f'¡Verificación correcta!, ¿Que producto desea comprar?: \n ')
                        while True:
                            

                                                    
                            with open('operaciones.csv', "a", newline='') as f:
                                        
                                header = ['CANASTO_ROPA','CANASTO_MATERO','BANDEJAS_EXHIBIDORAS','BANDEJAS_PINTADAS', 'ANILLOS',
                                            'PANERITAS_BASE_MIMBRE','PANERITAS_BASE_MADERA','PRECIO*UNIDAD','FECHA','PRECIO_TOTAL']
                                writer = csv.DictWriter(f, fieldnames=header)
                                    #writer.writeheader()
                                        

                                tipo=['CANASTO_ROPA', 'CANASTO_MATERO', 'BANDEJAS_EXHIBIDORAS','BANDEJAS_PINTADAS', 'ANILLOS',
                                            'PANERITAS_BASE_MIMBRE','PANERITAS_BASE_MADERA','ATRAS']
                                
                                for i in tipo:
                                    index = tipo.index(i)
                                    print((index + 1),'**',i)
                                opereacion = int(input('Ingrese un numero...: '))

                                    


                                    
                                if opereacion == 1:
                                    while True:
                                        
                                        cantidad,precio,precio_total = compra ()
                                        algo_mas = int(input('¿Necesita algo mas? 1:SI, 2:NO \n '))

                                        if algo_mas == 1:
                                            precio_final.append(int(precio_total))
                                                
                                            writer.writerow({'CANASTO_ROPA':cantidad,'CANASTO_MATERO':'*','BANDEJAS_EXHIBIDORAS':'*','BANDEJAS_PINTADAS':'*', 'ANILLOS':'*',
                                                    'PANERITAS_BASE_MIMBRE':'*','PANERITAS_BASE_MADERA':'*','PRECIO*UNIDAD':precio,'FECHA': datetime.date.today() ,'PRECIO_TOTAL': precio_total})
                                                
                                            break


                                                    
                                        else:
                                            writer.writerow({'CANASTO_ROPA':cantidad,'CANASTO_MATERO':'*','BANDEJAS_EXHIBIDORAS':'*','BANDEJAS_PINTADAS':'*', 'ANILLOS':'*',
                                                    'PANERITAS_BASE_MIMBRE':'*','PANERITAS_BASE_MADERA':'*','PRECIO*UNIDAD':precio,'FECHA': datetime.date.today() ,'PRECIO_TOTAL': precio_total})
                                            precio_final.append(int(precio_total))

                                            print(f'El precio total es: ${sum(precio_final)} \n')
                                            print('Gracias...¡¡Vuelvan pronto!!')
                                            break
                                            
                                    

                                            
                                if opereacion == 2:
                                    while True:

                                        cantidad,precio,precio_total = compra ()
                                        algo_mas = int(input('¿Necesita algo mas? 1:SI, 2:NO \n '))
                                                
                                        if algo_mas == 1:
                                            precio_final.append(int(precio_total))
                                            writer.writerow({'CANASTO_ROPA':'*','CANASTO_MATERO':cantidad,'BANDEJAS_EXHIBIDORAS':'*','BANDEJAS_PINTADAS':'*', 'ANILLOS':'*',
                                                    'PANERITAS_BASE_MIMBRE':'*','PANERITAS_BASE_MADERA':'*','PRECIO*UNIDAD':precio,'FECHA': datetime.date.today() ,'PRECIO_TOTAL': precio_total})
                                            break
                                                    
                                        else:
                                            writer.writerow({'CANASTO_ROPA':'*','CANASTO_MATERO':cantidad,'BANDEJAS_EXHIBIDORAS':'*','BANDEJAS_PINTADAS':'*', 'ANILLOS':'*',
                                                    'PANERITAS_BASE_MIMBRE':'*','PANERITAS_BASE_MADERA':'*','PRECIO*UNIDAD':precio,'FECHA': datetime.date.today() ,'PRECIO_TOTAL': precio_total})
                                                    
                                            
                                            precio_final.append(int(precio_total))

                                            print(f'El precio total es: ${sum(precio_final)} \n')
                                            print('Gracias...¡¡Vuelvan pronto!!')
                                            break    
                                if opereacion == 3:
                                    while True:

                                        cantidad,precio,precio_total = compra ()
                                        algo_mas = int(input('¿Necesita algo mas? 1:SI, 2:NO \n '))
                                            
                                        if algo_mas == 1:
                                            precio_final.append(int(precio_total))
                                            writer.writerow({'CANASTO_ROPA':'*','CANASTO_MATERO':'*','BANDEJAS_EXHIBIDORAS':cantidad,'BANDEJAS_PINTADAS':'*', 'ANILLOS':'*',
                                                        'PANERITAS_BASE_MIMBRE':'*','PANERITAS_BASE_MADERA':'*','PRECIO*UNIDAD':precio,'FECHA': datetime.date.today() ,'PRECIO_TOTAL': precio_total})
                                            break
                                                    
                                        else:
                                            writer.writerow({'CANASTO_ROPA':'*','CANASTO_MATERO':'*','BANDEJAS_EXHIBIDORAS':cantidad,'BANDEJAS_PINTADAS':'*', 'ANILLOS':'*',
                                                    'PANERITAS_BASE_MIMBRE':'*','PANERITAS_BASE_MADERA':'*','PRECIO*UNIDAD':precio,'FECHA': datetime.date.today() ,'PRECIO_TOTAL': precio_total})
                                                    
                                            
                                                    
                                                    
                                            print(f'El precio total es: ${sum(precio_final)} \n')
                                            print('Gracias...¡¡Vuelvan pronto!!')
                                            break

                                if opereacion == 4:
                                    while True:

                                        cantidad,precio,precio_total = compra ()   
                                        algo_mas = int(input('¿Necesita algo mas? 1:SI, 2:NO \n '))
                    
                                        if algo_mas == 1:
                                            precio_final.append(int(precio_total))
                                            writer.writerow({'CANASTO_ROPA':'*','CANASTO_MATERO':'*','BANDEJAS_EXHIBIDORAS':'*','BANDEJAS_PINTADAS':cantidad, 'ANILLOS':'*',
                                                        'PANERITAS_BASE_MIMBRE':'*','PANERITAS_BASE_MADERA':'*','PRECIO*UNIDAD':precio,'FECHA': datetime.date.today() ,'PRECIO_TOTAL': precio_total})
                                            break
                                        else:
                                            writer.writerow({'CANASTO_ROPA':'*','CANASTO_MATERO':'*','BANDEJAS_EXHIBIDORAS':'*','BANDEJAS_PINTADAS':cantidad, 'ANILLOS':'*',
                                                    'PANERITAS_BASE_MIMBRE':'*','PANERITAS_BASE_MADERA':'*','PRECIO*UNIDAD':precio,'FECHA': datetime.date.today() ,'PRECIO_TOTAL': precio_total})
                                                    
                                            
                                                    
                                                    
                                            print(f'El precio total es: ${sum(precio_final)} \n')
                                            print('Gracias...¡¡Vuelvan pronto!!')
                                            break
                                if opereacion == 5:
                                    while True:

                                        cantidad,precio,precio_total = compra ()
                                        algo_mas = int(input('¿Necesita algo mas? 1:SI, 2:NO \n '))

                                        if algo_mas == 1:
                                            precio_final.append(int(precio_total))
                                            writer.writerow({'CANASTO_ROPA':'*','CANASTO_MATERO':'*','BANDEJAS_EXHIBIDORAS':'*','BANDEJAS_PINTADAS':'*', 'ANILLOS':cantidad,
                                                        'PANERITAS_BASE_MIMBRE':'*','PANERITAS_BASE_MADERA':'*','PRECIO*UNIDAD':precio,'FECHA': datetime.date.today() ,'PRECIO_TOTAL': precio_total})
                                            break
                                        else:
                                            writer.writerow({'CANASTO_ROPA':'*','CANASTO_MATERO':'*','BANDEJAS_EXHIBIDORAS':'*','BANDEJAS_PINTADAS':'*', 'ANILLOS':cantidad,
                                                    'PANERITAS_BASE_MIMBRE':'*','PANERITAS_BASE_MADERA':'*','PRECIO*UNIDAD':precio,'FECHA': datetime.date.today() ,'PRECIO_TOTAL': precio_total})
                                                    
                                            
                                                    
                                                    
                                            print(f'El precio total es: ${sum(precio_final)} \n')
                                            print('Gracias...¡¡Vuelvan pronto!!')
                                            break
                                if opereacion == 6:
                                    while True:

                                        cantidad,precio,precio_total = compra ()
                                        algo_mas = int(input('¿Necesita algo mas? 1:SI, 2:NO \n '))
                                            
                                        if algo_mas == 1:
                                            precio_final.append(int(precio_total))
                                            writer.writerow({'CANASTO_ROPA':'*','CANASTO_MATERO':'*','BANDEJAS_EXHIBIDORAS':'*','BANDEJAS_PINTADAS':'*', 'ANILLOS':'*',
                                                    'PANERITAS_BASE_MIMBRE':cantidad,'PANERITAS_BASE_MADERA':'*','PRECIO*UNIDAD':precio,'FECHA': datetime.date.today() ,'PRECIO_TOTAL': precio_total})
                                            break
                                        else:
                                            writer.writerow({'CANASTO_ROPA':'*','CANASTO_MATERO':'*','BANDEJAS_EXHIBIDORAS':'*','BANDEJAS_PINTADAS':'*', 'ANILLOS':'*',
                                                    'PANERITAS_BASE_MIMBRE':cantidad,'PANERITAS_BASE_MADERA':'*','PRECIO*UNIDAD':precio,'FECHA': datetime.date.today() ,'PRECIO_TOTAL': precio_total})
                                                
                                        
                                                
                                                
                                            print(f'El precio total es: ${sum(precio_final)} \n')
                                            print('Gracias...¡¡Vuelvan pronto!!')
                                            break
                                if opereacion == 7:
                                    while True:

                                        cantidad,precio,precio_total = compra ()   
                                        algo_mas = int(input('¿Necesita algo mas? 1:SI, 2:NO \n '))
                                        if algo_mas == 1:
                                            precio_final.append(int(precio_total))
                                            writer.writerow({'CANASTO_ROPA':'*','CANASTO_MATERO':'*','BANDEJAS_EXHIBIDORAS':'*','BANDEJAS_PINTADAS':'*', 'ANILLOS':'*',
                                                        'PANERITAS_BASE_MIMBRE':'*','PANERITAS_BASE_MADERA':cantidad,'PRECIO*UNIDAD':precio,'FECHA': datetime.date.today() ,'PRECIO_TOTAL': precio_total})
                                            break
                                        else:
                                            writer.writerow({'CANASTO_ROPA':'*','CANASTO_MATERO':'*','BANDEJAS_EXHIBIDORAS':'*','BANDEJAS_PINTADAS':'*', 'ANILLOS':'*',
                                                    'PANERITAS_BASE_MIMBRE':'*','PANERITAS_BASE_MADERA':cantidad,'PRECIO*UNIDAD':precio,'FECHA': datetime.date.today() ,'PRECIO_TOTAL': precio_total})
                                                    
                                            
                                                    
                                                    
                                            print(f'El precio total es: ${sum(precio_final)} \n')
                                            print('Gracias...¡¡Vuelvan pronto!!')
                                            break
                                if opereacion == 8:
                                    atras_true= True
                                    break                            
                                    


                    
                    else:
                        print('No se encuentra en nuestra base de datos,Ingrese con la opcion "1-2" para registrar nuevo cliente ')
                        break
                                
                            

                                
                if opcion_cliente == 2:
                    header = ['NOMBRE_CLIENTE','APELLIDO_CLIENTE','DNI_CLIENTE','TELEFONO']
                    csvfile = open('cliente.csv','a')
                    writer = csv.DictWriter(csvfile, fieldnames=header)
                    nombre,apellido,DNI,telefono = datos_personales ()
                    writer.writerow({'APELLIDO_CLIENTE': apellido, 'NOMBRE_CLIENTE': nombre, 'DNI_CLIENTE': DNI, 'TELEFONO':telefono})
                    csvfile.close()
                    print('¡Ahora sí!, :\n')
                    break

                        
                        
                        
                    

            
                
                    

                            
                           
                        

                            
                            
        if opcion ==2:
            break
        if opcion ==3:
            break

                    
                        



                        
                    



                    

                    

        
if __name__ == '__main__':
    print('')
    print('******************************\n')
    print("Bienvenidos al software FENIX 1.0 \n")
    print('******************************')
    framework()
