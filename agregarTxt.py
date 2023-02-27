class txt:
    
    
    
    def addPalabras(ingles, espanol):
        parIngles=ingles.lower()
        parEspanol=espanol.lower()
        file=open('diccionario.txt', 'a')
        file.write('\n'+parIngles)
        file.write(' ')
        file.write(parEspanol)
        file.write('\n')
        file.close()
    
    def buscar(parametro, idioma):
        par=parametro.lower()
        with open('diccionario.txt', 'r') as f:
            lineas = f.readlines()
            for linea in lineas:
                if par in linea:
                   arreglo = linea.split()
                   print(arreglo)
                  # for x in arreglo:
                   print(idioma)
                   print(arreglo[0])
                   print(arreglo[1])
                   if int(idioma)==1 and arreglo[0]==par:
                            return arreglo[1]
                   elif int(idioma)==2 and arreglo[1]==par:
                            return arreglo[0]
        return "No existe coincidencia"
                       
  