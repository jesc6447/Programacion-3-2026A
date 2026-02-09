#Juan Emmanuel Sanchez Castañon 
#pilas 

cadena1 = "((1+5) * 5(1-2))) - (4+1)"
cadena2 = "{ [ ( 2 + 2 ) * 5 ] / 10 } "
cadena3 = "((((3+4) - (16+2))+(11-3*[4/2]))"
cadena4 = "{[(4 -2) + (4-1[3-1})"
cadena5 = "5+(2*4)-8"

cadenaprueba = "{(})"

def verificar_parentesis(cadena):
    pila = []
    for caracter in cadena:
        if caracter in "([{":
            pila.append(caracter)
        elif caracter in ")]}":
            if not pila:
                return False
            ultimo = pila.pop()
            if (caracter == ")" and ultimo != "(") or (caracter == "]" and ultimo != "[") or (caracter == "}" and ultimo != "{"):
                return False
    return len(pila) == 0

print(verificar_parentesis(cadena1))  
print(verificar_parentesis(cadena2))  
print(verificar_parentesis(cadena3))  
print(verificar_parentesis(cadena4))  
print(verificar_parentesis(cadena5)) 
print(verificar_parentesis(cadenaprueba))  


