import turtle
wn = turtle.Screen()
wn.setup(500,500)
turtle = turtle.Turtle()
turtle.speed("fastest")

step = 100
def draw_square(length,angle,c):
# for i in range (0,step):
    if c ==0: return
    for b in range (0,4):
        turtle.forward(length+c)
        turtle.right(angle+b)
        draw_square(length,angle,c-1)
draw_square(100,90,step)
                        