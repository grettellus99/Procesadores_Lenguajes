
#-------TIPOS de caracteres que pueden entrar
letras = list(range(65,90+1)) + list(range(97,122+1))

digitos = range(48,57+1) 
#32=espacio
palabrasReservadas = ["switch", "case", "default", "break", "let", "int", 
                    "boolean", "string", "if", "function", 
                    "input", "print", "return" "eof"]
c1 = list(range(33,42)) + list(range(43,255+1))
c2 = list(range(33,42)) + list(range(43,47)) + list(range(48,255+1))
c3 = list(range(33,34)) + list(range(35,255+1))

### lista de operadores o simbolos que tienen S como estado final
op=[40,41,43,44,58,59,123,125]