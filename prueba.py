op=0
opu=0
opd=0
opt=0
clientes=[]
while op!= 4:
    print("------------- Opciones ---------------")
    print("1 -> Registrara cliente")
    print("2 -> Consultar cliente")
    print("3 -> Registrar pedido")
    print("4 -> Salir")
    print("--------------------------------------")
    try:
        op=int(input("Ingrese opcion: "))
        print("\n")
    
        if op ==1:
            print("----------------- Registrara cliente -----------------")
            #Crea lista cliente
            cliente=[]
            #Datos apedir
            rut=int(input("(+)Ingrese rut: "))
            if rut< 5000000 or rut>99999999:
                print("INVALIDO")
                break

            nombre=(input("(+)Ingrese nombre: "))
            direc=input("(+)Ingrese direccion: ")
            comuna=input("(+)Ingrese Comuna: ")
            correo=input("(+)Ingrese correo: ")
            if "@" not in correo:
                print("INVALIDO")
                break

            edad=int(input("(+)Ingrese edad: "))
            if edad<18:
                print("INVALIDO")
                break

            celular=int(input("(+)Ingrese celular: "))
            if celular > 999999999  or celular< 99999999:
                print("INVALIDO")
                break

            #ingresar datos en lists cliente
            cliente.append(rut)
            cliente.append(nombre)
            cliente.append(direc)
            cliente.append(comuna)
            cliente.append(correo)
            cliente.append(edad)
            cliente.append(celular)

            #Ingresar lista cliente a lista clientes
            clientes.append(cliente)
            print("\n")
            print("---------------------------------------")
            print("(+) CLIENTE INGRESADO CORRECTAMENTE (+)")
            print("---------------------------------------")
            print("\n")

        elif op ==2:

            con_rut=int(input("Ingrese rut a consultar: "))

            for cliente in clientes:
                if cliente[0]==con_rut:
                    print("---------- Informacion de cliente ----------")
                    print("Rut:",cliente[0])
                    print("Nombre:",cliente[1])
                    print("Direccion:",cliente[2])
                    print("Comuna:",cliente[3])
                    print("Correo:",cliente[4])
                    print("Edad:",cliente[5])
                    print("Celular:",cliente[6])
        elif op ==3:
            ops=0
            total=0
            print("|               Registrar pedido                 |")
            print("|------------------------------------------------|")
            print("|     1     |       2      |          3          |")
            print("|-----------|--------------|---------------------|")
            print("|California | Crab ahumado | Tempura Tuna Nikkei |")
            print("|-----------|--------------|---------------------|")
            print("|  $5.100   |    $6.200    |        $5.800       |")
            print("|------------------------------------------------|")
            print("|      Precione 4 si decea terminar el pedido    |")
            print("\n")
            
            while ops!= 4:
                
                ops=int(input("Ingrese opcion: "))
                if ops == 1:
                    total=total+5100
                    opu=opu+1
                elif ops == 2:
                    total = total+6200
                    opd=opd+1
                elif ops == 3:
                    total=total+5800
                    opt=opt+1
            print("\n")
            print("------------- Boleta---------------")
            print(f"California:             |    {opu}")
            print(f"Crab ahumado:           |    {opd}")
            print(f"Tempura Tuna Nikkei:    |    {opt}")
            print("-----------------------------------")
            print(f"Total:                    ${total}")
            print("-----------------------------------")
            print("\n")
            print("¿Con cuanto dinero cancelara la compra?")
            paga=int(input("--> "))
            if paga<total:
                print("El dinero es insuficiente")
                break
            elif paga==total:
                print("A pagadao con el monto justo, que lo disfrute")
                break
            elif paga>total:
                vuelto=paga-total
                print("Su vuelto es de:",vuelto)
            
        elif op==4:
            print("Gracias por preferir Sushi - Nikkey")
    except ValueError:
        print("Mal digitao")


        

