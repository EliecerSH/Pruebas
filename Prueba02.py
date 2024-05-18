
nom=input(" ingrese el nombre del trabajador ")
while not nom or len(nom) > 30:
   print(" El nombre de contener de 1 a 30 caracteres ")
   nom=input(" ingrese el nombre del trabajador ")

sb=float(input(" ingrese el sueldo base "))
while not sb or sb < 0:
   try:
    sb=float(input(" ingrese el sueldo base (solo se aceptan valores mayores a 0)"))
   except ValueError:
      print(" solo se aceptan caracteres numericos mayores a 0 ")

hx=float(input(" Ingresa las horas extras trabajadas "))
while not hx or hx <0:
    try:
     hx=float(input(" Ingresa las horas extras trabajadas (solo se aceptan valor mayores a 0)"))
    except ValueError:
      print(" solo se aceptan valores numericos de >-1")

SueldoPorHora =(sb/180)
TotalDeHorasExtra=(SueldoPorHora*1.5)*hx
SueldoBruto=(sb+TotalDeHorasExtra)
SueldoLiquido=(SueldoBruto)*0.83
Fanasa=SueldoBruto*0.07
Afp=SueldoBruto*0.10

election=0

while election != 2:
          print(f"""-------liquidacion--------
      
          NOMBRE: {nom}
          SUELDO BRUTO: ${SueldoBruto:.1f}
          HHORAS EXTRAS {hx:.0f} : ${TotalDeHorasExtra:.1f}
          DESCUENTO DE FONASA: ${Fanasa:.1f}
          DECUENTO DE AFP: ${Afp:.1f}
          SUELDO LIQUIDO : ${SueldoLiquido:.1f}
      
          1) Guardar liquidación
          2) terminar proceso
          """)
          try:
              election=int(input())
          except ValueError:
              print("sono se aceptan los numeros en las opciones ")
          if election==1:
           archivo= open(f'liquidacion_{nom}_trabajador.txt','w')
           archivo.write(F"""-----LIQUIDACION-----           
                  NOMBRE: {nom}
                  SUELDO BRUTO: ${SueldoBruto:.1f}
                  HHORAS EXTRAS {hx:.1f}: ${TotalDeHorasExtra:.1f}
                  DESCUENTO DE FONASA: ${Fanasa:.1f}
                  DECUENTO DE AFP: ${Afp:.1f}
                  SUELDO LIQUIDO : ${SueldoLiquido:.1f}
                  """)
           archivo.close
           print(" termino del proceso ")
          elif election==2:
           print(" termino del proceso ")