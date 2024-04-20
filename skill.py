
import keyboard
import time
import pyautogui
#skill y tiempo de casteo
def skills(key, duration):
    keyboard.press(key)
    time.sleep(duration)
    keyboard.release(key)
#click derecho arriba

def arriba_click():
    x = 960
    y = 300
    pyautogui.moveTo(x, y)
    pyautogui.click(button='left')
    time.sleep(1)
def abajo_click():
    x = 960
    y = 660
    pyautogui.moveTo(x, y)
    pyautogui.click(button='left')
    time.sleep(1)

def gunlancer():
    skills('q',1)
    time.sleep(1)
    skills('w',1)
    time.sleep(1)
    skills('e',2)
    time.sleep(1)
    skills('r',2)
    time.sleep(1)
    skills('a',1)
    time.sleep(1)
    skills('s',2)
    #skills('d',1)
    time.sleep(1)
    skills('f',1)
def matona():
    skills('q',1)
    time.sleep(1)
    skills('w',2)
    time.sleep(1)
    skills('e',2)
    time.sleep(1)
    skills('r',1)
    time.sleep(1)
    skills('a',1)
    time.sleep(1)
    skills('s',1)
    time.sleep(1)
    skills('d',1)
    time.sleep(1)
    skills('f',1)
    time.sleep(1)

def floor1_gunlancer():
    total_duration = 120  # Duración total en segundos (2 =120 minutos)
    start_time = time.time()
    while time.time() - start_time < total_duration:
        arriba_click()
        gunlancer()
        keyboard.press('f1')
        abajo_click()
        gunlancer()
        keyboard.press('f1')
        keyboard.press('g')
        time.sleep(0.1)  # Espera corta entre repeticiones para evitar que el programa se vuelva muy pesado

def floor1_matona():
    total_duration = 120  # Duración total en segundos (2=120 minutos)
    start_time = time.time()
    while time.time() - start_time < total_duration:
        arriba_click()
        matona()
        keyboard.press('f1')
        abajo_click()
        matona()
        keyboard.press('f1')
        keyboard.press('g')
        time.sleep(0.1)