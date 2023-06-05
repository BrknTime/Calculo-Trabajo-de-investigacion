from scipy import integrate

# Aqui ponemos funcion que queremmos integrar
def func(x):
    return x**2 
# Aqui colocamos los limites de integracion
a = 0
b = 2

# Aca se calcula el resultado de la integral
resultado, _ = integrate.quad(func, a, b)

# Con el round podemos redondear el resultado 
resultado_redondeado = round(resultado, 2)

# Imprimir el resultado en la terminal
print("El resultado de la integral dada es:", resultado_redondeado)
