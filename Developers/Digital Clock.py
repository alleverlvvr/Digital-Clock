from tkinter import *
from tkinter import ttk
from PIL import  ImageTk, Image # pip install pillow
import datetime
import time
import threading

root = Tk()

#root.config(bg="yellow")
root.geometry("600x670")
root.title("Advanced Digital Clock")
root.config(bg="cadetblue1")
# root.minsize(400,200)
# root.maxsize(900,600)
root.resizable(False, False) 

#~~~~~~~~~~~~~~~~~ Heading ~~~~~~~~~~~~~~~~~~#
heading_frame = Frame(root,border=5,relief = SUNKEN,bg="white")
image = Image.open("images/logo.jpg")
image = image.resize((50,50),Image.ANTIALIAS)
images=ImageTk.PhotoImage(image)

Label(heading_frame, image=images).pack(pady=2)
Label(heading_frame,text="Advanced Digital Clock",font="Algerian 20",bg = "white",fg="navy").pack()
heading_frame.pack(pady=(5,0),fill =Y)
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

#~~~~~~~~~~~~~~~~~~ Tabs ~~~~~~~~~~~~~~~~~~~~~#
my_notebook = ttk.Notebook(root)
my_notebook.pack(side=LEFT,padx=15)

clock_tab = Frame(my_notebook,width= 600,height = 500,bg="#8CF5B6")
stopwatch_tab = Frame(my_notebook,width= 600,height = 500)
alarm_tab = Frame(my_notebook,width= 600,height = 500)
about_us_tab = Frame(my_notebook,width= 500,height = 500)

my_notebook.add(clock_tab, text = "Clock")
# my_notebook.add(stopwatch_tab, text = "Stopwatch")
# my_notebook.add(alarm_tab, text = "Alarm")
my_notebook.add(about_us_tab, text = "About us")

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##



image_back = Image.open("images/background1.jpg")
image_back = image_back.resize((600,520),Image.ANTIALIAS)
image_background=ImageTk.PhotoImage(image_back)

Label(clock_tab, image=image_background).place(x=0,y=0)

#~~~~~~~~~~~~~~~~ Clock Window ~~~~~~~~~~~~~~~~#

def clock():
    h=time.strftime('%I')
    h1=time.strftime('%H')
    m=time.strftime('%M')
    s=time.strftime('%S')
    dd=time.strftime('%d')
    mm=time.strftime('%B')
    week_day = time.strftime("%A")

    yyyy=datetime.datetime.now()
    lbl_date.config(text=dd)
    lbl_month.config(text=mm)
    lbl_year.config(text=yyyy.year)
    
    lbl_noon.config(text= time.strftime("%p"))

    total_time = time.strftime('%X')
    # print(time.strftime('%X'))


    if total_time >= "00:00:00" and total_time < "05:00:00" :
        lbl_noon2.config(text='Mid Night')
    elif total_time >= "05:00:00" and total_time < "12:00:00":
        lbl_noon2.config(text='Morning')
    elif total_time >= "12:00:00" and total_time < "15:00:00":
        lbl_noon2.config(text='Noon')
    elif total_time >= "15:00:00" and total_time < "18:00:00":
        lbl_noon2.config(text='Afternoon')
    elif total_time >= "18:00:00" and total_time < "22:00:00":
        lbl_noon2.config(text='Evening')
    else:
        lbl_noon2.config(text='Night')

    lbl_hr1.config(text=h)
    lbl_min1.config(text=f": {m} :")
    lbl_sec1.config(text=s)
    lbl_cdate.config(text=week_day)

    lbl_hr1.after(200,clock)
    

clock_frame = Frame(clock_tab,border=5,relief = GROOVE,bg="#390404")



lbl_hr1=Label(clock_frame,text='08',font=("Digital-7",50),bg='#390404',fg='#FA2441',padx=25)
lbl_hr1.grid(row=0,column=0,pady=(0,5),padx=(8))

# Label(clock_frame,text=":",font=("Digital-7",50),bg='#390404',fg='#FA2441').place(x=90,y=0)

lbl_min1=Label(clock_frame,text='08',font=("Digital-7",50),bg='#390404',fg='#FA2441',padx=25)
lbl_min1.grid(row=0,column=1,pady=(0,5),padx=(0,8))

lbl_sec1=Label(clock_frame,text='08',font=("Digital-7",50),bg='#390404',fg='#FA2441',padx=25)
lbl_sec1.grid(row=0,column=2,pady=(0,5))

# Label(clock_frame,text=":",font=("Digital-7",50),bg='#390404',fg='#FA2441').place(x=220,y=0)

lbl_noon=Label(clock_frame,text='AM',font=("Digital-7",50),bg='#390404',fg='#FA2441')
lbl_noon.grid(row=0,column=3,pady=(0,5))

