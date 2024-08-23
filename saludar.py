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