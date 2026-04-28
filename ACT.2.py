#TP integrador – Repetitivas- Condicionales y Secuenciales. // Iovaldi Ludmila // Comision 2
#Actividad II: “Acceso al Campus y Menú Seguro”

#Variables correctas
us_correcto = "alumno"
cl_correcta= "python123"

#Solicitud de datos al usuario
for v in range (1,4):
    usuario= input("Ingrese el usuario: " ).strip().lower()
    clave= input("ingrese la clave: ").strip()
    if usuario == us_correcto and clave == cl_correcta:
        print("*ACCESO CONCEDIDO*")
        print("--------------------")

#Menu con diferentes opciones        
        while True:
            print("Escoja una de las siguientes opciones: ")
            print("1)Ver estado de inscripcion") 
            print("2)Cambiar clave") 
            print("3)Mostrar mensaje motivacional") 
            print("4)Salir")
            
            opcion=(input("Opcion:"))

#Validacion de la variable "opcion"             
            if not opcion.isdigit():
                print("¡Error!: ingrese un numero valido")
                continue

#Solicitud de opcion al usuario            
            opcion= int(opcion)
        
            if opcion < 1 or opcion > 4:
                print("¡Error!: opcion fuera de rango")


#Si es == 1            
            if opcion == 1:
                    print("*Inscripto*")
                    print("--------------------")

#Si es == 2             
            elif opcion ==2:
                    clave_nueva= input("ingrese su nueva clave(<= a 6 caracteres.): ")
                    if len (clave_nueva) <6:
                        print("¡Error!: la clave debe tener mas de 6 caracteres")
                        print("--------------------")
                    else:
                        clave_confir= input ("Por favor confirme su nueva clave:")
                    
                        if clave_nueva==clave_confir:
                            print("*Clave cambiada con exito*")
                            print("--------------------")
                        else:
                            print(">>Error de concordancia<<")
                            print("--------------------")

#Si es == 3            
            if opcion ==3:
                print("“No importa cuántas veces te equivoques, lo importante es seguir intentando. El código siempre recompensa la perseverancia.”")
                print("--------------------")

#Si es == 4            
            elif opcion == 4:
                    break
        break

#Si ingresamos los datos de validacion del usuario incorrectos 
    else:
        print(">>usuario y/o clave incorrecto<<")
        print("--------------------")
        
else:
    print(">>CUENTA BLOQUEADA.<<")