lbl_hr2=Label(clock_frame,text='Hour',font=("Digital-7",25,"bold"),padx=3,bg='green',fg='white')
lbl_hr2.grid(row=1,column=0,pady=(0,5))

lbl_min2=Label(clock_frame,text='Minute',font=("Digital-7",25,"bold"),bg='green',fg='white',padx=5)
lbl_min2.grid(row=1,column=1,pady=(0,5))

lbl_sec2=Label(clock_frame,text='Second',font=("Digital-7",25,"bold"),bg='blue',fg='white')
lbl_sec2.grid(row=1,column=2,pady=(0,5))

lbl_noon2=Label(clock_frame,text='Noon',font=("Digital-7",25,"bold"),bg='blue',fg='white')
lbl_noon2.grid(row=1,column=3,pady=(0,5))


lbl_date=Label(clock_frame ,text='date',font=("Digital-7",25,"bold"),bg='green',fg='white')
lbl_date.grid(row=2,column=0,pady=(0,5))


lbl_month=Label(clock_frame,text='month',font=("Digital-7",25,"bold"),bg='green',fg='white')
lbl_month.grid(row=2,column=1,pady=(0,5))

lbl_year=Label(clock_frame,text='Year',font=("Digital-7",25,"bold"),bg='blue',fg='white')
lbl_year.grid(row=2,column=2,pady=(0,5))

lbl_cdate=Label(clock_frame,text='',font=("Digital-7",25,"bold"),bg='blue',fg='white')
lbl_cdate.grid(row=2,column=3,pady=(0,5))


clock_frame.pack(anchor = CENTER,pady=(150,0))
clock()



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#~~~~~~~~~~~~~~~~~~~~~~~~~ About us Tab ~~~~~~~~~~~~~~~~~~~~~~~~#
photos = []
for i in range(1,7):
    image = Image.open(f"images/{i}.jpeg")
    image = image.resize((80,80),Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))

photoframe = Frame(about_us_tab,border=5,relief = GROOVE,bg="deepskyblue2")
f1=Frame(photoframe,width=800,height=200,padx=10,bg = "deepskyblue2")
Label(f1,text="Name:- Rahul Shaw\nRoll no:- 13000319007 ",font="times 15",bg="light cyan",fg="deep pink4").pack(side=RIGHT)
Label(f1, image=photos[0],pady=50,padx=40).pack(padx=(15,30),anchor="s")
f1.pack(pady=(5,0),anchor="w")

f2 = Frame(photoframe, width=900, height=200, padx=22,bg = "deepskyblue2")
Label(f2,text="Name:- Arijit Bandyopadhaya\nRoll no:- 13000319009",font="times 15",bg="light cyan",fg="deep pink4").pack(side=LEFT)
Label(f2, image=photos[1], anchor="e", padx=22).pack(padx=(30,15),anchor="s")
f2.pack(anchor="w")

f2 = Frame(photoframe, width=900, height=200, padx=22,bg = "deepskyblue2")
Label(f2,text="Name:- Sayan Ghosh\nRoll no:- 13000319045",font="times 15",bg="light cyan",fg="deep pink4").pack(side=RIGHT)
Label(f2, image=photos[2], anchor="e", padx=22).pack(padx=(15,30),anchor="s")
f2.pack(anchor="w")

f2 = Frame(photoframe, width=900, height=200, padx=22,bg = "deepskyblue2")
Label(f2,text="Name:- Ishani Banerjee\nRoll no:- 13000319046",font="times 15",bg="light cyan",fg="deep pink4").pack(side=LEFT)
Label(f2, image=photos[3], anchor="e", padx=22).pack(padx=(30,15),anchor="s")
f2.pack(anchor="w")

f2 = Frame(photoframe, width=900, height=200, padx=22,bg = "deepskyblue2")
Label(f2,text="Name:- Biswambhar Pal\nRoll no:- 13000319047",font="times 15",bg="light cyan",fg="deep pink4").pack(side=RIGHT)
Label(f2, image=photos[4], anchor="e", padx=22).pack(padx=(15,30),anchor="s")
f2.pack(anchor="w")

f2 = Frame(photoframe, width=900, height=200, padx=22,bg = "deepskyblue2")
Label(f2,text="Name:- Brishti Mukherjee\nRoll no:- 13000319052",font="times 15",bg="light cyan",fg="deep pink4").pack(side=LEFT)
Label(f2, image=photos[5], anchor="e", padx=22).pack(padx=(30,15),anchor="s")
f2.pack(pady=(0,5),anchor="w")

photoframe.pack()

# def testing():
#     l=Label(alarm_tab,text="")
#     l.pack()
#     time.sleep(5)
#     l.config(text = "times up!")

# but = Button(alarm_tab,text="click", command=threading.Thread(target=testing).start())
# but.pack()


root.mainloop()

