from machine import Pin
import time

led = Pin(15, Pin.OUT)
bt = Pin(16, Pin.IN, Pin.PULL_UP)

while True:
    led.value(not bt.value()) #tirar o not caso queira que o led permaneça ligado
    time.sleep_ms(100) 