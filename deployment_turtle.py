import tk
import tkinter as Tk
from turtle import *
import streamlit as st
import time
from PIL import Image
import threading
import colorsys as cs
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
    title("PATTERN 4")
    setup(800,800)
    speed(0)
    width(2)
    bgcolor("black")
    for j in range(25):
        for i in range(15):
            color(cs.hsv_to_rgb(i/15,j/25,1))
            right(90)
            circle(200-j+4,90)
            left(90)
            circle(200-j+4,90)
            right(180)
            circle(50,24)
    hideturtle()
    done()        

def pattern5():
    title("PATTERN5")
    setup (800,800)
    tracer(10)
    width(4)
    bgcolor("black")
    def square(x):
        for i in range(3):
            forward(x)
            left(90)
        forward(x)
    for j in range(20):
        for i in range(50): #
                color(cs.hsv_to_rgb(i/10,1-j/20,1))
                right(135)
                square(200-j+4)
                right(135)
                circle(50,24)   #34 
    hideturtle()
    done()        


def pattern6():
    title("PATTERN6")
    bgcolor("black")
    tracer(10)
    width(2)
    def square(x):
        for i in range(3):
            forward(x)
            left(90)
        forward(x)
    n=35
    for i in range(n):
        color(cs.hsv_to_rgb(1-i/n,1-i/n,1))
        for j in range(4):
            square(30+(i*3))
            circle(30+(i*3))
    hideturtle()
    done()                                          

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
def pattern9():
    title("PATTERN9")
    bgcolor("black")
    t=[Turtle(),Turtle()] 
    x=6
    colors=["red","yellow","blue","lime"]
    for index,i in enumerate(t):
        i.speed(0)
        i.color("white")
        i.shape("circle")
        i.shapesize(0.3)
        i.width(3)
        i.pu()   
        i.seth(90)
        i.fd(350)
        i.seth(-180)
        i.pd()
    t[0].pu()
    delay(0)
    speed(0)
    ht()
    time.sleep(4)
    for i in colors:
        color(i)
        for i in range(360):
            t[0].fd(x)
            t[0].lt(1)
            pu()
            goto(t[0].pos())
            pd()
            t[1].fd(2*x)
            t[1].lt(2)
            goto(t[1].pos())
    done()    
            
t=threading.current_thread().getName()
print("current thread1", t)
st.title("PATTERN USING PYTHON TURTLE")  
c1,c2,c3=st.columns(3)
image1=Image.open("D:/python/ML model/turtle_program/pattern1.png")
image1=image1.resize((190,190))
c1.image(image1,caption="PATTERN 1")
image2=Image.open("D:/python/ML model/turtle_program/pattern2.png")
image2=image2.resize((190,190))
c2.image(image2,caption="PATTERN 2")
image3=Image.open("D:/python/ML model/turtle_program/pattern3.png")
image3=image3.resize((190,190))
c3.image(image3,caption="PATTERN 3")
image4=Image.open("D:/python/ML model/turtle_program/pattern4.png")
image4=image4.resize((190,190))
c1.image(image4,caption="PATTERN 4")
image5=Image.open("D:/python/ML model/turtle_program/pattern5.png")
image5=image5.resize((190,190))
c2.image(image5,caption="PATTERN 5")
image6=Image.open("D:/python/ML model/turtle_program/pattern6.png")
image6=image6.resize((190,190))
c3.image(image6,caption="PATTERN 6")
image7=Image.open("D:/python/ML model/turtle_program/pattern7.png")
image7=image7.resize((190,190))
c1.image(image7,caption="PATTERN 7")
image8=Image.open("D:/python/ML model/turtle_program/pattern8.png")
image8=image8.resize((190,190))
c2.image(image8,caption="PATTERN 8")
image9=Image.open("D:/python/ML model/turtle_program/pattern9.png")
image9=image9.resize((190,190))
c3.image(image9,caption="PATTERN 9")

def main():
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
            if(n=='9'):
                reset()
                pattern9()           
            mainloop()  
            # n=st.text_input("Enter the Pattern No",key=str(t))
            # t+=1


        except Terminator :
            pass
            # st.text("Interrupted")           
                

            
if __name__ ==  '__main__': # main function will run in cmd 
  main()

 #streamlit run "D:\python\ML model\turtle_program\turtle_program1.py"   

