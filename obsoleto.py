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