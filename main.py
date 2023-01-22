from decimal import Decimal

# Un programa guarda datos en variables. Analogía: variable = cajon, dato = contenido del cajon.

# las variables tienen nombre.
# Reglas:
# - empiezan con una 'letra minuscula' o '_' (guion bajo). No pueden empezar con un numero.
# - siguen (si tienen mas de una letra) con 'letra minuscula', '_' o 'numero'.
# - no pueden tener espacios en blanco (usar '_' en ese caso), ni ñ, ni tildes, ni diéresis, ni nada.
# Nota: se podrían usar letras MAYUSCULAS (va a funcionar PERO es un estilo incorrecto)
# para asignar datos a variables se pone un 'variable = dato'
# Ejemplos:

edad = 20
pi = 3.14159265358979323846264338327950288419716939937510
mol = 6.022e+23
numero_complejo = 5 + 4j
nombre_y_apellido = 'Juan Perez'
tiene_hijos = True
en_chino = '新时代，我在中国|大厨小用？捷克老铁包的除夕水饺嘎嘎香'

nombre, apellido, estatura = 'Juan', 'Perez', 1.76
x = y = z = 0

# problemas con comillas en textos ('strings') resueltos
texto1 = "La palabra sintoísmo proviene del japonés shinto ('camino de los dioses')."
texto2 = 'La palabra sintoísmo proviene del japonés shinto ("camino de los dioses").'
texto3 = "\"Lo se\", dijo él, \"le he oido decir 'ayúdenme' mientras caía.\""

texto_multi_linea = """Esta es la "primera linea",
seguida de la 'segunda linea', 
y hay una "tercera linea" y es la ultima"""  # también podria usarse 3 comillas simples.
otro_texto_multi_linea = 'primera linea\nsegunda linea\ntercera linea'  # \n significa saltar a new line

# mal estilo, NO USAR
a=20  # el signo igual deberia tener un espacio antes y uno despues
PHONE = 12345678  # variable en mayusculas
MiPerro = 'Bobby'  # letras mayusculas para separar palabras, deberia ser mi_perro

# a una variable le puedo asignar un calculo, y lo que se asigna es el resultado final
var1 = 2 + 3 - (4 * 5) + (edad / 2)
var2 = 'hola ' + 'que tal'
var3 = '=-' * 10

# cero y vacio es diferente
edad = 0  # significa que tiene menos de un año (el cajon edad tiene un numero 0 adentro)
edad = None  # significa que la variable no tiene ningun dato (el cajon edad esta vacio)

# Para preguntar que TYPE de datos tiene una variable, usamos una funcion type()
print(var)
print(type(var))  # devuelve: dict

# TIPOS (types) DE VARIABLES SIMPLES (guardan un solo dato)

# - de texto: se llaman 'String' o 'cadena de caracteres', su type es 'str'
text = 'hola'  # type: str

# - numéricas:
entero = 20  # type int  (en Python3, int no tiene límites)
con_decimales = 4.20  # type float  (ojo, hay límite en cantidad de decimales)
complejo = 2 + 4j  # type: complex

# - Booleanas (logica):
tiene_hermanos = False  # type: bool #(solo puede tomar valores True o False, logica de bool en matematica)

# - NoneType (cajon vacio)
pais = None  # type: NoneType

# TIPOS (types) DE VARIABLES MULTIPLES (guardan una coleccion de datos).

# - Listas (un cajon con una lista de elementos Ordenados SI modificables luego de creados)
phones = ['4444-1234', '11 4999-8877', '+54 911 5566-7788']  # type: list
cosas = ['Pedro', 123, True, 1 + 2j, 'carpintero', 12.34]  # type: list

# - Dictionaries (un cajon con sub-cajones con nombres)
persona = {'nombre': 'Juan', 'apellido': 'Perez', 'edad': 20}  # type: dict

# - Tuples (un cajon con una lista de elementos Ordenados NO modificables luego de creados)
this_tuple = ("apple", "banana", "cherry")  # type: tuple

# - Sets (un cajon con una lista de elementos NO Ordenados, NO modificables, NO duplicados, agregables y quitables)
set_de_frutas = {"apple", "banana", "cherry"}  # type: set
frozenset_de_frutas = frozenset({"apple", "banana", "cherry"})  # type: frozenset





# Problema 1: Precisión de los números float debido a que estan codificados en binario
0.1 + 0.1 == 0.2          # True
0.1 + 0.1 + 0.1 == 0.3    # False!!!
0.1 + 0.1 + 0.1           # 0.30000000000000004 !!!
Decimal(0.1 + 0.1 + 0.1)  # 0.3000000000000000444089209850062616169452667236328125
Decimal(0.3)              # 0.299999999999999988897769753748434595763683319091796875



# Problema 2: (Historico), como se codifica texto en los bytes de la compu (o en internet)
# - al principio ASCII: 127 caracteres https://www.ascii-code.com
bytes('Conversión de la eñe', encoding='ascii')  # falla porque no hay ni ó ni ñ en ASCII
# - luego Extended ASCII: 255 caracteres https://www.ascii-code.com  (ISO-8859-1 (latin-1), etc...)
bytes('Conversión de la eñe', encoding='latin-1')  # OK
str(b'Conversi\xf3n de la e\xf1e', encoding='latin-1')
# - UNICODE y utf-8 (el mas usado), utf-16, utf-32, incorporan caracteres de todos los idiomas en un unico set
#   https://home.unicode.org Everyone in the world should be able to use their own language on phones and computers.
bytes('Conversión de la eñe', encoding='utf-8')  # OK
str(b'Conversi\xc3\xb3n de la e\xc3\xb1e', encoding='utf-8')
bytes('新时代，我在中国|大厨小用？捷克老铁包的除夕水饺嘎嘎香', encoding='utf-8')
bytes('بورتريه للشخص العراقي في آخر ', encoding='utf-8')
#   Ahora podemos guardar datos en bytes (o transmitir bytes por internet) con un solo encoding.
#   PERO necesitamos SABER o ADIVINAR en que encoding esta para convertirlo
str(b'Conversi\xc3\xb3n de la e\xc3\xb1e', encoding='utf-8')  # devuelve algo incorrecto

