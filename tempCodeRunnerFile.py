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