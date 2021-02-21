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
            print(correcto, "define")
        elif comando[1] == "block":
            pass
        elif comando[1] == "if":
            pass
        elif (comando[1] == "walk") or (comando[1] == "drop") or (comando[1] == "free") or (comando[1] == "pick") or (comando[1] == "grab"):
            correcto = walkDropFreePickGrab(comando, variables)
        elif comando[1] == "rotate":
            correcto = rotateLook(comando,variables,["left","right","back"])
        elif comando[1] == "look":
            correcto = rotateLook(comando,variables,["N","E","W","S"])
        elif comando[1] == "walkTo":
            correcto = walkTo(comando, variables)
        elif comando[1].lower() == "nop":
            correcto = nop(comando)
        elif comando[1] in functions.keys():
            funciones(comando, variables, functions)
        else:
            correcto = False
        linea += 1

    return (correcto,variables,functions) 

def comando_sin_p(comando, varukas,comandos2_0,palabra):
    for palabra in comando:
        comando_here=comando.index(palabra)
        
        if palabra in comandos2_0 :
            if comando[comando_here+1]=="(" and comando[comando_here+2] in varukas and comando[comando_here+3]==")" :
                comando.pop(comando_here+1)
                comando.pop(comando_here+3)
        elif palabra == "(":
            if comando[comando_here+1]=="(" and comando[comando_here+2]=="(" and comando[-1]==")" and comando[-2]==")" and comando[-3]==")":
                comando.pop(comando_here)
                comando.pop(comando_here+1)
                comando.pop(-1)
                comando.pop(-2)
    return comando

#Comandosss

def If(comando,variables1,funcion):
    correcto=True
    conds=["not","can","blocked?","facing?", ]
    if comando[0]!="(":
        correcto=False
    elif comando[2] == "(": 
        if comando[3] not in conds:
            correcto=False          
        elif comando[3] in conds and comando[4]!= "(":
            correcto=False
        elif comando[3] in conds and comando[4]== "(" or comando[4]== ")":
            if (comando[5]=="blocked?" or comando[5]== "facing?" or comando[5] in funcion) and comando[6]!= ")":
                correcto=False
            elif (comando[5]=="blocked?" or comando[5]== "facing?" or comando[5] in funcion) and comando[6]== ")" and comando[7]!= ")":
                correcto=False
            elif (comando[5]=="blocked?" or comando[5]== "facing?" or comando[5] in funcion) and comando[6]== ")" and comando[7]== ")" and comando[8]!= "(":
                correcto=False
            elif (comando[5]=="blocked?" or comando[5]== "facing?" or comando[5] in funcion) and comando[6]== ")" and comando[7]== ")" and comando[8]== "(" and comando[9] not in funcion:
                correcto=False
            elif (comando[5]=="blocked?" or comando[5]== "facing?" or comando[5] in funcion) and comando[6]== ")" and comando[7]== ")" and comando[8]== "(" and comando[9] in funcion:
                if comando[10]in funcion or comando[10]==")":    
                    correcto=False
                elif comando[11] in variables1 or comando[11]=="(":
                    correcto=False
                elif comando[12] in funcion or comando[12]==")":
                    correcto=False
                elif comando[13] in variables1 or comando[13]=="(":
                    correcto=False
                elif comando[14] in variables1 or comando[14] in funcion:
                    correcto=False
                elif comando[15] in funcion or comando[15]== "(":
                    
                    correcto=False
    return correcto
            


def block(comando1, variables,comandos):
    correcto= True
    if comando1[2]=="(" :
        if comando1[3]==")" or comando1[3] in variables.keys() or comando1[3] not in comandos:
            correcto= False
    else:
        correcto= False
    for i in comando1:
        posicion=comando1.index(i)
        if  i in comandos and comando1[posicion+1] ==")" and comando1[posicion+2]=="(" and comando1[posicion+3] ==")" :
            correcto= False
        elif (i in variables.keys()):           
            if comando1[posicion+1] in variables.keys()and comando1[posicion+2]==")" and comando1[posicion+3]=="(" and comando1[posicion+4]==")":
                correcto=False
            elif comando1[posicion+1] ==")" and comando1[posicion+2] =="(" and comando1[posicion+3] ==")":
                correcto=False
    return correcto


def walkDropFreePickGrab(comando, variables):
    """
    Parser para las funciones de walk, Drop, Free, 
    Pick y Grab
    """
    correcto = False
    if len(comando) == 4:
        if (comando[2].isdigit()):
            correcto = True
        elif (comando[2] in variables.keys()):
            if (variables[comando[2]].isdigit()) :
                correcto = True
            if variables[comando[2]] == True:
                correcto = True
    return correcto

