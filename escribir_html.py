# escribe-html.py

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
          color: blue;
        }
        
        .operator {
          color: white;
        }
        
        .delimiter {
          color: yellow;
        }
        
        html {
          background-color: black;
        }
    </style>
  </head>
  <body>
"""

closeFile = """
</body>
</html>
"""

todo = startFile + closeFile 


comment = '<p class="comment">'
identifyer = '<p class="identifyer">'
reserved = '<p class="reserved">'
literal = '<p class="literal">'
operator = '<p class="operator">'
delimiter = '<p class="comment">'
closingTag ='</p>'
f = open('index.html','w')


# f.write(startFile)
f.write(todo)

f.close()