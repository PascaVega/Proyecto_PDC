# Calculadora de integrales definidas por medio de distintos métodos numéricos

#Se importan las librerias
import math
import random

"""
Se define la precedencia de los operadores para convertir la expresión 
de la función en RPN (Reverse Polish Notation)
"""

precedencia : dict = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "sin": 4, "cos": 4, "tan": 4, "asin": 4, "acos": 4, "atan": 4}
asociacion : dict = {"+": True, "-": True, "*": True, "/": True, "^": False}

"""Funciones auxiliares"""

#Verifica si un simbolo es un operador (se comprueba en "precedencia" (dicccionario))
def operador(simbolo : str) -> bool:
    return simbolo in precedencia

#Verifica si un operador tiene asociatividad por izquierda
def asociacion_izquierda(simbolo : str) -> bool:
    return simbolo != "^"

def es_funcion(simbolo: str) -> bool:
    return simbolo in {"sin", "cos", "tan", "asin", "acos", "atan"}

#Se convierte la expresión en Notación Polaca Inversa
def convertir_a_RPN(expresion: str) -> str:
    salida = []
    operadores = []
    simbolos = dividir_simbolos(expresion)

    for simbolo in simbolos:

        #Si el simbolo es un número irracional
        if simbolo.isnumeric() or simbolo in ["pi", "e"]:
            salida.append(simbolo)

        #Si el simbolo es una función trigonométrica
        elif simbolo.isalpha() and simbolo not in ["sin", "cos", "tan", "asin", "acos", "atan"]:
            salida.append(simbolo)
        elif simbolo in["sin", "cos", "tan", "asin", "acos", "atan"]:
            operadores.append(simbolo)
        
        #Si el simbolo es un operador aritmético
        elif simbolo in "+-*/^":
            while (operadores and operadores[-1] != "(" and
                   (asociacion.get(simbolo, False) and precedencia.get(simbolo, 0) <= precedencia.get(operadores[-1], 0)) or
                   (not asociacion.get(simbolo, False) and precedencia.get(simbolo, 0) < precedencia.get(operadores[-1], 0))):
                salida.append(operadores.pop())
            operadores.append(simbolo)
        
        #Si el simbolo es un parentesis se elimina
        elif simbolo == "(":
            operadores.append(simbolo)
        elif simbolo == ")":
            while operadores and operadores[-1] != "(":
                salida.append(operadores.pop())
            operadores.pop()
            if operadores and operadores[-1] in ["sin", "cos", "tan", "asin", "acos", "atan"]:
                salida.append(operadores.pop())

    while operadores:
        salida.append(operadores.pop())

    return " ".join(salida)

#Dividir la expresión en simbolos
def dividir_simbolos(expresion: str) -> list:
    simbolos = []
    i = 0
    while i < len(expresion):
        if expresion[i].isspace():
            i += 1
            continue

        if expresion[i] in "+-*/^()":
            simbolos.append(expresion[i])
            i += 1

        elif expresion[i:i+3] in ["sin", "cos", "tan", "sen", "asin", "acos", "atan"]:
            simbolos.append(expresion[i:i+3])
            i += 3

        else:
            simbolo = []
            while i < len(expresion) and (expresion[i].isdigit() or expresion[i].isalpha() or expresion[i] == "."):
                simbolo.append(expresion[i])
                i += 1
            simbolos.append("".join(simbolo))

    return simbolos

#Se ingresa la función y se transforma en RPN
def ingresar_funcion() -> str:

    #Se ingresa la expresión matemática
    expresion : str = input("Introduzca la función: ")

    #Se separan los simbolos
    simbolos : list = dividir_simbolos(expresion)

    #Se transforma en RPN (se eliminan los parentesis)
    rpn  : str = convertir_a_RPN(" ".join(simbolos))
    return rpn

#Se definen los limites de integración de la función
def limites_integracion() -> tuple:
    limite_inferior : float = float(input("Ingrese el límite inferior: "))
    limite_superior : float = float(input("Ingrese el límite superior: "))
    return limite_inferior,limite_superior

"""Se crean las funciones para las operaciones"""

def suma(x : float, y : float) -> float:
    return x + y

def resta(x : float, y : float) -> float:
    return x - y

def multiplicacion(x : float, y : float) -> float:
    return x * y

def division(x : float, y : float) -> float:
    if y == 0:
        raise ValueError("División por cero")
    return x / y

