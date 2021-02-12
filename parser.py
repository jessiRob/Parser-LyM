def leerArchivo (ruta_archivo):
    archivo= open(ruta_archivo,"r")
    linea=archivo.readline()
    texto = []
    textoStr=""

    while (len(linea)!=0):
        textoStr += linea.replace("\n","")
        linea=archivo.readline()
    #print(textoStr)
    #print(len(textoStr))
    s=0
    open1 = 0
    close = 0
    openPos = 0
    while s<(len(textoStr)):
        if open1 == close:
            if textoStr[s] == "(":
                open1 +=1
                openPos = s
                #print("x",open1, close)
            elif (textoStr[s] != " ") and (open1 == 0):
                #print("F")
                return []
            s +=1
        while (open1 != close) and (s<(len(textoStr))):
            if textoStr[s] == "(":
                open1 +=1
            if textoStr[s] == ")":
                close +=1
                #print(open1,close)
                if (open1 == close):
                    open1 = 0
                    close = 0
                    texto.append(textoStr[openPos:s+1])
                    openPos = 0
                #print(texto,textoStr[s] ,s, openPos, open1, close)  
            s +=1
    archivo.close         
    return texto

def separarPalabra(inicio, instruccion):
    i=inicio
    palabra = ""
    while (i < len(instruccion)-1) and (palabra ==""):
        if (instruccion[i] == " ") or (instruccion[i] == "("):
            print("1", instruccion[i])
            i+=1
        else:
            find1 = instruccion[i:].find(" ")
            find2 = instruccion[i:].find("(")
            if (find1 > find2) and (find2 != -1):
                palabra = instruccion[i:find2+i]
            elif (find1 == -1) and (find2 ==-1):
                return False
            else:
                palabra = instruccion[i:find1+i]
            print("2", instruccion[i], find1, find2)
    print("fijo", palabra)
    return palabra

def analizarArchivo(ruta_archivo):
    texto = leerArchivo (ruta_archivo)
    print(texto)
    comando  = 0
    correcto = True
    variables = []
    functions = []

    if texto[comando][0][0] != "(":
        correcto = False

    while correcto and (comando<len(texto)):
        instruccion = texto[comando]
        palabra = separarPalabra(1, instruccion)
        if palabra.contains("define"):
            pass
        elif palabra.contains("block"):
            pass
        elif palabra.contains("if"):
            pass
        elif palabra.contains("walk"):
            pass
        elif palabra.contains("rotate"):
            pass
        elif palabra.contains("look"):
            pass
        elif palabra.contains("drop"):
            pass
        elif palabra.contains("free"):
            pass
        elif palabra.contains("pick"):
            pass
        elif palabra.contains("grab"):
            pass
        elif palabra.contains("walkTo"):
            pass
        elif palabra.contains("NOP"):
            pass
        #elif texto[linea][0:-1] in :
            #pass

        comando += 1
    return correcto






print(analizarArchivo("D:\datos\Jessica\jess\sistemas\lym\Proyecto1\PruebaBien1.txt"))
print("ya")
