""" 
Actividad 3.2 Programando un DFA
    Por: 
    Arturo Duran Castillo - A00833516
    Ramón Esaú Gómez González - A00832787
"""
DECIMAL = {'1', '2' , '3', '4', '5', '6', '7', '8', '9' , '0'}
LETTER = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
OPERATOR = {'+', '-', '=', '/', '*'}
SPECIAL = {'(', ')'}
OTHER = {".", " ", "_"}
ALPHABET = DECIMAL | LETTER | OPERATOR | SPECIAL | OTHER
f = open('index.html','w')
#String en el que almacenamos el inicio de nuestro documento html y las clases para cada tipo de elemento de python
startFile = """
<!DOCTYPE html>
<html>
  <head>
    <style>

        .comment {
          color: green;
        }

        .identifyer {
          color: lightskyblue;
        }
        
        .reserved {
          color: purple;
        }
        
        .literal {
          color: lightgreen;
        }
        
        .operator {
          color: white;
        }
        
        .delimiter {
          color: yellow;
        }
        
        html {
          background-color: black;
          line-height: .1px;
        }

        p {
            display: inline-block;
        }
    </style>
  </head>
  <body>
"""
#string en el que guardamos las etiquetas de cierre de <html> y <body>
closeFile = """
</body>
</html>
"""
#Strings en los que almacenamos la etiqueta con la que se personalizará cada token de python sgún su tipo
comment = '<p class="comment">'
identifyer = '<p class="identifyer">'
reserved = '<p class="reserved">'
literal = '<p class="literal">'
operator = '<p class="operator">'
delimiter = '<p class="comment">'
closingTag ='</p>'

def errorDetector(actual, next, token, char):
    numbersNotValid = {8, 9, 13, 14}
    numbers = {7, 8, 9, 10, 11, 12, 13, 14, 15}
    if (actual == 7 and next == 17): # Variable no empieza con letra 
        print (token + char, "-> Variable no valida")
        return True 
    if (actual in numbersNotValid and next not in numbers): # Error en numeros 
        print (token, "-> Numero no valido")
        return True
    if (next == 20): # Se va a mover al estado de error 
        print (token + char, "-> Expresion no valida!")
        return True
    else: 
        return False
    
def tokenHandler(actual, next, token, char):
    if (errorDetector(actual, next, token, char)): # En caso de recibir un token no valido
        return "ERROR"
    
    fix = False # Cuando se le agrega algo a token y se debe quitar si es que se necesitaba imprimir sin el token 

    if (next in {7, 8, 9, 10, 11, 12, 13, 14, 15}): # NUMBERS
        token += char 
        fix = True
    elif (actual in {7, 10}): # Se termino el Entero 
        tag = literal + ' ' + token + closingTag
        f.write(tag)
        # print(token, "-> Integer")
        token = ""
    elif (actual in {12, 15, 11}): 
        tag = literal + ' ' + token + closingTag
        f.write(tag)
        # print(token, "-> Floating")
        token = ""

    if(actual == 1 and next != 7): # MINUS
        tag = operator + ' ' + token + closingTag
        f.write(tag)
        # print(token, "-> Minus")
        token = ""

    if (next in {6, 16}): # DIVISION OR COMMENT
        token += char
        fix = True 
    elif (actual == 6): # Se termino la Division
        if (fix):
            tag = operator + ' ' + token[:-1] + closingTag
            f.write(tag)
            # print (token[:-1], "-> Division")
            token = token[-1]
        else:
            tag = operator + ' ' + token + closingTag
            f.write(tag)
            # print(token, "-> Division")
            token = ""
    elif (actual == 16): # Se termino el comentario
        tag = comment + ' ' + token + closingTag
        f.write(tag)
        # print(token, "-> Comment")
        token = ""

    if (next == 17): # VARIABLES 
        token += char
        fix = True 
    elif (actual == 17 and next != 17): # Se termino la variable
        if (fix): 
            tag = identifyer + ' ' + token[:-1] + closingTag
            f.write(tag)
            # print (token[:-1], "-> Variable")
            token = token[-1]
        else:
            tag = identifyer + ' ' + token + closingTag
            f.write(tag)
            # print(token, "-> Variable")
            token = ""

    if (next in {4, 3}): # POWER
        token += char
        fix = True
    elif (actual == 4): # Se termino el Power
        if (fix): 
            tag = operator + ' ' + token[:-1] + closingTag
            f.write(tag)
            # print (token[:-1], "-> Power")
            token = token[-1]
        else:
            tag = operator + ' ' + token + closingTag
            f.write(tag)
            # print(token, "-> Power")
            token = ""
    elif (actual == 3): # Se termino la Multiplicacion
        if (fix): 
            tag = operator + ' ' + token[:-1] + closingTag
            f.write(tag)
            # print (token[:-1], "-> Multiplication")
            token = token[-1]
        else:
            tag = operator + ' ' + token + closingTag
            f.write(tag)
            # print(token, "-> Multiplication")
            token = ""


    if (next == 2): # PLUS 
        # print(char, "-> Plus")
        tag = operator + ' ' + char + closingTag
        f.write(tag)
    elif (next == 1): # MINUS
        token += char 
    elif (next == 5): # EQUALS
        tag = operator + ' ' + char + closingTag
        f.write(tag)
        # print(char, "-> Equals")
    elif (next == 19): # OPENING PARENTHESIS
        tag = operator + ' ' + char + closingTag
        f.write(tag)
        # print(char, "-> Opening parenthesis")
    elif (next == 18): # CLOSING PARENTHESIS
        tag = operator + ' ' + char + closingTag
        f.write(tag)
        # print(char, "-> Closing parenthesis")
    elif (next == 21): # POWER
        tag = operator + ' ' + char + closingTag
        f.write(tag)
        # print(char, "-> Power")
    elif (next == 22): # COLON
        tag = operator + ' ' + char + closingTag
        f.write(tag)
        # print(char, "-> Colon")
    elif (char == '\n'): # salto de linea
        f.write('<br>')
        return token
    elif (char == ' '): 
        f.write('<p>&nbsp;<p>')
        return token        
    return token


