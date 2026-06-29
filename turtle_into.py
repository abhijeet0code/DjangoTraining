from turtle import *

# forward(100)
# left(95)
# forward(200)
# right(85)
# forward(300)

reset()
speed(0)
penup()
goto(-150,250)
pendown()
right(90)
forward(550)
left(90)
forward(10)
left(90)
forward(550)
left(90)
forward(10)


bk(10)
# penup()
# pendown()


color("black","orange")

begin_fill()
bk(340)
left(90)
forward(80)
right(90)
forward(340)
left(90)
end_fill()

color("black","white")
begin_fill()
forward(80)
left(90)
forward(340)
left(90)
forward(80)
bk(80)
end_fill()

color("black","green")
begin_fill()
bk(80)
left(90)
forward(340)
right(90)
forward(80)
end_fill()


penup()

goto(30,170)
pendown()
circle(40)


done()