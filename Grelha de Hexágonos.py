import turtle

a = turtle.Screen()
turtle.speed(0)
def Hexágono(posx, posy,lado):
    turtle.showturtle()
    # posicioan
    turtle.penup()
    turtle.goto(posx, posy)
    turtle.pendown()

    # desenha
    for i in range(6):
        turtle.forward(lado)
        turtle.left(60)
    turtle.hideturtle()

def grelha(n,posx, posy,lado,cor):

    # inicialização
    turtle.pencolor(cor)
    for i in range(n):

        # desenha linha i
        for j in range(n):
            Hexágono(turtle.xcor(),turtle.ycor(), lado)
            turtle.setx(turtle.xcor()+lado)

        # muda de linha
        turtle.penup()
        turtle.goto(posx,turtle.ycor()-lado)
        turtle.pendown()
    turtle.hideturtle()


Hexágono(-100,250,50)
grelha(5,-100,250,50,'darkcyan')

a.exitonclick()