def getMovement(char): 
    if (char in DECIMAL): 
        return "DECIMAL"
    elif (char in {"E", "e"}): 
        return "E,e"
    elif (char in LETTER): 
        return "LETTER"
    else:
        return char
    
def analyzeFile(file): 
    d = [{"DECIMAL": 7, "LETTER": 17, "E,e": 17, "+": 2, "-": 1,"*": 3, "/": 6, "=": 5, "(": 19, ")": 18, " ": 0, ".": 11, "_": 20, "^": 21, "\n": 0, '#':16, ':':22 }, # q0
        {"DECIMAL": 7, "LETTER": 17, "E,e": 8, "+": 2, "-": 1,"*": 3, "/": 6, "=": 5, "(": 19, ")": 18, " ": 0, ".": 20, "_": 20, "^": 21, "\n": 0, '#':16, ':':22 }, #q1
        {"DECIMAL": 7, "LETTER": 17, "E,e": 8, "+": 2, "-": 1,"*": 3, "/": 6, "=": 5, "(": 19, ")": 18, " ": 0, ".": 11, "_": 20, "^": 21, "\n": 0, '#':16, ':':22 }, #q2
        {"DECIMAL": 7, "LETTER": 17, "E,e": 17, "+": 2, "-": 1,"*": 4, "/": 6, "=": 5, "(": 19, ")": 18, " ": 0, ".": 20, "_": 20, "^": 21, "\n": 0, '#':16, ':':22 }, #q3
        {"DECIMAL": 7, "LETTER": 17, "E,e": 17, "+": 2, "-": 1, "*": 3, "/": 6, "=": 5, "(": 19, ")": 18, " ": 0, ".": 20, "_": 20, "^": 21, "\n": 0, '#':16, ':':22 }, #q4
        {"DECIMAL": 7, "LETTER": 17, "E,e": 17, "+": 2, "-": 1,"*": 3, "/": 6, "=": 5, "(": 19, ")": 18, " ": 0, ".": 20, "_": 20, "^": 21, "\n": 0, '#':16, ':':22 }, #q5
        {"DECIMAL": 7, "LETTER": 17, "E,e": 17, "+": 2, "-": 1,"*": 3, "/": 20, "=": 5, "(": 19, ")": 18, " ": 0, ".": 20, "_": 20, "^": 21, "\n": 0, '#':16, ':':22 }, #q6
        {"DECIMAL": 7, "LETTER": 17, "E,e": 8, "+": 2, "-": 1,"*": 3, "/": 6, "=": 5, "(": 19, ")": 18, " ": 0, ".": 11, "_": 20, "^": 21, "\n": 0, '#':16, ':':22 }, #q7
        {"DECIMAL": 10, "LETTER": 17, "E,e": 17, "+": 9, "-": 9,"*": 3, "/": 6, "=": 5, "(": 19, ")": 18, " ": 0, ".": 20, "_": 20, "^": 21, "\n": 0, '#':16, ':':22 }, #q8
        {"DECIMAL": 10, "LETTER": 17, "E,e": 17, "+": 9, "-": 9,"*": 3, "/": 6, "=": 5, "(": 19, ")": 18, " ": 0, ".": 20, "_": 20, "^": 21, "\n": 0, '#':16, ':':22 }, #q9
        {"DECIMAL": 10, "LETTER": 17, "E,e": 17, "+": 2, "-": 1,"*": 3, "/": 6, "=": 5, "(": 19, ")": 18, " ": 0, ".": 11, "_": 20, "^": 21, "\n": 0, '#':16, ':':22 }, #q10
        {"DECIMAL": 12, "LETTER": 20, "E,e": 17, "+": 2, "-": 1,"*": 3, "/": 6, "=": 5, "(": 19, ")": 18, " ": 0, ".": 20, "_": 20, "^": 21, "\n": 0, '#':16, ':':22 }, #q11
        {"DECIMAL": 12, "LETTER": 17, "E,e": 13, "+": 2, "-": 1,"*": 3, "/": 6, "=": 5, "(": 19, ")": 18, " ": 0, ".": 20, "_": 20, "^": 21, "\n": 0, '#':16, ':':22 }, #q12
        {"DECIMAL": 15, "LETTER": 17, "E,e": 17, "+": 14, "-": 14,"*": 3, "/": 6, "=": 5, "(": 19, ")": 18, " ": 0, ".": 20, "_": 20, "^": 21, "\n": 0, '#':16, ':':22 }, #q13
        {"DECIMAL": 15, "LETTER": 17, "E,e": 17, "+": 14, "-": 14,"*": 3, "/": 6, "=": 5, "(": 19, ")": 18, " ": 0, ".": 20, "_": 20, "^": 21, "\n": 0, '#':16, ':':22 }, #q14
        {"DECIMAL": 15, "LETTER": 17, "E,e": 17, "+": 2, "-": 1,"*": 3, "/": 6, "=": 5, "(": 19, ")": 18, " ": 0, ".": 20, "_": 20, "^": 21, "\n": 0, '#':16, ':':22 }, #q15
        {"DECIMAL": 16, "LETTER": 16, "E,e": 16, "+": 16, "-": 16,"*": 16, "/": 16, "=": 16, "(": 16, ")": 16, " ": 16, ".": 16, "_": 16, "^": 16, "\n": 0, '#':16, ':':16 }, #q16
        {"DECIMAL": 17, "LETTER": 17, "E,e": 17, "+": 2, "-": 1,"*": 3, "/": 6, "=": 5, "(": 19, ")": 18, " ": 0, ".": 20, "_": 17, "^": 21, "\n": 0, '#':16, ':':22 }, #q17
        {"DECIMAL": 7, "LETTER": 17, "E,e": 17, "+": 2, "-": 1,"*": 3, "/": 6, "=": 5, "(": 19, ")": 18, " ": 0, ".": 20, "_": 20, "^": 21, "\n": 0, '#':16, ':':22 }, #q18
        {"DECIMAL": 7, "LETTER": 17, "E,e": 17, "+": 2, "-": 1,"*": 3, "/": 6, "=": 5, "(": 19, ")": 18, " ": 0, ".": 20, "_": 20, "^": 21, "\n": 0, '#':16, ':':22 }, #q19
        {"DECIMAL": 7, "LETTER": 17, "E,e": 17, "+": 2, "-": 1,"*": 3, "/": 6, "=": 5, "(": 19, ")": 18, " ": 0, ".": 20, "_": 20, "^": 21, "\n": 0, '#':16, ':':22 }, #q20
        {"DECIMAL": 7, "LETTER": 17, "E,e": 17, "+": 2, "-": 1,"*": 3, "/": 6, "=": 5, "(": 19, ")": 18, " ": 0, ".": 20, "_": 20, "^": 21, "\n": 0, '#':16, ':':22 }, #q21
        {"DECIMAL": 7, "LETTER": 17, "E,e": 17, "+": 2, "-": 1,"*": 3, "/": 6, "=": 5, "(": 19, ")": 18, " ": 0, ".": 20, "_": 20, "^": 21, "\n": 0, '#':16, ':':22 } # q22
        ] 
    state = 0 
    # acceptance = {1, 2, 3, 4, 5, 6, 7, 10, 12, 15, 16, 17, 18, 19, 21}
    token = "" 
    for char in file: 
        move = getMovement(char)
        token = tokenHandler(state, d[state][move], token, char)
        if (token == "ERROR"):
            state = 0
            token = ""
        else: 
            state = d[state][move]

    if (len(token) > 0): #If the file ends with a comment
        tokenHandler(state, d[state]["\n"], token, "\n") 



# Receives the name of a file and returns a list with each of its lines.
def lexerAritmetico(file_name):
    with open(file_name, "r") as file: 
        return file.read()


def main():
    # file_name = input("Ingrese el nombre del archivo: ")
    
    f.write(startFile)
   
    file_name = 'ejemplo.txt'
    file = lexerAritmetico(file_name) 
    analyzeFile(file)
    f.write(closeFile)
    f.close()


main() 