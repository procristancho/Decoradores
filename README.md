# Decoradores
En este repositorio comparto una serie de tutoriales sobre decoradores con Python. Aquí podrás encontrar explicaciones sencillas y ejemplos prácticos sobre este tema. Mi objetivo es ofrecer una referencia rápida y útil para quienes deseen profundizar en estos temas.

Los decoradores son una característica poderosa y muy versátil en Python, los decoradores permiten modificar el comportamiento de funciones o métodos de manera elegante y
reutilizable. En esencia un decorador es una función que toma otra función como argumento y devuelve una nueva función con funcionalidad añadida.

# Código del archivo saludar.py
El archivo 'saludar.py' contiene un ejemplo básico de un decorador. aqui esta el código:
```python
def decorador(func):
    def envolver():
        print('Something before the function to be decorated')
        func()
        print('Something after the function to be decorated')
    
    return envolver


@decorador
def saludar():
    print('\nHello everybody here!!\n')

saludar()
```

## Explicación del Código
1. Definición del Decorador (decorador()):
     - **decorador** es una función que toma otra función func como argumento.
     - Dentro de decorador, se define una función interna llamada envolver que imprime un mensaje antes y después de llamar a func.
     - La función envolver se devuelve como el resultado del decorador.
2. Uso del Decorador:

    - El decorador @decorador se aplica a la función saludar.
    - Cuando se llama a saludar(), en realidad se está llamando a envolver que ha sido retornada por el decorador.
    - Esto imprime los mensajes definidos en envolver antes y después de ejecutar la función saludar.
  
## Como ejecutar el código
1. **Clona el repositorio :** si aún no tienes el repositorio, clónalo con el siguiente comando:
```
git clone https://github.com/procristancho/Decoradores.git

```
2. **Ejecuta el archivo :** Navega al directorio del proyecto y ejecuta el archivo 'saludar.py'
```bash
cd Decoradores
ptyhon saludar.py
```
3. **Resultado esperado :** Al ejecutar el archivo, deberías ver las siguiente salida:
```
Something before the function to be decorated

Hello everybody here!!

Something after the function to be decorated
```
## Requisitos
- Python 3.x
  
## Licencia
Este proyecto está licenciado bajo la Licencia MIT. 


# Código del archivo obsoleto.py
Este repositorio contiene un ejemplo de cómo crear y utilizar un decorador en Python para marcar una función como obsoleta. 
```python
import warnings
from functools import wraps

def obsoleto(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        warnings.warn(f"La función {func.__name__} está obsoleta y será removida en el futuro", 
                      category=DeprecationWarning, stacklevel=2)
        return func(*args, **kwargs)
    return wrapper

@obsoleto
def vieja_funcion():
    print("Esta es una función obsoleta destinada a ser removida")

vieja_funcion()

```

## Contenido
- **obsoleto(func) :** Un decorador que emite una advertencia de obsolescencia.
- **@wraps(func):** Este es otro decorador que preserva la información original de la función decorada (como su nombre y docstring), lo cual es útil para mantener la documentación y otras propiedades de la función intactas.
- **warnings.warn:** Esta función genera una advertencia. En este caso, se utiliza DeprecationWarning para indicar que la función está obsoleta.
- **stacklevel=2:** Esto ajusta la advertencia para que apunte a la línea donde se llamó a la función obsoleta, en lugar de dentro del decorador, lo que facilita a los desarrolladores identificar dónde se está utilizando la función.
- **vieja_funcion():** Una función marcada como obsoleta utilizando el decorador obsoleto.

## Salida Esperada
Cuando se ejecuta el código anterior, se obtendrá la siguiente salida:
```
<path_to_file>: La función vieja_funcion está obsoleta y será removida en el futuro
Esta es una función obsoleta destinada a ser removida
```
## Requisitos
- Python 3.x

## Instalación
```bash
git clone https://github.com/procristancho/Decoradores.git
cd Decoradores
python obsoleto.py

```
## Licencia
Este proyecto está licenciado bajo la Licencia MIT. 


