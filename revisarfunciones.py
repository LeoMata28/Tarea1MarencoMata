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

class TestClass:
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

    #funcion para confirmar que todos los caracteres del A a Z cumplen con la funcion check_char
    def test_uno(self):
        #define nuevas listas con los valores de los atributos de la clase
        mayusculas = self.mayusculas
        minusculas = self.minusculas
        ent=Pruebas()#se genera un objeto para poder llamar a las funciones de la clase Pruebas
        for i1 in mayusculas:#toma todos los valores de la lista mayusculas
            assert ent.check_char(i1)==0#confirma que todas las minusculas cumplan con check_char
        for i2 in minusculas:#toma todos los valores de la lista mayusculas
            assert ent.check_char(i2)==0#confirma que todas las minusculas cumplan con check_char

    def test_dos(self):
        mayusculas = self.mayusculas
        minusculas = self.minusculas
        cont1=0#define dos variables numericas como contadores
        cont2=0
        ent=Pruebas()
        for i1 in mayusculas:#toma todos los valores de la lista mayusculas
            assert i1==ent.caps_switch(minusculas[cont1])#revisa que las minusculas se conviertan a mayusculas
            cont1=cont1+1
        for i2 in minusculas:#toma todos los valores de la lista minusculas
            assert i2==ent.caps_switch(mayusculas[cont2])#revisa que las mayusculas se conviertan a minusculas
            cont2=cont2+1

    def test_tres(self):
        entrada="AB"#genera un dato string de más de un caracter
        ent=Pruebas()
        assert ent.check_char(entrada)==0#revisa que se cumpla check_char. Se espera un resultado negativo en pytest

    def test_cuatro(self):
        entrada="$"#genera un dato string de un caracter pero que no está entre A-Z
        ent=Pruebas()
        assert ent.check_char(entrada)==0#revisa que se cumpla check_char. Se espera un resultado negativo en pytest

    def test_cinco(self):
        entrada=85#genera un dato numérico
        ent=Pruebas()
        assert ent.check_char(entrada)==0#revisa que se cumpla check_char. Se espera un resultado negativo en pytest

