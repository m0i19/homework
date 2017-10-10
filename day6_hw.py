import turtle as t

t.speed(0)
t.up()
t.sety(50)
t.down()
t.circle(60)
t.up()
t.sety(-130)
t.down()
t.circle(90)
t.up()

t.goto(-30,170)
t.down()
for x in range(3):
    t.forward(60)
    t.left(120)
t.up()

t.goto(-30,120)
t.down()
t.begin_fill()
t.circle(8)
t.end_fill()
t.up()

t.goto(30,120)
t.down()
t.begin_fill()
t.circle(8)
t.end_fill()
t.up()

t.goto(-5,80)
t.down()
t.goto(5,80)
t.up()

t.goto(-83,-10)
t.down()
t.goto(-120,10)
t.up()

t.goto(83,-10)
t.down()
t.goto(120,10)
t.up()

t.goto(0,-5)
t.down()
t.begin_fill()
t.fillcolor("red")
t.circle(9)
t.end_fill()
t.up()

t.goto(0,-50)
t.down()
t.begin_fill()
t.fillcolor("red")
t.circle(9)
t.end_fill()
t.up()

t.goto(0,-102)
t.down()
t.begin_fill()
t.fillcolor("red")
t.circle(9)
t.end_fill()
t.up()


