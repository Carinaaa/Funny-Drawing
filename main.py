'''import colorgram


colors = colorgram.extract("my_hirst_pic.jpg", 30)

rgb_colors = []
for c in colors:
    r = c.rgb.r
    g = c.rgb.g
    b = c.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

print(rgb_colors)
'''
colors = [(245, 241, 233), (227, 234, 242), (245, 234, 239), (233, 242, 236), (208, 158, 96), (234, 213, 101), (41, 104, 144), (149, 78, 57), (130, 168, 194), (202, 137, 162), (148, 65, 83), (24, 40, 55), (204, 90, 68), (169, 159, 55), (139, 180, 152), (193, 89, 121), (59, 117, 93), (26, 44, 36), (223, 171, 187), (63, 46, 34), (91, 154, 104), (44, 161, 182), (237, 212, 7), (226, 175, 167), (13, 96, 75), (41, 59, 99), (179, 189, 213), (99, 125, 168), (65, 33, 43), (104, 43, 59)]

from turtle import Turtle, Screen, colormode

screen = Screen()
screen.setup(width=500, height=400)
x = -250
y = -200
tim = Turtle("turtle")
tim.color("pink")
tim.penup()
tim.goto(x=x, y=y)

colormode(255)

while y < 200:
    for c in colors:
        if tim.pos()[0] >= 250:
            tim.penup()
            x = -250
            y += 50
            tim.setpos(x,y)
        tim.pendown()
        tim.dot(15,c)
        tim.penup()
        tim.forward(50)


screen.exitonclick()