# Código del archivo rate_limiting.py

Este código implementa un **limitador de tasa** simple en python, utilizando decoradores. El limitador de tasa es útil para controlar la frecuencia con la que se puede llamar a una función. La idea es evitar que una función sea ejecutada más de un cierto número de veces en un periodo de tiempo determinado

## Contenido y explicación del código
```python
import time
from functools import wraps
```
- **import time:** Importa el módulo time, que se usa para manejar funciones relacionadas con el tiempo, como obtener la hora actual (time.time()) y poner a dormir el programa (time.sleep()).
- f**rom functools import wraps:** Importa la función wraps del módulo functools. Esta se usa para preservar la metadata de la función original cuando se utiliza un decorador.

```python
def limitador_de_tasa(calls_per_period, period):
```
- Define la función limitador_de_tasa, que actúa como un decorador. Toma dos parámetros:
    - calls_per_period: El número de veces que la función decorada puede ser llamada en el intervalo de tiempo especificado.
    - period: El intervalo de tiempo en segundos durante el cual se permite calls_per_period llamadas.

```python
    def decorator(func):
        last_called = [0]
```

- Define una función interna llamada decorator que toma como argumento la función que se desea limitar (func). La variable last_called se usa para rastrear la última vez que la función fue llamada. Se almacena en una lista para que pueda ser modificada dentro del wrapper (las listas son mutables).

```python
        @wraps(func)
        def wrapper(*args, **kwargs):
```
- **@wraps(func):** Esto asegura que el decorador no altere los atributos de la función original como su nombre o su docstring.
- def wrapper(*args, **kwargs): Define la función wrapper, que será la versión decorada de la función original. Esta puede aceptar cualquier número de argumentos posicionales (*args) y argumentos con nombre (**kwargs).

```python
            elapsed = time.time() - last_called[0]
```
- Calcula el tiempo que ha pasado desde la última vez que se llamó a la función (elapsed). Esto se hace restando el valor en last_called[0] de la hora actual (time.time()).



```python
            if elapsed < period / calls_per_period:
                time.sleep(period / calls_per_period - elapsed)
```

- Si el tiempo transcurrido (elapsed) es menor que el intervalo permitido entre llamadas (calculado como period / calls_per_period), la ejecución se suspende (time.sleep) por la diferencia de tiempo necesaria para respetar el límite de llamadas.

```python
            result = func(*args, **kwargs)
            last_called[0] = time.time()
            return result
```
- La función original (func) se llama y su resultado se almacena en result.
- Se actualiza last_called[0] con la hora actual para registrar la última vez que la función fue llamada.
- Finalmente, se retorna el resultado de la función original.

```python
    return decorator
```
- Se retorna la función decorator desde limitador_de_tasa, lo que permite que sea utilizada como un decorador.

### Ejemplo de Uso

```python
@limitador_de_tasa(5, 10)  # 5 llamadas cada 10 segundos
def hacer_pedido():
    print("Pedido realizado")

for _ in range(10):
    hacer_pedido()
```
En este ejemplo, la función hacer_pedido solo podrá ser ejecutada 5 veces cada 10 segundos. Aunque el bucle intenta hacer 10 llamadas consecutivas, el decorador limita la frecuencia de las ejecuciones para cumplir con la restricción de tasa.

### Cómo funciona
- El decorador limitador_de_tasa utiliza el módulo time para rastrear el tiempo transcurrido desde la última llamada a la función.
- Si la función es llamada más frecuentemente de lo permitido, el decorador suspende la ejecución hasta que se cumpla el intervalo de tiempo necesario.
- Esto es útil en situaciones donde se necesita regular la frecuencia de las solicitudes, como al hacer peticiones a una API externa.

### Requisitos
- Python 3.x

### Instalación
```bash
git clone https://github.com/procristancho/Decoradores.git
cd Decoradores
python rate_limiting.py
```
## Licencia
Este proyecto está licenciado bajo la Licencia MIT. 


