

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
    variables = {}
    functions = {}

    if texto[linea][0] != "(":
        correcto = False

    while correcto and (linea<len(texto)):
        comando = texto[linea]
        comando=comando.split() 
        parenthesis_o=comando.count("(")
        parenthesis_c=comando.count(")")
        
        print(comando,parenthesis_o, parenthesis_c)
            
        if comando[1] == "define":
            correcto = define(comando, variables, functions)
        elif comando[1] == "block":
            pass
        elif comando[1] == "if":
            pass
        elif comando[1] == "walk":
            correcto = walk(comando, variables)
        elif comando[1] == "rotate":
            pass
        elif comando[1] == "look":
            pass
        elif comando[1] == "drop":
            pass
        elif comando[1] == "free":
            pass
        elif comando[1] == "pick":
            pass
        elif comando[1] == "grab":
            pass
        elif comando[1] == "walkTo":
            pass
        elif comando[1].lower() == "nop":
            pass
        elif comando[1] in functions.keys():
            pass
        
        #elif texto[linea][0:-1] in :
            #pass
        linea += 1

    return correcto

def walk(comando, variables):
    correcto = False
    if len(comando) == 4:
        if (comando[2].isdigit()):
            correcto = True
        elif (comando[2] in variables.keys()):
            if (variables[comando[2]].isdigit()) :
                correcto = True
    return correcto

def define(comando, variables, functions):
    comandos = ["walk","rotate","look","drop","free","pick","grab","walkTo","nop","if","define","block",]
    correcto = False
    if len(comando) == 5:
        if (comando[2].isalnum()):
            if (comando[2] not in comandos):
                if (comando[3].isalnum()):
                    variables[comando[2]] = comando[3]
    elif len(comando) == 5:
        pass

    return correcto

print(leerArchivo("PruebaBien1.txt"))
