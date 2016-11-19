#!/usr/bin/python

from Tkinter import *

root = Tk()

root.title("Simple Graph")

root.resizable(0, 0)

points = []

spline = 0

tag1 = "theline"
is_mousedown = False

e = Entry(root)
e.pack()

e.delete(0, END)
e.insert(0, "a default value")

var = StringVar()
label = Label(root, textvariable=var, relief=RAISED)

var.set("Hey!? How are you doing?")
label.pack()


def point(event):
    c.create_oval(event.x, event.y, event.x + 10, event.y + 10, fill="black")
    points.append(event.x)
    points.append(event.y)
    global is_mousedown
    is_mousedown = True
    return points


def canxy(event):
    print event.x, event.y


def graph(event):
    global theline
    c.create_line(points, tags="theline")


def motion(event):
    global is_mousedown
    if is_mousedown == True:
        c.create_oval(event.x, event.y, event.x + 10, event.y + 10, fill="black")
        points.append(event.x)
        points.append(event.y)
        return points
        # print event.x, event.y


def toggle(event):
    global spline
    if spline == 0:
        c.itemconfigure(tag1, smooth=1)
        spline = 1
    elif spline == 1:
        c.itemconfigure(tag1, smooth=0)
        spline = 0
    return spline


def mouseup(event):
    global is_mousedown
    is_mousedown = False


c = Canvas(root, bg="white", width=200, height=200)

c.configure(cursor="crosshair")

c.pack()

c.bind("<Button-1>", point)

c.bind("<Button-3>", graph)

c.bind("<Button-2>", toggle)

c.bind('<Motion>', motion)

c.bind('<ButtonRelease-1>', mouseup)


def action_detect():
    print "click!"
    global c
    print c.find_all()



b = Button(root, text="Detect", command=action_detect)
b.pack()

root.mainloop()
