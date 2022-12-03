from turtle import *
import streamlit as st
import time
from PIL import Image
import threading
def pattern1():
    title("PATTERN1")
    bgcolor("white")
    list1=["red","blue","green","yellow"]
    up()
    goto(200,0)
    for i in range(4):
        down()
        begin_fill()
        fillcolor(list1[i])
        circle(50)
        end_fill()
        up()
        backward(100)

def pattern2():
    title("PATTERN2")
    list1=["red","blue","green","yellow"]
    # reset()
    up()
    goto(200,0)
    for i in range(4):
        down()
        color(list1[i])
        pensize(20)
        circle(100)
        up()
        backward(100)
def pattern3():
    # reset()
    title("PATTERN3")
    bgcolor("black")
    pencolor("red")
    speed(100)
    penup()
    goto(0,200)
    pendown()
    x=0
    y=0
    while True:
        forward(x)
        right(y)
        x+=3 #x+=3
        y+=1 #y+=1
        if y==210 :
            break
        hideturtle()
def pattern4():
    title("PATTERN4")
    bgcolor("black")
    speed(0)
    hideturtle()
    for i in range(120):
        color("red")
        circle(i)
        color("orange")
        circle(i*0.8)
        right(3)
        forward(3)

def pattern5():
    title("PATTERN5")
    colormode(255)
    color(255,20,147)
    # wn.bgcolor("black")
    p=True
    n=1
    t=1
    speed(0)
    while True:
        circle(n)
        if p:
            n=n-1
        else:
            n=n+1
        if n==0 or n==60:
            p=not p 
            t+=1
        left(1)
        forward(3)
        if(t==8):
            break
    p=True
    n=1
    t=1
    color("yellow")
    speed(0)
    while True:
        circle(-n)
        if p:
            n=n-1
        else:
            n=n+1
        if n==0 or n==60:
            p=not p 
            t+=1
        right(1)
        forward(3)
        if(t==8):
            break  

    setheading(0)
    p=True
    n=1
    t=1
    color("red")
    speed(0)
    while True:
        circle(n)
        if p:
            n=n-1
        else:
            n=n+1
        if n==0 or n==60:
            p=not p 
            t+=1
        right(2)
        forward(3)
        if(t==16):
            break                        

def pattern6():
    title("PATTERN6")
    amul=Turtle()
    title("flower")
    amul.setheading(0)
    p=True
    n=1
    t=1
    amul.color("red")
    amul.speed(0)
    while True:
        amul.circle(-n)
        if p:
            n=n-1
        else:
            n=n+1
        if n==0 or n==60:
            p=not p 
            t+=1
        amul.left(1)
        amul.forward(3)
        if(t==8):
            break 
    amul.setheading(270)
    amul.color("green")
    amul.pensize(15)
    amul.forward(350)
    amul.setheading(0)
    amul.color("brown")
    amul.forward(200)
    amul.forward(-400)                           

def pattern7():
    title("PATTERN7")
    title("Rainbow")
    speed(0)
    colors=["red","purple","green","orange","blue","yellow"]
    bgcolor("black")
    amul=Pen()
    for i in range(360):
        amul.pencolor(colors[i%6])
        amul.width(i//100+1)
        amul.forward(i)
        amul.left(59)
def pattern8():
    import colorsys
    title("PATTERN8")
    speed(0)
    hideturtle()
    bgcolor("black")
    tracer(5)
    width(2)
    h=0.001
    for i in range(60):
        color(colorsys.hsv_to_rgb(h,1,1))
        forward(100)
        left(60)
        forward(100)
        right(120)
        circle(50)
        left(240)
        forward(100)
        left(60)
        forward(100)
        h+=0.02
        color(colorsys.hsv_to_rgb(h,1,1))
        forward(100)
        right(60)
        forward(100)
        left(120)
        circle(-50)
        right(240)
        forward(100)
        right(60)
        forward(100)
        left(2)
        h+=0.02
t=threading.current_thread().getName()
print("current thread1", t)
st.title("PATTERN USING PYTHON TURTLE")  
c1,c2,c3=st.columns(3)
image1=Image.open("pattern1.png")
image1=image1.resize((190,190))
c1.image(image1,caption="PATTERN 1")
image2=Image.open("pattern2.png")
image2=image2.resize((190,190))
c2.image(image2,caption="PATTERN 2")
image3=Image.open("pattern3.png")
image3=image3.resize((190,190))
c3.image(image3,caption="PATTERN 3")
image4=Image.open("pattern4.png")
image4=image4.resize((190,190))
c1.image(image4,caption="PATTERN 4")
image5=Image.open("pattern5.png")
image5=image5.resize((190,190))
c2.image(image5,caption="PATTERN 5")
image6=Image.open("pattern6.png")
image6=image6.resize((190,190))
c3.image(image6,caption="PATTERN 6")
image7=Image.open("pattern7.png")
image7=image7.resize((190,190))
c1.image(image7,caption="PATTERN 7")
image8=Image.open("pattern8.png")
image8=image8.resize((190,190))
c2.image(image8,caption="PATTERN 8")
image8=Image.open("pattern8.png")
image8=image8.resize((190,190))


n=st.text_input("Enter the Pattern No")
t=1
if st.button("Enter"):
    st.success("Displaying")
    t=threading.current_thread().getName()
    print("current thread2", t)
    try:
        t=threading.current_thread().getName()
        print("current thread3", t)
        if(n=='1'):
            reset()
            pattern1()
        if(n=='2'):
            reset()   
            pattern2() 
        if(n=='3'):
            reset()    
            pattern3() 
        if(n=='4'):
            reset()
            pattern4()
        if(n=='5'):
            reset()   
            pattern5() 
        if(n=='6'):
            reset()    
            pattern6()
        if(n=='7'):
            reset()
            pattern7()
        if(n=='8'):
            reset()
            pattern8()       
        mainloop()  
        # n=st.text_input("Enter the Pattern No",key=str(t))
        # t+=1


    except Terminator :
        pass
        # st.text("Interrupted")           
            

            
# if __name__ ==  '__main__': # main function will run in cmd 
#   main()

 #streamlit run "D:\python\ML model\turtle_program\turtle_program1.py"   

