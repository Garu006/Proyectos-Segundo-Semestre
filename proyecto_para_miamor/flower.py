import turtle
import math

def generar_flor_realista():
    # Configurar pantalla
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=800)
    screen.title("Flor para ti")

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    screen.tracer(0)

    # Mostrar texto "Te amo"
    t.goto(0, 320)
    t.color("white")
    t.write("Te amo", align="center", font=("Courier", 36, "bold"))

    # Dibujar centro de la flor
    t.goto(0, -30)
    t.color("#6b3e26")  # marrón oscuro
    t.begin_fill()
    t.circle(35)
    t.end_fill()

    # Dibujar pétalos
    num_petalos = 18
    petalo_radio = 120
    petalo_angulo = 60
    petalo_color = "#FFCC00"  # amarillo girasol

    for i in range(num_petalos):
        angulo = 360 / num_petalos * i
        t.setheading(angulo)
        t.penup()
        t.goto(0, 0)
        t.forward(40)
        t.pendown()
        t.color(petalo_color, petalo_color)
        t.begin_fill()
        dibujar_petalo(t, radio=petalo_radio, angulo=petalo_angulo)
        t.end_fill()

    # Dibujar tallo
    t.penup()
    t.goto(0, -30)
    t.setheading(-90)
    t.color("#228B22")  # verde
    t.pensize(20)
    t.pendown()
    t.forward(200)

    screen.update()
    screen.mainloop()

def dibujar_petalo(t, radio=100, angulo=60):
    """Dibuja un pétalo con dos arcos simétricos."""
    for _ in range(2):
        t.circle(radio, angulo)
        t.left(180 - angulo)

if __name__ == '__main__':
    generar_flor_realista()