def potencia(x : float, y : float) -> float:
    return x ** y

def seno(x : float) -> float:
    return math.sin(x)

def coseno(x : float) -> float:
    return math.cos(x)

def tangente(x : float) -> float:
    return math.tan(x)

def arcseno(x : float) -> float:
    return math.asin(x)

def arccoseno(x : float) -> float:
    return math.acos(x)

def arctangente(x : float) -> float:
    return math.atan(x)

#Se evalua la expresión para ejecutar las operaciones correspondientes
def evaluar_expresion(expresion : str, variables : dict) -> float:

    #Se separa la expresión en términos y operadores
    terminos : list = expresion.split(" ")
    lista : list = []

    #Se define un diccionario de operadores
    operadores : dict = {
        "+": suma,
        "-": resta,
        "*": multiplicacion,
        "/": division,
        "^": potencia,
        "sin": seno,
        "cos": coseno,
        "tan": tangente,
        "asin": arcseno,
        "acos": arccoseno,
        "atan": arctangente
    }

    #Se define los números especiales
    numeros_especiales : dict = {
        "pi": math.pi,
        "e": math.e,
        "phi": (1 + math.sqrt(5)) / 2
    }

    for termino in terminos:

        #Si es un operador, se aplica la operación a los dos últimos elementos de la lista
        if termino in operadores:            
            if termino in {"sin", "cos", "tan", "asin", "acos", "atan"}:
                a : float = lista.pop()
                resultado : float = operadores[termino](a)
            else:
                b : float = lista.pop()
                a : float = lista.pop()
                resultado : float = operadores[termino](a, b)
            lista.append(resultado)

        #Si es una variable, se sustituye por su valor
        elif termino in variables:
            lista.append(variables[termino])

        #Si es un número, se convierte a float y lo añade a la lista
        else:
            lista.append(float(termino))

    #Se retorna el valor de la evalución de la expresión
    return lista[0]

#Selección de métodos
def metodo():
    
    #Se presentan los métodos
    print("Métodos de integración:")
    print("Método del rectágulo (Regla del punto medio) (1) // Método del Trapecio (2) // Método de Simpson (3)")
    print("Método del Trapecio Compuesto (4) // Método de Simpson Compuesto (5)")
    print("Método del Trapecio Adaptativo (6) // Método de Simpson Adaptativo (7)")
    print("Cuadratura de Gauss-Legendre (8) // Integración de Monte Carlo (9)")
    print("Integración de Romberg (10) // Método de Newton-Cotes Cerrado (11)")
    print("Método de Newton-Cotes Abierto (12) ")

    #El usuario seleciona el método a usar
    seleccion : int = int(input("Ingrese el número del método seleccionado: "))

    #Se configuran las selecciones
    if seleccion == 1:
        rectangulo_simple()
        return
    elif seleccion == 2:
        trapecio_simple()
        return
    elif seleccion == 3:
        simpson_simple()
        return
    elif seleccion == 4:
        trapecio_compuesto()
        return
    elif seleccion == 5:
        simpson_compuesto()
        return
    elif seleccion == 6:
        trapecio_adaptativo()
        return
    elif seleccion == 7:
        simpson_adaptativo()
        return
    elif seleccion == 8:
        Gauss_Legendre()
        return
    elif seleccion == 9:
        monte_Carlo()
        return
    elif seleccion == 10:
        romberg()
        return
    elif seleccion == 11:
        newton_cotes_cerrado()
        return
    elif seleccion == 12:
        newton_cotes_abierto()
        return
    
    
    #Si no se ingresa un número dentro de las opciones se retorna a pedir otro número
    else:
        print("Ingrese un método válido.")
        metodo()

"""Método del rectángulo simple (Regla del punto medio)"""

def rectangulo_simple():

    #Se definen las variables para los límites de integración
    a : float = 0
    b : float = 0

    #Se ingresa la función y los límites de integración
    funcion : str = ingresar_funcion()
    a,b = limites_integracion()

    #Se define la variable a integrar
    variable : str = input("Ingrese la variable por la cual se va a integrar: ")

    """
    Para este método se utiliza la siguiente formula
    para realizar la aproximación de la integral: (b-a)*f((a+b)/2)
    """

    base : float = b-a
    x_funcion : float = (a+b)/2

    #Se define un diccionario para evaluar la variable en la función
    variables = {variable : x_funcion}
    altura : float = evaluar_expresion(funcion, variables)
    resultado : float = base*altura

    #Se imprime el resultado
    print(f"Por el método del Réctangulo Simple, el resultado es {resultado}")

    return

