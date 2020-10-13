import turtle

x1, y1 = eval(input("첫 번째 점에 대한 x1과 y1을 입력하세요: "))
x2, y2 = eval(input("두 번째 점에 대한 x2와 y2를 입력하세요: "))

distance = ((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))**0.5

turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.write("점1")
turtle.goto(x2,y2)
turtle.write("점2")

turtle.penup()
turtle.goto((x1+x2)/2,(y1+y2)/2)
turtle.write(distance)

turtle.done()
