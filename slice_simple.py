def slice_simple():
    texto = "Awesome"
    # Código a implementar, se debe utilizar la variable 'texto' para resolver el ejercicio.
    # No se debe modificar la definición de la función, ni ingresar otro valor mediante input.
    texto = "Awesome"
    texto = texto.lower()
    print(texto[0:3])
    medio = int(len(texto)/2)
    print(texto[medio-1:medio+2])
    print(texto[0:4] + texto[-3:])
# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_simple_test.py` o `python tp3_slice_simple_test.py`