"""Método del Trapecio Simple"""

def trapecio_simple():

    #Se definen las variables para los límites de integración
    a : float = 0
    b : float = 0

    #Se ingresa la función y los límites de integración
    funcion : str = ingresar_funcion()
    a,b = limites_integracion()

    #Se define la variable a integrar
    variable : str = input("Ingrese la variable por la cual se va a integrar: ")

    """
    Para este método se utiliza la siguiente formula
    para realizar la aproximación de la integral: ((b-a)/2) * [f(a)+f(b)]
    """

    base : float = (b-a)/2

    #Se define un diccionario para evaluar la variable en la función
    funcion_a = {variable : a}
    funcion_b = {variable : b}
    resultado_a : float = evaluar_expresion(funcion, funcion_a)
    resultado_b : float = evaluar_expresion(funcion, funcion_b)
    resultado : float = base*(resultado_a+resultado_b)

    #Se imprime el resultado
    print(f"Por el método del Trapecio Simple, el resultado es {resultado}")

    return

"""Método de Simpson Simple (Regla de Simpson)"""

def simpson_simple():

    #Se definen las variables para los límites de integración
    a : float = 0
    b : float = 0

    #Se ingresa la función y los límites de integración
    funcion : str = ingresar_funcion()
    a,b = limites_integracion()

    #Se define la variable a integrar
    variable : str = input("Ingrese la variable por la cual se va a integrar: ")

    """Para este método se utiliza la siguiente formula
    para realizar la aproximación de la integral: ((b-a)/6) * [f(a) + 4*f((a+b)/2) + f(b)]
    """
    base : float = (b-a)/6
    c : float = (a+b)/2

    #Se define un diccionario para evaluar la variable en la función
    funcion_a = {variable : a}
    funcion_b = {variable : b}
    funcion_c = {variable : c}
    resultado_a : float = evaluar_expresion(funcion, funcion_a)
    resultado_b : float = evaluar_expresion(funcion, funcion_b)
    resultado_c : float = evaluar_expresion(funcion, funcion_c)
    resultado : float = base*(resultado_a + resultado_b + 4*resultado_c)

    #Se imprime el resultado
    print(f"Por el método del Simpson Simple, el resultado es {resultado}")
    return

"""Método del Trapecio Compuesto"""

def trapecio_compuesto():

    #Se definen las variables para los límites de integración
    a : float = 0
    b : float = 0

    #Se ingresa la función y los límites de integración
    funcion : str = ingresar_funcion()
    a,b = limites_integracion()

    #Se define la variable a integrar y el número de subintervalos
    variable : str = input("Ingrese la variable por la cual se va a integrar: ")
    n : int = int(input("Introduce el número de subintervalos: "))

    """Para este método se utiliza la siguiente formula
    para realizar la aproximación de la integral: 
    (h/2) * [f(a) + 2 ∑ i=1 n-1 f(a+ih) + f(b)]
    """
    #Se define la variable base del intervalo
    h : float = (b - a) / n

    #Se evalúan los extremos iniciales
    funcion_a : dict= {variable: a}
    funcion_b : dict= {variable: b}
    resultado_a : float= evaluar_expresion(funcion, funcion_a)
    resultado_b : float= evaluar_expresion(funcion, funcion_b)

    #Suma de los extremos
    resultado : float = (resultado_a + resultado_b)

    result : float = 0

    #Se calcula el área de los subintervalos
    for i in range(1, n):
        x = a + i * h
        funcion_x = {variable: x}
        result += evaluar_expresion(funcion, funcion_x)

    resultado += (result*2)

    #Se multiplica por el tamaño de los subintervalos
    resultado *= (h/2)

    #Se imprime el resultado
    print(f"Por el método del Trapecio compuesto, el resultado es {resultado}")

    return

"""Método de Simpson Compuesto"""

