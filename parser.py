

def leerArchivo (ruta_archivo):
    archivo= open(ruta_archivo,"r")
    linea=archivo.readline()
    texto = []
    textoStr=""

    while (len(linea)!=0):
        textoStr=textoStr.replace("    ","")#ADDED
        textoStr=textoStr.replace("("," ( ")#ADDED
        textoStr=textoStr.replace(")"," ) ")#ADDED
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
                return texto
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

def analizarArchivo(ruta_archivo):
    texto = leerArchivo (ruta_archivo)
    linea  = 0
    correcto = True
    lista_p = [1]
    functions = []

    if texto[linea][0] != "(":
        correcto = False

    for comando in texto:
        comando=comando.split() 
        parenthesis_o=comando.count("(")
        parenthesis_c=comando.count(")")
        
        print(comando,parenthesis_o, parenthesis_c)
            
"""
    
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
        #elif texto[linea][0:-1] in :
            #pass
"""


print(leerArchivo("PruebaBien1.txt"))
