import keyboard
import time
import pyautogui
#skill y tiempo de casteo
def skills(key, duration):
    pyautogui.keyDown(key)
    time.sleep(duration)  # Mantiene la tecla presionada durante 3 segundos
    pyautogui.keyUp(key)
#click derecho arriba

def arriba_click():
    x = 960
    y = 300
    pyautogui.moveTo(x, y)
    pyautogui.click(button='left')
    time.sleep(1)
def revivir():
    x = 1379
    y = 445
    pyautogui.moveTo(x, y)
    for _ in range(5):
        pyautogui.click(button='left')
    time.sleep(0.1)
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
    time.sleep(1)
def matona():
    skills('q',0.1)
    skills('v',1)
    skills('v',1)
    skills('w',1)
    skills('e',2)
    skills('r',0.1)
    skills('a',1)
    skills('s',0.1)
    skills('d',0.1)
    skills('f',0.1)
    time.sleep(1)
def soul():
    skills('v',1)
    time.sleep(2)
    skills('q',2)
    time.sleep(1)
    skills('w',1)
    time.sleep(1)
    skills('e',1)
    time.sleep(1)
    skills('r',1)
    time.sleep(1)
    skills('a',1)
    time.sleep(1)
    skills('s',1)
    time.sleep(1)
    skills('d',2)
    time.sleep(1)
    skills('f',1)
    time.sleep(1)
def franco():
    skills('q',0.1)
    time.sleep(1)
    skills('v',1)
    time.sleep(2)
    skills('w',1)
    skills('e',1)
    skills('r',1)
    skills('a',1)
    skills('s',1)
    time.sleep(1)
    skills('d',2)
    time.sleep(1)
    skills('f',2.5)
    time.sleep(1)
def berserker():
    skills('z',1)
    skills('q',1)
    time.sleep(1)
    skills('v',4)
    time.sleep(1)
    skills('w',2)
    skills('e',1)
    skills('r',2)
    skills('a',1)
    skills('s',2)
    skills('d',1)
    skills('f',1)
    time.sleep(1)
def breaker():
    skills('q',1)
    time.sleep(1)
    skills('v',1)
    time.sleep(2)
    skills('w',1)
    skills('e',1)
    skills('r',1)
    skills('a',1)
    skills('s',3)
    skills('d',1)
    skills('f',1)
    time.sleep(1)

def floor1_gunlancer():
    total_duration = 120  # Duración total en segundos (2 =120 minutos)
    start_time = time.time()
    while time.time() - start_time < total_duration:
        arriba_click()
        revivir()
        gunlancer()
        skills('f1',1)
        abajo_click()
        gunlancer()
        skills('f1',1)
        skills('g',2)
        time.sleep(0.1)  # Espera corta entre repeticiones para evitar que el programa se vuelva muy pesado

def floor1_matona():
    total_duration = 80  # Duración total en segundos (2 =120 minutos)
    start_time = time.time()
    while time.time() - start_time < total_duration:
        revivir()
        arriba_click()
        matona()
        skills('f1',1)
        revivir()
        abajo_click()
        matona()
        skills('f1',1)
        for _ in range(5):
            skills('g',1)
        time.sleep(0.1)
def floor1_soul():
    total_duration = 80  # Duración total en segundos (2 =120 minutos)
    start_time = time.time()
    while time.time() - start_time < total_duration:
        arriba_click()
        soul()
        skills('f1',5)
        abajo_click()
        soul()
        skills('f1',5)
        skills('g',5)
        time.sleep(0.1)
def floor1_franco():
    total_duration = 80  # Duración total en segundos (2 =120 minutos)
    start_time = time.time()
    while time.time() - start_time < total_duration:
        revivir()
        arriba_click()
        franco()
        skills('f1',2)
        revivir()
        abajo_click()
        franco()
        skills('f1',2)
        for _ in range(5):
            skills('g',1)
            time.sleep(0.1)
        time.sleep(0.1)
def floor1_serker():
    total_duration = 80  # Duración total en segundos (2 =120 minutos)
    start_time = time.time()
    while time.time() - start_time < total_duration:
        revivir()
        arriba_click()
        berserker()
        skills('f1',2)
        revivir()
        abajo_click()
        berserker()
        skills('f1',2)
        for _ in range(5):
            skills('g',1)
            time.sleep(0.1)
        time.sleep(0.1)
def floor1_breaker():
    total_duration = 80  # Duración total en segundos (2 =120 minutos)
    start_time = time.time()
    while time.time() - start_time < total_duration:
        revivir()
        arriba_click()
        breaker()
        skills('f1',2)
        revivir()
        abajo_click()
        breaker()
        skills('f1',2)
        for _ in range(5):
            skills('g',1)
            time.sleep(0.1)
        time.sleep(0.1)