def simpson_compuesto():

    #Se definen las variables para los límites de integración
    a : float = 0
    b : float = 0

    #Se ingresa la función y los límites de integración
    funcion : str = ingresar_funcion()
    a,b = limites_integracion()

    #Se define la variable a integrar y el número de subintervalos
    variable : str = input("Ingrese la variable por la cual se va a integrar: ")
    n : int = int(input("Introduce el número de subintervalos (debe ser un número par): "))

    if n % 2 != 0:
        raise ValueError("El número de subintervalos debe ser par.")

    """Para este método se utiliza la siguiente formula
    para realizar la aproximación de la integral:
    (h/3) * [f(a) + 4 ∑ n-1 i=1,3,5... f(a+ih) + 2 ∑ n-2 i=2,4,6... f(a+ih) + f(b)]
    """
    #Se define la variable base del intervalo
    h : float = (b - a) / n

    #Se evalúan los extremos iniciales
    funcion_a : dict = {variable: a}
    funcion_b : dict = {variable: b}
    resultado_a : float= evaluar_expresion(funcion, funcion_a)
    resultado_b : float= evaluar_expresion(funcion, funcion_b)

    #Inicializar suma de Simpson
    resultado : float = resultado_a + resultado_b

    #Sumar las evaluaciones de los puntos intermedios
    for i in range(1, n):
        x = a + i * h
        funcion_x = {variable: x}
        if i % 2 == 0:
            resultado += 2 * evaluar_expresion(funcion, funcion_x)
        else:
            resultado += 4 * evaluar_expresion(funcion, funcion_x)

    #Se multiplica por el tamaño de los subintervalos y se divide por 3
    resultado *= h / 3

    #Se imprime el resultado
    print(f"Por el método del Simpson compuesto, el resultado es {resultado}")

    return

"""Métodos del trapecio adaptativo"""

#Función general del método Trapecio Adaptativo
def trapecio_adaptativo():

    #Se definen las variables para los límites de integración
    a : float = 0
    b : float = 0

    #Se ingresa la función y los límites de integración
    funcion : str = ingresar_funcion()
    a,b = limites_integracion()

    #Se define la variable a integrar y la tolerancia
    variable : str = input("Ingrese la variable por la cual se va a integrar: ")
    tol : float = float(input("Introduce la tolerancia: "))

    """
    Para este método se utiliza el método del trapecio simple,
    en donde se implementa un criterio de adaptación.
    """

    resultado : float = trapecio_adaptativo_funcion(funcion, a, b, variable, tol)

    #Se imprime el resultado
    print(f"Por el método del Trapecio Adaptativo, el resultado es {resultado}")

    return

#Funciones de apoyo para el Método del Trapecio Adaptativo
def trapecio(f : str, a : float, b : float, variable : str) -> float:

    #Se obtiene la mitad del intervalo
    medio : float = (a + b) / 2

    #Se calcula la integral de cada subintervalo
    funcion_a : float = evaluar_expresion(f, {variable: a})
    funcion_b : float = evaluar_expresion(f, {variable: b})
    funcion_media : float = evaluar_expresion(f, {variable: medio})
    return (b - a) * (funcion_a + 2 * funcion_media + funcion_b) / 4.0

def trapecio_adaptativo_funcion(f : str, a : float, b : float, variable : str, tol : float) -> float:
    #Se obtiene la mitad del intervalo
    medio : float = (a + b) / 2

    #Integral del intervalo completo
    t1 : float= trapecio(f, a, b, variable)

    #Suma de las integrales de los subintervalos
    t2 : float= trapecio(f, a, medio, variable) + trapecio(f, medio, b, variable)

    """Se compara la suma de las integrales de los subintervalos con la integral del intervalo completo.
    Si la diferencia es menor que la tolerancia, suma las integrales.
    De lo contrario, se subdivide cada subintervalo y se repite el proceso recursivamente."""

    if abs(t2 - t1) < tol:
        return t2
    else:
        return trapecio_adaptativo_funcion(f, a, medio, variable, tol / 2) + trapecio_adaptativo_funcion(f, medio, b, variable, tol / 2)

"""Método de Simpson Adaptativo"""

#Función general del método Simpson Adaptativo
def simpson_adaptativo():

    #Se definen las variables para los límites de integración
    a : float = 0
    b : float = 0

    #Se ingresa la función y los límites de integración
    funcion : str = ingresar_funcion()
    a,b = limites_integracion()

    #Se define la variable a integrar y la tolerancia
    variable : str = input("Ingrese la variable por la cual se va a integrar: ")
    tol : float = float(input("Introduce la tolerancia: "))

    """Para este método se apoya del método simpson simple
    y se parte de un criterio de adaptación.
    """
    resultado : float  = simpson_adaptativo_funcion(funcion, a, b, variable, tol)

    #Se imprime el resultado
    print(f"Por el método del Simpson Adaptativo, el resultado es {resultado}")
    return

