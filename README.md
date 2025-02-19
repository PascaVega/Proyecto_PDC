# Calculadora de Integrales usando Métodos Numéricos

| Nombre                 | Identificación | Grupo | Trabajo          |
|------------------------|----------------|-------|------------------|
| Angélica Pascagaza Vega| 1031652163     |   5   | Trabajo individual |

## Índice

1. [Introducción](#Introducción)
2. [Conceptos Clave](#Conceptos-clave)
3. [Métodos numéricos](#Métodos-numéricos)
4. [Comparación de métodos](#Comparación-de-métodos)
5. [Procedimiento](#Procedimiento)
5. [Resultados](#Resultados)
6. [Conclusión](#Conclusión)
7. [Referencias](#Referencias)

## Introducción
En las aplicaciones prácticas de la integración se presentan situaciones que no tienen una solución analítica o directa de la integral. Por tal razón, son de gran utilidad los métodos numéricos de integración, los cuales permiten aproximar las integrales, haciendo posible resolver problemas que no son tratables de otro modo. Este proyecto tiene como objetivo facilitar la aplicación de estos métodos a través de un programa desarrollado en Python, el cual comprenda los métodos numéricos más utilizados a la hora de aproximar integrales definidas. 

## Conceptos clave
- **Función:** Relación matemática que asigna un valor de salida a cada valor de entrada.

- **Integral:** Representa el área bajo la curva de una función en un intervalo dado.

- **Puntos de evaluación:** Valores específicos en el dominio de la función donde se evalúa la función para aproximar la integral.
  
- **Pesos:** Coeficientes que se asignan a cada punto de evaluación para ponderar su contribución a la integral aproximada.
  
- **Métodos estadísticos:** En integración numérica se aplican para estimar el error y la precisión de las aproximaciones.
  
- **Extrapolación de Richardson:** Consiste en calcular la integral con diferentes tamaños de paso (distancia entre los puntos de evaluación) y luego combinar estos resultados para eliminar errores de orden inferior, obteniendo así una mejor estimación.
  
- **Polinomios de interpolación:** Se utilizan para aproximar una función mediante un polinomio que pasa por un conjunto de puntos conocidos.
  

## Métodos numéricos
1.	**Método del rectángulo (Regla del punto medio)**
   
Es una técnica básica de integración numérica en la que a partir del área de rectángulos se aproxima la integral de una función. Existen tres variaciones principales de este método: <i>regla del rectángulo izquierdo, regla del rectángulo derecho y regla del punto medio. </i> En esta ocasión únicamente se hace uso de la <b>regla del punto medio</b>, en donde se calcula la altura de los rectángulos a partir del valor de la función en el punto medio de cada subintervalo.

**Fórmula:**

$$\int_{a}^{b} f(x) \ dx \approx (b-a) \cdot f\left(\frac{a+b}{2}\right)$$

2.	**Método del Trapecio**

En esta técnica se aproxima la integral definida de la función dividiendo el área bajo la curva en trapecios, lo que proporciona una estimación más precisa.

**Fórmula:**

$$\int_{a}^{b} f(x) \ dx \approx \frac{b-a}{2} \left( f(a) + f(b) \right)$$

3.	**Método de Simpson**

En este método se utilizan parábola para aproximar la integral de una función definida, debido a que se logran obtener mejores aproximaciones usando segmentos curvos en vez de líneas rectas.

**Fórmula:**

$$\int_{a}^{b} f(x) \ dx \approx \frac{b-a}{6} \left( f(a) + 4f\left(\frac{a+b}{2}\right) + f(b) \right)$$

4.	**Método del Trapecio Compuesto**

Esta técnica aplica el método del trapecio en subintervalos más pequeños y suma los resultados, de tal manera que se mejora la precisión al dividir el intervalo en <i>n</i> subintervalos.

**Formula:**

$$\int_{a}^{b} f(x) \ dx \approx \frac{b-a}{2n} \left( f(a) + 2 \cdot \sum_{k=1}^{n-1} f\left(x_{k}\right) + f(b) \right)$$

5.	**Método de Simpson Compuesto**

Para esta aproximación se emplea la regla de Simpson en múltiples subintervalos del intervalo total, de esa manera se mejora la precisión.

**Formula:**

$$\int_{a}^{b} f(x) \ dx \approx \frac{b-a}{3n} \left( f(a) + 4 \sum_{k=1}^{n-1} f\left( x_{k} \right) + 2 \sum_{k=1}^{n-2} f\left(x_{k}\right) + f(b) \right)$$

6.	**Método del Trapecio Adaptativo**

Esta técnica ajusta dinámicamente el tamaño de los subintervalos en función del error estimado, empleando más subdivisiones donde la función varia más y reduciendo el número donde la función es más suave.

<b>Procedimiento:</b> Inicialmente se divide el intervalo inicial y se calcula el error. Luego, se evalúa si el error es mayor que un umbral dado, de serlo, se subdivide en más partes los intervalos con mayor error. Y este proceso se repite hasta que el error en cada subintervalo esté dentro del límite tolerado.

7.	**Método de Simpson Adaptativo**

Similar a la técnica anterior, se ajustan los subintervalos según el error estimado, pero se utiliza la regla de Simpson.

<b>Procedimiento:</b> Inicialmente se divide el intervalo inicial y se calcula el error. Luego, se evalúa si el error es mayor que un umbral dado, de serlo, se subdivide en más partes los intervalos con mayor error. Y este proceso se repite hasta que el error en cada subintervalo esté dentro del límite tolerado.

8.	**Cuadratura de Gauss-Legendre**

En este método se utilizan los puntos de evaluación y los pesos optimizados para maximizar la exactitud en los polinomios de grado dado. 

**Formula:**

$$\int_{a}^{b} f(x) \ dx \approx \frac{b-a}{2} \cdot \sum_{i=1}^{n} w_i \cdot f\left(\frac{b-a}{2} x_i + \frac{a+b}{2}\right)$$

9.	**Integración de Monte Carlo**

En esta técnica se utilizan métodos estadísticos para aproximar la integral definida (bastante útiles en espacios de alta dimensión). Este consiste en la generación de números aleatorios para estimar el valor medio de la función.

<b>Procedimiento:</b> Primero se generan un grupo de puntos aleatorios en el dominio de la función y se evalúa la función en ellos. Luego se calcula la media de esas evaluaciones y se multiplica por el volumen del dominio.

10.	**Integración de Romberg**

Es un método de refinamiento que combina el <i>método del trapecio</i> con la <i>extrapolación de Richardson </i> para mejorar la precisión.

<b>Procedimiento:</b> Se inicia con el método del Trapecio Compuesto para después aplicar la extrapolación de Richardson repetidamente, con el fin de obtener estimaciones de orden superior de la integral.

11.	**Método de Newton-Cotes Cerrado**

Se utilizan polinomios de interpolación construidos a partir de puntos de evaluación equiespaciados que incluyen los extremos del intervalo.

12.	**Método de Newton-Cotes Abierto**

Esta técnica también utiliza polinomios de interpolación, pero los puntos de evaluación no incluyen los extremos del intervalo.


## Comparación de métodos
Cada método tiene sus propias aplicaciones y es adecuado para diferentes tipos de problemas de integración.

<table cellspacing="1" bgcolor="">
  <tr bgcolor="#252582">
    <th><b>Método</b></th>
    <th><b>Precisión</b></th>
    <th><b>Complejidad Computacional</b></th>
    <th><b>Facilidad de Implementación</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Método del Rectángulo</td>
    <td style="color:#141414" align="center">Baja</td>
    <td style="color:#141414" align="center">Baja</td>
    <td style="color:#141414" align="center">Alta</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Método del Trapecio</td>
    <td style="color:#141414" align="center">Moderada</td>
    <td style="color:#141414" align="center">Moderada</td>
    <td style="color:#141414" align="center">Moderada</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Método del Simpson</td>
    <td style="color:#141414" align="center">Alta</td>
    <td style="color:#141414" align="center">Moderada</td>
    <td style="color:#141414" align="center">Moderada</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Método del Trapecio Compuesto</td>
    <td style="color:#141414" align="center">Alta</td>
    <td style="color:#141414" align="center">Alta</td>
    <td style="color:#141414" align="center">Moderada</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Método de Simpson Compuesto</td>
    <td style="color:#141414" align="center">Muy alta</td>
    <td style="color:#141414" align="center">Alta</td>
    <td style="color:#141414" align="center">Moderada</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Método del Trapecio Adaptativo</td>
    <td style="color:#141414" align="center">Alta</td>
    <td style="color:#141414" align="center">Alta (adaptativo)</td>
    <td style="color:#141414" align="center">Moderada</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Método de Simpson Adaptativo</td>
    <td style="color:#141414" align="center">Muy alta</td>
    <td style="color:#141414" align="center">Alta (adaptativo)</td>
    <td style="color:#141414" align="center">Moderada</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Cuadratura de Gauss-Legendre</td>
    <td style="color:#141414" align="center">Muy alta</td>
    <td style="color:#141414" align="center">Alta</td>
    <td style="color:#141414" align="center">Baja</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Integración de Monte Carlo</td>
    <td style="color:#141414" align="center">Alta (con suficientes muestras)</td>
    <td style="color:#141414" align="center">Baja (para gran número de muestras)</td>
    <td style="color:#141414" align="center">Baja</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Integración de Romberg</td>
    <td style="color:#141414" align="center">Muy alta</td>
    <td style="color:#141414" align="center">Alta</td>
    <td style="color:#141414" align="center">Moderada</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Método de Newton-Cotes Cerrado</td>
    <td style="color:#141414" align="center">Moderada a Alta</td>
    <td style="color:#141414" align="center">Moderada</td>
    <td style="color:#141414" align="center">Moderada</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Método de Newton-Cotes Abierto</td>
    <td style="color:#141414" align="center">Moderada</td>
    <td style="color:#141414" align="center">Moderada</td>
    <td style="color:#141414" align="center">Moderada</td>
  </tr>
</table>


## Procedimiento
En esta sección se encontrarán los diagramas de flujo preliminares y finalmente cómo se construyó en Python.

### Diagrama de Flujo del Programa General
```mermaid
flowchart TD;
    A[Inicio] 
    A --> B[Seleccione el método]
    B --> C[Ingrese la Función]
    C --> D[Se convierte la función a Notación Polaca Inversa]
    D --> E[Se ingresan los límites de integración y otros valores especificos requeridos en el método]
    E --> F[Se aplica el método]
    F --> G[Se imprime el resultado]
    G --> H{Se pregunta al usuario si desea realizar otra aproximación}
    H -->|Sí| B
    H -->|No| I[Fin]
```

### Método del rectángulo (Regla del punto medio)

```python
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

    #Tiempo inicial
    tiempo_inicial = time.time()

    base : float = b-a
    x_funcion : float = (a+b)/2

    #Se define un diccionario para evaluar la variable en la función
    variables = {variable : x_funcion}
    altura : float = evaluar_expresion(funcion, variables)
    resultado : float = base*altura

    #Se imprime el resultado
    print(f"Por el método del Réctangulo Simple, el resultado es {resultado}")
    
    #Tiempo final
    tiempo_final = time.time()

    #Calcular el tiempo de ejecución
    duracion = tiempo_final - tiempo_inicial

    #Mostrar el tiempo de ejecución en segundos
    print(f"El método del rectángulo se ejecutó en {duracion:.6f} segundos.")

    return
```

```mermaid
flowchart TD;
    A[Método del Rectángulo] 
    A --> B[Base = Limite superior - Limite inferior]
    B --> C[X_función = Limite superior + Limite inferior]
    C --> D[Altura = función de X_función]
    D --> E[Se obtiene la multiplicación a partir del producto de las variables Base y Altura]
    E --> F[Se imprime el resultado]
    F --> G[Fin]
```

### Método del Trapecio Simple

```python
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

    #Tiempo inicial
    tiempo_inicial = time.time()

    base : float = (b-a)/2

    #Se define un diccionario para evaluar la variable en la función
    funcion_a = {variable : a}
    funcion_b = {variable : b}
    resultado_a : float = evaluar_expresion(funcion, funcion_a)
    resultado_b : float = evaluar_expresion(funcion, funcion_b)
    resultado : float = base*(resultado_a+resultado_b)

    #Se imprime el resultado
    print(f"Por el método del Trapecio Simple, el resultado es {resultado}")

    #Tiempo final
    tiempo_final = time.time()

    #Calcular el tiempo de ejecución
    duracion = tiempo_final - tiempo_inicial

    #Mostrar el tiempo de ejecución en segundos
    print(f"El método del trapecio simple se ejecutó en {duracion:.6f} segundos.")

    return
```

```mermaid
flowchart TD;
    A[Método del Trapecio Simple] 
    A --> B[Base = Limite superior - Limite inferior]
    B --> C[Base = Base/2]
    C --> D[Altura = función de Limite superior + función de Limite inferior]
    D --> E[Se obtiene la multiplicación a partir del producto de las variables Base y Altura]
    E --> F[Se imprime el resultado]
    F --> G[Fin]
```

### Método de Simpson Simple

```python
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

    #Tiempo inicial
    tiempo_inicial = time.time()

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
    print(f"Por el método de Simpson Simple, el resultado es {resultado}")

    #Tiempo final
    tiempo_final = time.time()

    #Calcular el tiempo de ejecución
    duracion = tiempo_final - tiempo_inicial

    #Mostrar el tiempo de ejecución en segundos
    print(f"El método de Simpson simple se ejecutó en {duracion:.6f} segundos.")

    return
```

```mermaid
flowchart TD;
    A[Método de Simpson Simple] 
    A --> B[Base = Limite superior - Limite inferior]
    B --> C[Base = Base/6]
    C --> D[Altura = función de Limite superior + función de Limite inferior]
    D --> E[Altura = Altura + 4 * función del promedio de los límites]
    E --> F[Se obtiene la multiplicación a partir del producto de las variables Base y Altura]
    F --> G[Se imprime el resultado]
    G --> H[Fin]
```

### Método del Trapecio Compuesto

```python
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

    #Tiempo inicial
    tiempo_inicial = time.time()

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

    #Tiempo final
    tiempo_final = time.time()

    #Calcular el tiempo de ejecución
    duracion = tiempo_final - tiempo_inicial

    #Mostrar el tiempo de ejecución en segundos
    print(f"El método del trapecio compuesto se ejecutó en {duracion:.6f} segundos.")

    return
```

```mermaid
flowchart TD;
    A[Método del Trapecio Compuesto] 
    A --> B[n = número de intervalos]
    B --> C[h = b-a]
    C --> D[h = h/n]
    D --> E[Se suman las imágenes de los limites junto con el resultado de la sumatoria]
    E --> F[Se multiplica la suma por h/2]
    F --> G[Se imprime el resultado]
    G --> H[Fin]
```

### Método de Simpson Compuesto

```python
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

    #Tiempo inicial
    tiempo_inicial = time.time()

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

    #Tiempo final
    tiempo_final = time.time()

    #Calcular el tiempo de ejecución
    duracion = tiempo_final - tiempo_inicial

    #Mostrar el tiempo de ejecución en segundos
    print(f"El método de simpson compuesto se ejecutó en {duracion:.6f} segundos.")

    return
```

```mermaid
flowchart TD;
    A[Método de Simpson Compuesto] 
    A --> B[n = número de intervalos que debe ser par]
    B --> C[h = b-a]
    C --> D[h = h/n]
    D --> E[Se suman las imágenes de los limites junto con los resultado de las sumatorias]
    E --> F[Se multiplica la suma por h/3]
    F --> G[Se imprime el resultado]
    G --> H[Fin]
```

### Método del Trapecio Adaptativo

```python
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

    #Tiempo inicial
    tiempo_inicial = time.time()

    resultado : float = trapecio_adaptativo_funcion(funcion, a, b, variable, tol)

    #Se imprime el resultado
    print(f"Por el método del Trapecio Adaptativo, el resultado es {resultado}")

    #Tiempo final
    tiempo_final = time.time()

    #Calcular el tiempo de ejecución
    duracion = tiempo_final - tiempo_inicial

    #Mostrar el tiempo de ejecución en segundos
    print(f"El método del trapecio adaptativo se ejecutó en {duracion:.6f} segundos.")

    return
```

```mermaid
flowchart TD;
    A[Método del Trapecio Adaptativo] 
    A --> B[tol = tolerancia]
    B --> C[Función del trapecio adaptativo]
    C --> D[medio = a + b]
    D --> E[medio = medio /2]
    E --> F[t1 = aproximación del intervalo completo]
    F --> G[t2 = suma de las aproximaciones de las integrales de los subintervalos]
    G --> I[comparar = valor absoluto de t2 - t1]
    I --> J{comparar < tol}
    J --> |Si| K[Imprimir t2]
    J --> |No| C
    K --> L[Fin]
```

### Método de Simpson Adaptativo

```python
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

    #Tiempo inicial
    tiempo_inicial = time.time()

    resultado : float  = simpson_adaptativo_funcion(funcion, a, b, variable, tol)

    #Se imprime el resultado
    print(f"Por el método del Simpson Adaptativo, el resultado es {resultado}")

    #Tiempo final
    tiempo_final = time.time()

    #Calcular el tiempo de ejecución
    duracion = tiempo_final - tiempo_inicial

    #Mostrar el tiempo de ejecución en segundos
    print(f"El método de simpson adaptativo se ejecutó en {duracion:.6f} segundos.")

    return
```

```mermaid
flowchart TD;
    A[Método de Simpson Adaptativo] 
    A --> B[tol = tolerancia]
    B --> C[Función de Simpson adaptativo]
    C --> D[medio = a + b]
    D --> E[medio = medio /2]
    E --> F[s1 = aproximación del intervalo completo]
    F --> G[s2 = suma de las aproximaciones de las integrales de los subintervalos]
    G --> I[comparar = valor absoluto de s2 - s1]
    I --> J{comparar < 15 * tol}
    J --> |Si| K[Imprimir 2*s2/15 - s1/15]
    J --> |No| M[tol = tol/2]
    M --> N[Integral izquierda = ]
    M --> O[Integral derecha = ]
    N --> C
    O --> C
    N --> P[Imprimi la suma de las integrales por derecha e izquierda]
    O --> P
    K --> L[Fin]
```

### Método de Cuadratura de Gauss-Legendre

```python
def Gauss_Legendre():

    #Se definen las variables para los límites de integración
    a : float = 0
    b : float = 0

    #Se ingresa la función y los límites de integración
    funcion : str = ingresar_funcion()
    a,b = limites_integracion()

    #Número de puntos de Gauss-Legendre
    n : int = int(input("Introduce el número de puntos para la cuadratura de Gauss-Legendre: "))

    #Tiempo inicial
    tiempo_inicial = time.time()

    #Calcular la integral utilizando la cuadratura de Gauss-Legendre
    resultado : float = cuadratura_gauss_legendre(funcion, a, b, n)

    #Imprimir el resultado
    print(f"La aproximación de la integral utilizando la cuadratura de Gauss-Legendre es: {resultado}")

    #Tiempo final
    tiempo_final = time.time()

    #Calcular el tiempo de ejecución
    duracion = tiempo_final - tiempo_inicial

    #Mostrar el tiempo de ejecución en segundos
    print(f"El método de la cuadratura de Gauss Legendre se ejecutó en {duracion:.6f} segundos.")

    return
```

```mermaid
flowchart TD;
    A[Método de la Cuadratura de Gauss-Legendre] 
    A --> B[n = número de puntos de la cuadratura]
    B --> C[Se obtiene los nodos y pesos a través del método Newton-Raphson]
    C --> D[x = coordenadas en el intervalo a,b]
    D --> E[Se evalua la integral]
    E --> F[Se imprime la integral]
    F --> H[Fin]
```

### Método de Monte Carlo

```python
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

    #Tiempo inicial
    tiempo_inicial = time.time()

    #Calcular la integral utilizando el método de Monte Carlo
    resultado : float = monte_Carlo_funcion(funcion, a, b, n)

    #Imprimir el resultado
    print(f"La aproximación de la integral con el método de Monte Carlo: {resultado}")

    #Tiempo final
    tiempo_final = time.time()

    #Calcular el tiempo de ejecución
    duracion = tiempo_final - tiempo_inicial

    #Mostrar el tiempo de ejecución en segundos
    print(f"El método de monte carlo se ejecutó en {duracion:.6f} segundos.")

    return
```

```mermaid
flowchart TD;
    A[Método de Monte Carlo] 
    A --> B[n = número de puntos de la muestra]
    B --> C[Se obtienen los puntos aleatorios de manera uniforme]
    C --> D[Se evaluan los puntos en la función]
    D --> E[Se obtiene la aproximación]
    E --> F[Se imprime la integral]
    F --> H[Fin]
```

### Método de Romberg

```python
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

    #Tiempo inicial
    tiempo_inicial = time.time()

    #Calcular la integral utilizando el método Romberg
    resultado = romberg_funcion(funcion, a, b, max_iter)

    #Mostrar la tabla de Romberg
    print("Tabla de Romberg:")
    for i in range(len(resultado)):
        for j in range(i + 1):
            print(f"resultado[{i}][{j}] = {resultado[i][j]:.10f}", end="  ")
    
    #Tiempo final
    tiempo_final = time.time()

    #Calcular el tiempo de ejecución
    duracion = tiempo_final - tiempo_inicial

    #Mostrar el tiempo de ejecución en segundos
    print(f"El método de Romberg se ejecutó en {duracion:.6f} segundos.")

    return
```

```mermaid
flowchart TD;
    A[Método de Romberg] 
    A --> B[max_iter = número máximo de iteraciones]
    B --> C[Se obtienen los puntos aleatorios de manera uniforme]
    C --> D[Se crea una matriz]
    D --> E[Se obtienen las aproximaciones iniciales con la regla del trapezoide]
    E --> F[Se pulen las aproximaciones con la extrapolación de Richardson]
    F --> H[Se imprime la matriz]
    H --> I[Fin]

```

### Método de Newton Cotes-Cerrado

```python
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

    #Tiempo inicial
    tiempo_inicial = time.time()

    #Suma de los términos internos
    suma = 0.0
    for i in range(1, n):
        x_i = a + i * h
        suma += evaluar_expresion(funcion, {variable : x_i})

    #Se aplica la fórmula de Newton-Cotes cerrado
    integral : float= (h / 2) * (evaluar_expresion(funcion, {variable : a}) + 2 * suma + evaluar_expresion(funcion, {variable : b}))

    #Imprimir el resultado
    print(f"La aproximación de la integral con el método de Cotes-Cerrado: {integral}")

    #Tiempo final
    tiempo_final = time.time()

    #Calcular el tiempo de ejecución
    duracion = tiempo_final - tiempo_inicial

    #Mostrar el tiempo de ejecución en segundos
    print(f"El método de Newton Cotes-cerrado se ejecutó en {duracion:.6f} segundos.")

    return
```

```mermaid
flowchart TD;
    A[Método de Newton Cotes-Cerrado] 
    A --> B[n = número de subintervalos]
    B --> C[h = ancho de cada subintervalo]
    C --> D[suma = suma de los terminos internos]
    D --> E[Se obtiene la aproximación usando la fórmula de Newton-Cotes cerrado]
    E --> H[Se imprime la aproximación]
    H --> I[Fin]
```

### Método de Newton-Cotes Abierto

```python
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

    #Tiempo inicial
    tiempo_inicial = time.time()

    #Suma de los términos internos
    suma = 0.0
    for i in range(1, n + 1):
        x_i = a + i * h
        suma += evaluar_expresion(funcion, {variable : x_i})

    #Aplicar la fórmula de Newton-Cotes abierto
    integral : float = h * suma

    #Imprimir el resultado
    print(f"La aproximación de la integral con el método de Cotes-Abierto: {integral}")

    #Tiempo final
    tiempo_final = time.time()

    #Calcular el tiempo de ejecución
    duracion = tiempo_final - tiempo_inicial

    #Mostrar el tiempo de ejecución en segundos
    print(f"El método de Newton Cotes-abierto se ejecutó en {duracion:.6f} segundos.")

    return
```

```mermaid
flowchart TD;
    A[Método de Newton Cotes-Abierto] 
    A --> B[n = número de subintervalos]
    B --> C[h = ancho de cada subintervalo]
    C --> D[suma = suma de los terminos internos]
    D --> E[Se obtiene la aproximación usando la fórmula de Newton-Cotes abierto]
    E --> H[Se imprime la aproximación]
    H --> I[Fin]
```


## Resultados
Para evaluar la exactitud de los métodos, se planteó la siguiente integral y se obtuvieron las aproximaciones con todos los métodos

$$
\int_{18}^{30} \left( x^3 + \sin(2x) - 2x^2 + 15 \right)
$$

Al resolver la integral mediante sustitución de variable, esta da como resultado:

$$
\int_{18}^{30} \left( x^3 + \sin(2x) - 2x^2 + 15 \right) \approx 162323,68601815
$$

Para cada método de aproximo la integral, y teniendo en cuenta que el valor real de la función es 162323.6860, se calcula el error relativo.

$$
\text{Error Relativo} = \frac{|V_r - V_a|}{|V_r|} \times 100\\%
$$

1. Método del Rectángulo (Regla del punto medio)

[![M-todo-del-Rect-ngulo.png](https://i.postimg.cc/tT04wt33/M-todo-del-Rect-ngulo.png)](https://postimg.cc/3yBhDGbN)

$$
\text{Error Relativo} = \frac{|162323.6860 - 152234.7809|}{|162323.6860|} * 100\\% \approx 6.2115\\%
$$

2. Método del Trapecio Simple

[![M-todo-del-Trapecio-Simple.png](https://i.postimg.cc/tJkRsKLk/M-todo-del-Trapecio-Simple.png)](https://postimg.cc/YL4BVs2L)

$$
\text{Error Relativo} = \frac{|162323.6860 - 182476.2204|}{|162323.6860|} * 100\\% \approx 12.4150\\%
$$

3. Método de Simpson Simple

[![M-todo-de-Simpson-Simple.png](https://i.postimg.cc/Kv9vxy7v/M-todo-de-Simpson-Simple.png)](https://postimg.cc/jL7r4mkG)

$$
\text{Error Relativo} = \frac{|162323.6860 - 162315.2607|}{|162323.6860|} * 100\\% \approx 0.0051\\%
$$

4. Método del Trapecio Compuesto

[![M-todo-del-Trapecio-Compuesto.png](https://i.postimg.cc/qvSJ6XZP/M-todo-del-Trapecio-Compuesto.png)](https://postimg.cc/fV7n6XsC)

$$
\text{Error Relativo} = \frac{|162323.6860 - 162326.4262|}{|162323.6860|} * 100\\% \approx 0.0016\\%
$$

5. Método de Simpson Compuesto

[![M-todo-de-Simpson-Compuesto.png](https://i.postimg.cc/bJHpMXNP/M-todo-de-Simpson-Compuesto.png)](https://postimg.cc/WF3BFHkY)

$$
\text{Error Relativo} = \frac{|162323.6860 - 162324.4122|}{|162323.6860|} * 100\\% \approx 0.0004\\%
$$

6. Método del Trapecio Adaptativo

[![M-odo-del-Trapecio-Adaptativo.png](https://i.postimg.cc/v8hGtdNL/M-odo-del-Trapecio-Adaptativo.png)](https://postimg.cc/Bt8WJRsX)

$$
\text{Error Relativo} = \frac{|162323.6860 - 162324.6386|}{|162323.6860|} * 100\\% \approx 0.0005\\%
$$

7. Método de Simpson Adaptativo

[![M-todo-de-Simpson-Adaptativo.png](https://i.postimg.cc/jdkKB4KD/M-todo-de-Simpson-Adaptativo.png)](https://postimg.cc/JGJ9kJs8)

$$
\text{Error Relativo} = \frac{|162323.6860 - 162315.2659|}{|162323.6860|} * 100\\% \approx 0.0051\\%
$$

8. Cuadratura de Gauss-Legendre

[![M-todo-de-la-Cuadratura-de-Gauss-Legendre.png](https://i.postimg.cc/7ZF4ZP5D/M-todo-de-la-Cuadratura-de-Gauss-Legendre.png)](https://postimg.cc/Xrkm2bKD)

$$
\text{Error Relativo} = \frac{|162323.6860 - 162324.4122|}{|162323.6860|} * 100\\% \approx 0.0004\\%
$$

9. Integración de Monte Carlo

[![M-todo-de-Monte-Carlo.png](https://i.postimg.cc/CKbgBy88/M-todo-de-Monte-Carlo.png)](https://postimg.cc/sBf8qNwf)

$$
\text{Error Relativo} = \frac{|162323.6860 - 164685.2860|}{|162323.6860|} * 100\\% \approx 0.0145\\%
$$

10. Integración de Romberg

[![M-todo-de-Romberg.png](https://i.postimg.cc/PJ5sRPRb/M-todo-de-Romberg.png)](https://postimg.cc/9RKn4FVz)

$$
\text{Error Relativo} = \frac{|162323.6860 - 162324.4122|}{|162323.6860|} * 100\\% \approx 0.0004\\%
$$

11. Método de Newton-Cotes Cerrado

[![M-todo-de-Newton-Cotes-Cerrado.png](https://i.postimg.cc/VLTQKsBM/M-todo-de-Newton-Cotes-Cerrado.png)](https://postimg.cc/crQbHSz4)

$$
\text{Error Relativo} = \frac{|162323.6860 - 162326.4262|}{|162323.6860|} * 100\\% \approx 0.0016\\%
$$

12. Método de Newton-Cotes Abierto

[![M-todo-de-Newton-Cotes-Abierto.png](https://i.postimg.cc/y8ZqtqvG/M-todo-de-Newton-Cotes-Abierto.png)](https://postimg.cc/gxmBL79y)

$$
\text{Error Relativo} = \frac{|162323.6860 - 157606.4698|}{|162323.6860|} * 100\\% \approx 2.9060\\%
$$

## Conclusiones
El desarrollo de este proyecto no solo cumplió la función de afianzar los conocimientos obtenido durante el curso, sino que también ha dado una gran perfectiva sobre algunos de los métodos numéricos. Este programa permite comparar los métodos numéricos a través de su presión y eficiencia de diferentes técnicas de integración, adaptándose a distintas características de las funciones a integrar.

Este programa ha dejado en evidencia que la selección del método depende de la función específica, además de que las aproximaciones dependen del intervalo de integración y la precisión requerida. No obstante, el tiempo de ejecución que tarda el programa con cada método depende de su precisión, por lo cual aquellos que se tarden más darán una mejor aproximación. De esa manera, los métodos compuestos y adaptativos generalmente son superiores en términos de precisión y tiempo, mientras que métodos como Monte Carlo y Gauss-Legendre ofrecen ventajas en situaciones especiales.

Para concluir, el desarrollo y aplicación de este proyecto ha llevado a solidificar los cocimientos ya adquiridos. Al tiempo que se realizaba una tarea interdisciplinar en la que se lograron evaluar distintos aspectos de las integrales, tales que ayudaron a comprender con precisión las diferencias entre los métodos y cuál es más ventajoso en determinada situación.


## Bibiografía
1. Burden, R. L., & Faires, J. D. (2011). **Numerical Analysis** (9th ed.). Brooks/Cole. (Método del rectángulo)

2. Chapra, S. C., & Canale, R. P. (2015). **Numerical Methods for Engineers** (7th ed.). McGraw-Hill Education. (Método del Trapecio)

3. Kiusalaas, J. (2013). **Numerical Methods in Engineering with Python 3**. Cambridge University Press. (Método de Simpson)

4. Atkinson, K. E. (1989). **An Introduction to Numerical Analysis** (2nd ed.). John Wiley & Sons. (Método del Trapecio Compuesto)

5. Burden, R. L., & Faires, J. D. (2011). **Numerical Analysis** (9th ed.). Brooks/Cole. (Método de Simpson Compuesto)

6. Press, W. H., Teukolsky, S. A., Vetterling, W. T., & Flannery, B. P. (2007). **Numerical Recipes: The Art of Scientific Computing** (3rd ed.). Cambridge University Press. (Método del Trapecio Adaptativo)

7. Press, W. H., Teukolsky, S. A., Vetterling, W. T., & Flannery, B. P. (2007). **Numerical Recipes: The Art of Scientific Computing** (3rd ed.). Cambridge University Press. (Método de Simpson Adaptativo)

8. Hamming, R. W. (1973). **Numerical Methods for Scientists and Engineers** (2nd ed.). Dover Publications. (Cuadratura de Gauss-Legendre)

9. Metropolis, N., & Ulam, S. (1949). The Monte Carlo Method. *Journal of the American Statistical Association, 44*(247), 335-341. (Integración de Monte Carlo)

10. Stoer, J., & Bulirsch, R. (2002). **Introduction to Numerical Analysis** (3rd ed.). Springer. (Integración de Romberg)

11. Davis, P. J., & Rabinowitz, P. (1984). **Methods of Numerical Integration** (2nd ed.). Academic Press. (Método de Newton-Cotes Cerrado)

12. Davis, P. J., & Rabinowitz, P. (1984). **Methods of Numerical Integration** (2nd ed.). Academic Press. (Método de Newton-Cotes Abierto)

