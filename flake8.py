class Pruebas:
    # define dos listas con las letras mayusculas
    # y minusculas como atributo de la clase
    mayusculas = ['A', 'B', 'C', 'D', 'E',
                  'F', 'G', 'H', 'I', 'J',
                  'K', 'L', 'M', 'N', 'O',
                  'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']
    minusculas = ['a', 'b', 'c', 'd', 'e',
                  'f', 'g', 'h', 'i', 'j',
                  'k', 'l', 'm', 'n', 'o',
                  'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z']

# funcion para determinar que un caracter esté entre A y Z
    def check_char(self, entrada):
        # define 2 listas con los atributos de la
        # clase para mayusculas y minusculas
        mayusculas = self.mayusculas
        minusculas = self.minusculas
        tipodato = isinstance(entrada, str)
        error = "error(22): Invalid Argument"  # define un mensaje de error
        # determina si la entrada es un string
        if tipodato is True:  # confirma que la entrada sea un string
            if len(entrada) == 1:
                # confirma que la entrada sea solo un caracter
                if entrada in mayusculas or entrada in minusculas:
                    # confirma que el caracter pertenezca al alfabeto
                    return 0
                else:
                    return error  # retornar error unico
            else:
                return error  # retornar error unico
        else:
            return error  # retornar error unico

    # función que pasa de minuscula a mayuscula el carácter de entrada
    def caps_switch(self, entrada):
        mayusculas = self.mayusculas
        minusculas = self.minusculas
        ent = Pruebas()
        error = "error(22): Invalid Argument"  # define un mensaje de error
        # define un objeto para poder usar la funcion check_char
        if ent.check_char(entrada) == 0:
            # se cumple que sea un caracter entre a y z
            if entrada in mayusculas:
                return minusculas[mayusculas.index(entrada)]
                # pasa de mayusculas a minusculas
            if entrada in minusculas:
                return mayusculas[minusculas.index(entrada)]
                # pasa de minusculas a mayusculas
        else:
            return error  # retornar error unico


digitado = input("Digite una entrada:")
prb = Pruebas()
print("Resultado check_char =>", prb.check_char(digitado))
print("Resultado caps_switch =>", prb.caps_switch(digitado))