#Funciones de apoyo para el método simpson adaptativo
def simpson(f, a, b, variable) -> float:
    #Se obtiene el punto medio del intervalo
    medio : float= (a + b) / 2

    #Se calculan las funciones de cada extremo de los intervalos
    funcion_a : float = evaluar_expresion(f, {variable: a})
    funcion_b : float = evaluar_expresion(f, {variable: b})
    funcion_medio : float = evaluar_expresion(f, {variable: medio})

    #Se retorna el resultado del método simpson
    return (b - a) * (funcion_a + 4 * funcion_medio + funcion_b) / 6

def simpson_adaptativo_funcion(f : str, a : float, b : float, variable : str, tol : float, funcion_a=None, funcion_b=None, funcion_medio=None) -> float:
    #Se halla el punto medio del intervalo
    medio : float = (a + b) / 2

    #Se evaluan las funciones en los extremos y en el punto medio
    if funcion_a is None:
        funcion_a = evaluar_expresion(f, {variable: a})
    if funcion_b is None:
        funcion_b = evaluar_expresion(f, {variable: b})
    if funcion_medio is None:
        funcion_medio = evaluar_expresion(f, {variable: medio})
    
    #Se obtienen los puntos medios de cada subintervalo y se evaluan en la función
    medio_izquierda : float= (a + medio) / 2
    medio_derecha : float = (medio + b) / 2
    funcion_medio_izquierda : float = evaluar_expresion(f, {variable: medio_izquierda})
    funcion_medio_derecha : float = evaluar_expresion(f, {variable: medio_derecha})

    #Se calculan las aproximaciones de las integrales (sienso s2 más exacta que s1 al tener en cuenta más puntos de evaluación)
    s1 : float = (b - a) * (funcion_a + 4 * funcion_medio + funcion_b) / 6
    s2 : float = (b - a) * (funcion_a + 4 * funcion_medio_izquierda + 2 * funcion_medio + 4 * funcion_medio_derecha + funcion_b) / 12

    """Si la diferencia entre la integral de los subintervalos y
    la integral del intervalo completo es menor que la tolerancia, se acepta la integral.
    De lo contrario, se subdividen los subintervalos y se repite el proceso recursivamente.
    """
    if abs(s2 - s1) < 15 * tol:
        return s2 + (s2 - s1) / 15
    else:
        integral_izquierda = simpson_adaptativo_funcion(f, a, medio, variable, tol / 2, funcion_a, funcion_medio, funcion_medio_izquierda)
        integral_derecha = simpson_adaptativo_funcion(f, medio, b, variable, tol / 2, funcion_medio, funcion_b, funcion_medio_derecha)
        return integral_izquierda + integral_derecha

"""Método de Cuadratura de Gauss"""

#Método para la Cuadratura de Gauss-Legendre
def Gauss_Legendre():

    #Se definen las variables para los límites de integración
    a : float = 0
    b : float = 0

    #Se ingresa la función y los límites de integración
    funcion : str = ingresar_funcion()
    a,b = limites_integracion()

    #Número de puntos de Gauss-Legendre
    n : int = int(input("Introduce el número de puntos para la cuadratura de Gauss-Legendre: "))

    #Calcular la integral utilizando la cuadratura de Gauss-Legendre
    resultado : float = cuadratura_gauss_legendre(funcion, a, b, n)

    #Imprimir el resultado
    print(f"La aproximación de la integral utilizando la cuadratura de Gauss-Legendre es: {resultado}")

    return

#Funciones de apoyo para el método de la Cuadratura de Gauss-Legenddre
def cuadratura_gauss_legendre(funcion : str, a : float, b : float, n : int) -> float:

    #Se define la variable a integrar
    variable : str = input("Ingrese la variable por la cual se va a integrar: ")

    #Cálculo de los nodos y pesos de Gauss-Legendre
    nodos, pesos = gauss_legendre_nodos_pesos(n)

    #Transformación de coordenadas para el intervalo [a, b]
    x = lambda x: ((b - a) * x + (b + a)) / 2

    #Evaluación de la integral
    integral : float = sum(pesos[i] * evaluar_expresion(funcion,{variable: x(nodos[i])}) for i in range(n))
    integral *= (b - a) / 2
    
    return integral

