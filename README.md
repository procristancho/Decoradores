# Decoradores
En este repositorio comparto una serie de tutoriales sobre decoradores con Python. Aquí podrás encontrar explicaciones sencillas y ejemplos prácticos sobre este tema. Mi objetivo es ofrecer una referencia rápida y útil para quienes deseen profundizar en estos temas.

Los decoradores son una característica poderosa y muy versátil en Python, los decoradores permiten modificar el comportamiento de funciones o métodos de manera elegante y
reutilizable. En esencia un decorador es una función que toma otra función como argumento y devuelve una nueva función con funcionalidad añadida.

# Código del archivo saludar.py
El archivo 'saludar.py' contiene un ejemplo básico de un decorador. aqui esta el código:
```
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
```
ptyhon saludar.py
```
3. **Resultado esperado : **Al ejecutar el archivo, deberías ver las siguiente salida:
```

Something before the function to be decorated

Hello everybody here!!

Something after the function to be decorated

```
   ## Licencia
   Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo 'LICENSE' para más detalles.


# Código del archivo obsoleto.py
Este repositorio contiene un ejemplo de cómo crear y utilizar un decorador en Python para marcar una función como obsoleta. 
```
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

## Ejecución
```
git clone https://github.com/procristancho/Decoradores.git
cd Decoradores
python obsoleto.py

```
## Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