def rotateLook(comando, variables, valores):
    """
    Parser para las funciones de rotate y look. 
    Valores es una lista con los parametros para cada
    comando
    """
    correcto = False
    if len(comando) == 4:
        if (comando[2] in valores):
            correcto = True
        if (comando[2] in variables):
            if variables[comando[2]] == True:
                correcto = True
    return correcto

def walkTo(comando, variables):
    """
    Parser para las funciones de walkTo
    """
    valores = ["N","E","W","S"]
    correcto = False
    if len(comando) == 5:
        if (comando[2].isdigit()):
            if comando[3] in valores:
                correcto = True
        elif (comando[2] in variables.keys()):
            if (variables[comando[2]].isdigit()):
                if comando[3] in valores:
                    correcto = True
            if variables[comando[2]] == True:
                correcto = True
    return correcto

def nop(comando):
    correcto = False
    if len(comando) == 3:
        correcto = True
    return correcto

def define(comando, variables, functions):
    comandos = ["walk","rotate","look","drop","free","pick","grab","walkTo","nop","if","define","block",]
    correcto = False
    if (comando[2].isalnum()):
        if (comando[2] not in comandos) and (comando[2] not in variables.keys()) and (comando[2] not in functions.keys()):
            if len(comando) == 5:
                if (comando[3].isalnum()):
                    if comando[3] in variables.keys():
                        variables[comando[2]] = variables[comando[3]]
                        correcto = True
                    else:
                        variables[comando[2]] = comando[3]
                        correcto = True
            elif len(comando) > 6:
                if (comando[3] == "("):
                    #Parametros
                    variables1 = variables.copy()
                    finP = comando.index(")",4)
                    for i in range(4,finP+1):
                        if (not comando[i].isalnum) or (comando[i] in comandos):
                            print("F")
                            return correcto
                        variables1[comando[i]]=True
                        print
                    #DividirComandos
                    comandosInDef = []
                    comandoact = []
                    open = 1
                    close = 0
                    if comando[finP+1] != "(":
                        return correcto
                    comandoact.append(comando[finP+1])
                    finP += 2
                    while (finP<len(comando)):
                        if comando[finP] == "(":
                            open += 1
                            comandoact.append(comando[finP])
                        elif comando[finP] == ")":
                            close += 1
                            comandoact.append(comando[finP])
                            if close == open:
                                comandosInDef.append(comandoact)
                                open = 1
                                close = 0
                        else:
                            comandoact.append(comando[finP])
                        finP +=1
                        #print("dividir comandos",finP, len(comando))
                    #Analizar comandos
                    numCommand = 0
                    functions1 = functions.copy()
                    functions1[comando[2]] = len(variables1)-len(variables)-1
                    print("len",functions1[comando[2]])
                    correcto = True
                    while (numCommand<len(comandosInDef)) and (correcto == True):
                        comando1 = comandosInDef[numCommand]
                        print("si se puede")
                        if comando1[1] == "block":
                            pass
                        elif comando1[1] == "if":
                            pass
                        elif (comando1[1] == "walk") or (comando[1] == "drop") or (comando[1] == "free") or (comando[1] == "pick") or (comando[1] == "grab"):
                            correcto = walkDropFreePickGrab(comando1, variables1)
                            print(correcto)
                        elif comando1[1] == "rotate":
                            correcto = rotateLook(comando1,variables1,["left","right","back"])
                        elif comando1[1] == "look":
                            correcto = rotateLook(comando1,variables1,["N","E","W","S"])
                        elif comando1[1] == "walkTo":
                            correcto = walkTo(comando1, variables1)
                        elif comando1[1].lower() == "nop":
                            correcto = nop(comando)
                        elif comando1[1] in functions.keys():
                            funciones(comando1, variables1, functions1)
                        else:
                            correcto =  False
                        numCommand += 1
                    if correcto == True:
                        functions[comando[2]] = len(variables1)-len(variables)-1
    return correcto

def funciones(comando, variables, funciones):
    correcto = False
    if (funciones[comando[1]] == 0) and (len(comando) == 3):
        correcto = True
    elif (len(comando) == (funciones[comando[1]]+3)):
        for i in range(2,len(comando)-1):
            if (not comando[i].isdigit) and (comando[i] not in variables.keys()):
                return correcto
        correcto = True
    return correcto

print(analizarArchivo("D:\datos\Jessica\jess\sistemas\lym\Proyecto1\PruebaBien1.txt"))

