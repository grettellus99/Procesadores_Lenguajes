
#-------TIPOS de caracteres que pueden entrar
letras = list(range(65,90+1)) + list(range(97,122+1))

digitos = range(48,57+1) 
#32=espacio
palabrasReservadas = ["switch", "case", "default", "break", "let", "int", 
                    "boolean", "string", "if", "function", 
                    "input", "print", "return","eof","true","false"]
c1 = list(range(32,42)) + list(range(43,240)) + list(range(241,255+1))  + list(range(10,11)) + list(range(13,14))
c2 = list(range(32,42)) + list(range(43,47)) + list(range(48,240)) + list(range(241,255+1)) + list(range(10,11)) + list(range(13,14))
c3 = list(range(32,34)) + list(range(35,255+1))