#Obtener los nodos y pesos de Gauss-Legendre para n puntos.
def gauss_legendre_nodos_pesos(n : int) -> tuple:

    #Inicializar nodos
    nodos = [0] * n
    pesos = [0] * n

    #Encontrar nodos usando el método de Newton-Raphson
    for i in range(n):
        x = math.cos(math.pi * (i + 0.75) / (n + 0.5))
        for _ in range(10):  #Iteraciones de Newton-Raphson
            Pn = legendre(n, x)
            Pn_deriv = legendre_derivada(n, x)
            x -= Pn / Pn_deriv
        nodos[i] = x

        # Calcular los pesos
        Pn_deriv = legendre_derivada(n, nodos[i])
        pesos[i] = 2 / ((1 - nodos[i] ** 2) * Pn_deriv ** 2)

    return nodos, pesos

#Polinomio de Legendre de grado n evaluado en x.
def legendre(n: int, x: float) -> float:
    if n == 0:
        return 1    
    elif n == 1:
        return x
    else:
        p0 : float = 1
        p1 : float = x
        for k in range(2, n + 1):
            p2 = ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
            p0 = p1
            p1 = p2
        return p2

#Evaluar la derivada del polinomio de Legendre de grado n en x.
def legendre_derivada(n, x):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        Pn = legendre(n, x)
        Pnm1 = legendre(n - 1, x)
        return n * (x * Pn - Pnm1) / (x ** 2 - 1)

"""Método de Monte Carlo"""

#Integración de Monte Carlo
def monte_Carlo():

    #Se definen las variables para los límites de integración
    a : float = 0
    b : float = 0

    #Se ingresa la función y los límites de integración
    funcion : str = ingresar_funcion()
    a,b = limites_integracion()

    #Número de puntos de la muestra
    n : int = int(input("Introduce el número de puntos de la muestra: "))

    """
    Para este método se utiliza la siguiente formula
    para realizar la aproximación de la integral: 
    (b-a)/n * ∑ i=1 n f(x_i)
    """

    #Calcular la integral utilizando el método de Monte Carlo
    resultado : float = monte_Carlo_funcion(funcion, a, b, n)

    #Imprimir el resultado
    print(f"La aproximación de la integral con el método de Monte Carlo: {resultado}")

    return

#Función de apoyo para Integración de Monte Carlo
def monte_Carlo_funcion(funcion : str, a : float, b : float, n : int) -> float:

    #Se define la variable a integrar
    variable : str = input("Ingrese la variable por la cual se va a integrar: ")

    total = 0
    for _ in range(n):
        x = random.uniform(a, b)
        variables : dict = {variable : x}
        total += evaluar_expresion(funcion,variables)
    return (b - a) * total / n

"""Método de Romberg"""

#Integración de Romberg
def romberg():
    
    #Se definen las variables para los límites de integración
    a : float = 0
    b : float = 0

    #Se ingresa la función y los límites de integración
    funcion : str = ingresar_funcion()
    a,b = limites_integracion()

    #Número máximo de iteraciones (profundidad de la tabla de Romberg)
    max_iter : int = int(input("Introduce el número máximo de iteraciones: "))

    """
    Para esta técnica se integra por trapecios a diferentes niveles de refinación, 
    luego se utiliza la extrapolación de Richardson para mejorar la precisión de la estimación de la integral.
    """

    #Calcular la integral utilizando el método Romberg
    resultado = romberg_funcion(funcion, a, b, max_iter)

    #Mostrar la tabla de Romberg
    print("Tabla de Romberg:")
    for i in range(len(resultado)):
        for j in range(i + 1):
            print(f"resultado[{i}][{j}] = {resultado[i][j]:.10f}", end="  ")
    print()

    return

#Funciones de apoyo para el método de Romberg
def regla_trapezoide(funcion : str, a : float, b : float, n : int, variable : str) -> float:

    #h es el ancho del subintervalo
    h : float = (b - a) / n

    #Se multiplica por 0.5 dado que los extremos sólo contribuyen con la mitad del área de un trapezoide.
    integral : float = 0.5 * (evaluar_expresion(funcion, {variable : a}) + evaluar_expresion(funcion, {variable : b}))

    #Suma las contribuciones de los puntos intermedios
    for i in range(1, n):
        integral += evaluar_expresion(funcion, {variable : a + i * h})

    #Aproximación de la integral
    return integral * h

