import turtle

turtle.penup()
turtle.right(90)
turtle.forward(500)
turtle.pendown()
turtle.color("blue")

turtle.write("   -->   F  R  O  N  T    G  A  T  E   ")
turtle.right(180)
turtle.penup()


 # Infinity road
turtle.color("blue")
turtle.pensize(4)
turtle.pendown()
turtle.forward(240)
turtle.penup()
turtle.forward(20)
turtle.pendown()
turtle.write("A  D   B L O C K") 
turtle.penup()
turtle.backward(20)
turtle.pendown()
turtle.left(90)
turtle.forward(170)
turtle.penup()
turtle.forward(90)
turtle.pendown()

turtle.write("A R C H I  /  M C A       ")
turtle.penup()
turtle.backward(100)
turtle.right(90)

#  birla

turtle.pendown()

turtle.forward(78)
turtle.right(90)
 
turtle.forward(15)
turtle.penup()
turtle.forward(20)
turtle.write("B I R L A    A U D I  T O R I U M")
turtle.penup()
turtle.backward(35)
turtle.left(90)

turtle.pendown()

# Physics dept
turtle.forward(90)
turtle.right(90)
turtle.forward(20)
turtle.left(90)

turtle.forward(20)
turtle.penup()
turtle.forward(10)
turtle.pendown()
turtle.write("  P H Y S I C S    D E  P T")
turtle.circle(5)
turtle.penup()
turtle.backward(30)
turtle.right(90)

# Chemistry dept
turtle.color("blue")
turtle.pendown()
turtle.forward(400)
turtle.left(90)
turtle.forward(20)
turtle.penup()
turtle.forward(10)
turtle.pendown()
turtle.write(" C H E M I S T R Y      D E P T")
turtle.circle(5)
turtle.penup()
turtle.backward(30)
turtle.right(90)

turtle.pendown()
turtle.forward(94)
turtle.left(90)


turtle.pensize(2)
turtle.color("grey")
turtle.forward(170)
turtle.right(90)
turtle.forward(50)
turtle.penup()
turtle.forward(20)
turtle.pendown()

for i in range(1,2):
	turtle.forward(80)
	turtle.right(90)
	turtle.forward(30)
	turtle.right(90)
	turtle.forward(80)
	turtle.right(90)
	turtle.forward(30)

turtle.penup()

turtle.forward(10)
turtle.write("P  A  R  K  I   N  G       A R  E A")	
turtle.backward(10)

turtle.right(90)
turtle.backward(70)
turtle.left(90)
turtle.pendown()
# C  S  -  I S  B L O C K

turtle.forward(75)
turtle.left(90)
turtle.forward(80)
turtle.left(90)
turtle.penup()
turtle.forward(30)

turtle.right(90)
turtle.forward(60)

turtle.color("red")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()
turtle.write("C  S  -  I  S   B L O C K")

#media center

turtle.left(90)
turtle.backward(30)
turtle.right(180)
turtle.forward(20)
turtle.color("navy")
turtle.pendown()
turtle.color("deeppink")
turtle.begin_fill()
for i in range(5):
   turtle.forward(27) 
   turtle.right(72) 

turtle.end_fill()
turtle.penup()
turtle.left(90)
turtle.forward(7)
turtle.color("red")
turtle.dot()
turtle.forward(130)

turtle.write("M E D I A  C E N T R E   ")
turtle.color("red")



turtle.penup()
turtle.goto(0,0)

turtle.done()
