from sierpinski import Sierpinski

sides = int(input("How many sides should the shape be? "))
length = int(input("How big should each side be? "))

doodler = Sierpinski(sides=sides, length=length, speed=1000, dotsize=5)
doodler.draw_sierpinski()