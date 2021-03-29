import time
from pynput.keyboard import Key, Controller

def escribir():
    teclado = Controller()

    for letra in palabras[i]:
        teclado.press(letra)
        teclado.release(letra)

    teclado.press(Key.enter)
    teclado.release(Key.enter)
    time.sleep(2)

letraDeUnaCancion=""""""

palabras = letraDeUnaCancion.split(" ")

time.sleep(5)

for i in range(len(palabras)):
    escribir()
