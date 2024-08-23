import time
from functools import wraps

def limitador_de_tasa(calls_per_period, period):
    def decorator(func):
        last_called = [0]

        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            if elapsed < period / calls_per_period:
                time.sleep(period / calls_per_period - elapsed)
            result = func(*args, **kwargs)
            last_called[0] = time.time()
            return result
        return wrapper
    return decorator

@limitador_de_tasa(5, 10)  # 5 llamadas cada 10 segundos
def hacer_pedido():
    print(f"Pedido realizado {time.strftime('%H:%M:%S')}")

start_time = time.time()
for _ in range(11):
    hacer_pedido()
end_time = time.time()

total_time = end_time - start_time
print(f"Tiempo total: {total_time:.2f} segundos")
