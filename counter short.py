from machine import Pin
from time import sleep

% LED definitions ------------------
ledBlue=Pin(0, Pin.OUT)
ledRed=Pin(1, Pin.OUT)
ledGreen=Pin(2, Pin.OUT)
ledYellow=Pin(3, Pin.OUT)
ledBlue2=Pin(4, Pin.OUT)
ledRed2=Pin(5, Pin.OUT)
ledGreen2=Pin(6, Pin.OUT)
ledYellow2=Pin(7, Pin.OUT)
% ---------------------------------
% variable defintions -------------

x=1 #variable for sleep
y=0 # variable for LED reset
a=0 # binary 1st digit
b=0 # binary 2nd digit
c=0 # binary 3rd digit
d=0 # binary 4th digit
e=0 # binary 5th digit
f=0 # binary 6th digit
g=0 # binary 7th digit
h=0 # binary 8th digit
% ---------------------------------
% counter loop --------------------
while True:
    ledBlue.value(y)
    ledRed.value(y)
    ledGreen.value(y)
    ledYellow.value(y)
    ledBlue2.value(y)
    ledRed2.value(y)
    ledGreen2.value(y)
    ledYellow2.value(y)
    for i in range (0, 256, 1):
        a=int(i%2)
        b=int(i/2)%2
        c=int(i/4)%2
        d=int(i/8)%2
        e=int(i/16)%2
        f=int(i/32)%2
        g=int(i/64)%2
        h=int(i/128)%2
        ledBlue.value(a)
        ledRed.value(b)
        ledGreen.value(c)
        ledYellow.value(d)
        ledBlue2.value(e)
        ledRed2.value(f)
        ledGreen2.value(g)
        ledYellow2.value(h)
        sleep(x/15)
    