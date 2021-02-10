def leerArchivo (ruta_archivo):
    archivo= open(ruta_archivo,"r")
    linea=archivo.readline()
    texto = []

    while (len(linea)!=0):
          open = 0
          close = 0
          texto = ""
          while (open != close) and (len(linea)!=0):
              open += linea.count("(")
              close += linea.count(")")
              linea=archivo.readline()
          texto.append(linea.replace('\n',''))
          linea=archivo.readline()
    
    archivo.close         
    print(texto)
    return texto

def analizarArchivo(ruta_archivo):
    texto = leerArchivo (ruta_archivo)
    linea  = 0
    correcto = True
    variables = []
    functions = []

    if texto[linea][0] != "(":
        correcto = False

    while correcto and (linea<len(texto)):
        instruccion = texto[linea][:texto[linea].find("(")]
        if instruccion.contains("define"):
            pass
        elif instruccion.contains("block"):
            pass
        elif instruccion.contains("if"):
            pass
        elif instruccion.contains("walk"):
            pass
        elif instruccion.contains("rotate"):
            pass
        elif instruccion.contains("look"):
            pass
        elif instruccion.contains("drop"):
            pass
        elif instruccion.contains("free"):
            pass
        elif instruccion.contains("pick"):
            pass
        elif instruccion.contains("grab"):
            pass
        elif instruccion.contains("walkTo"):
            pass
        elif instruccion.contains("NOP"):
            pass
        elif texto[linea][0:-1] in :
            pass






leerArchivo("PruebaBien1.txt")