def romberg_funcion(funcion : str, a : float, b : float, max_iter : int):

    #Se define la variable a integrar
    variable : str = input("Ingrese la variable por la cual se va a integrar: ")

    #R es una matriz que almacenará las aproximaciones de la integral.
    R = [[0 for z in range(max_iter)] for z in range(max_iter)]
    for k in range(max_iter):
        n : float = 2**k

        #Se usa la regla del trapecio para calculas las aproximaciones iniciales
        R[k][0] = regla_trapezoide(funcion, a, b, n, variable)

        """La fórmula de la extrapolación de Richardson es:
        R[k][j]= (4^j * R[k][j-1] - R[k-1][j-1]) / (4^j - 1)        
        """

        #Se aplica la extrapolación de Richardson para pulir las aproximaciones.
        for j in range(1, k + 1):
            R[k][j] = (4**j * R[k][j - 1] - R[k - 1][j - 1]) / (4**j - 1)

    return R

"""Método de Newton-Cotes Cerrado"""

def newton_cotes_cerrado():

    #Se definen las variables para los límites de integración
    a : float = 0
    b : float = 0

    #Se ingresa la función y los límites de integración
    funcion : str = ingresar_funcion()
    a,b = limites_integracion()

    #Número máximo de iteraciones (profundidad de la tabla de Romberg)
    n : int = int(input("Introduce el número de subintervalos: "))

    #Se define la variable a integrar
    variable : str = input("Ingrese la variable por la cual se va a integrar: ")

    #Ancho de cada subintervalo
    h : float = (b - a) / n

    """
    Se utiliza un polinomio interpolador en el intervalo cerrado [a,b].
    La fórmula básica es:
    I ≈ (b-a)/n * [f(a)/2 + ∑ i=1 n-1 f(a+i*h) + f(b)/2]
    """
    #Suma de los términos internos
    suma = 0.0
    for i in range(1, n):
        x_i = a + i * h
        suma += evaluar_expresion(funcion, {variable : x_i})

    #Se aplica la fórmula de Newton-Cotes cerrado
    integral : float= (h / 2) * (evaluar_expresion(funcion, {variable : a}) + 2 * suma + evaluar_expresion(funcion, {variable : b}))

    #Imprimir el resultado
    print(f"La aproximación de la integral con el método de Cotes-Cerrado: {integral}")

    return

"""Método de Newton-Cotes Abierto"""

def newton_cotes_abierto():

    #Se definen las variables para los límites de integración
    a : float = 0
    b : float = 0

    #Se ingresa la función y los límites de integración
    funcion : str = ingresar_funcion()
    a,b = limites_integracion()

    #Número máximo de iteraciones (profundidad de la tabla de Romberg)
    n : int = int(input("Introduce el número de subintervalos: "))

    #Se define la variable a integrar
    variable : str = input("Ingrese la variable por la cual se va a integrar: ")

    #Ancho de cada subintervalo
    h: float = (b - a) / (n + 2) 

    """
    Se utiliza una fórmula de interpolación polinómica basada en puntos internos
    La fórmula general es:
    I ≈ (b-a)/n * [1/(n+1) * ∑ i=1 n f(a+i*h)]
    """

    #Suma de los términos internos
    suma = 0.0
    for i in range(1, n + 1):
        x_i = a + i * h
        suma += evaluar_expresion(funcion, {variable : x_i})

    #Aplicar la fórmula de Newton-Cotes abierto
    integral : float = h * suma

    #Imprimir el resultado
    print(f"La aproximación de la integral con el método de Cotes-Abierto: {integral}")

    return

"""Función para repetir el programa"""

def continuar() -> int:

    #El usuario decide si desea repetir el programa
    opcion : int = int(input("¿Desea realizar otra aproximación? Marque 1 (Sí) o 2 (No): "))
    return opcion

#Inicia el programa
if  __name__ == "__main__":
    print("Calculadora de integrales definidas por métodos.")

    #Se define un ciclo while para repetir el programa tantas veces como el usuario desee
    while True:

        #Se elige el método de integración y se desarrolla la integral
        metodo()

        #El usuario decide si desea realizar otra integral
        opcion : int = continuar()

        #En caso de que no quiera
        if opcion == 2:
            break

        #En caso de que ingrese una opción no válida
        elif opcion != 1 and 2:
            print("SintaxError")
            break

# ! /\|=\/ 