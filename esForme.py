import turtle
from turtle import *
nlati = int(input("Scrivi un numero: "))
ang=360/nlati
color('blue', 'lightgreen')
begin_fill()
while True:
    forward(80)
    left(ang)
    if abs(pos()) < 1:
        break
end_fill()
done()