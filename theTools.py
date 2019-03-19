#!/usr/bin/env python3
'''
Author: Zawar Ahmed Tahir
Date: 19-03-2019, Tuesday
'''
#ZAT#
from tkinter import *
from tkinter import font
import RPi.GPIO as GPIO
import time
import serial
import math
ser=serial.Serial('/dev/ttyACM0',9600)
GPIO.setwarnings(False)
st=1
motor_counter = 0
ampere = 0
with open("/home/pi/Documents/amp.txt",'r') as myfile:
    data=myfile.read().replace('\n','')
    
ampere_limit = int(data)
print(ampere_limit)
b1, b2, b3, b4 = "red", "red", "red", "red"
limit = 12
button_row = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)  # ampere in from arduino
GPIO.setup(22, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
print(ampere)
win = Tk()

myFont = font.Font(family='Helvetica', size=18, weight='bold')
headerFont = font.Font(family='Helvetica', size=22, weight='bold')

if(st==1):
    GPIO.output(2, 1)
    GPIO.output(3, 1)
    GPIO.output(4, 1)
    GPIO.output(17, 1)
    GPIO.output(22, 1)
    GPIO.output(10, 1)
    GPIO.output(9, 1)
    GPIO.output(11, 1)
    GPIO.output(5, 1)
    GPIO.output(6, 1)
        
    GPIO.output(13, 1)
    GPIO.output(19, 1)
    GPIO.output(26, 1)
    GPIO.output(14, 1)
    GPIO.output(15, 1)
    GPIO.output(18, 1)
    GPIO.output(23, 1)
    GPIO.output(24, 1)
    GPIO.output(25, 1)
    GPIO.output(8, 1)
        
    GPIO.output(7, 1)
    GPIO.output(12,1)
    GPIO.output(16, 1)
    GPIO.output(20, 1)
    GPIO.output(21, 1)
    GPIO.output(27, 1)
    st=0
        

def m1_on_off():
    global b1
    global motor_counter
    if (m1_button["background"] == "red" and motor_counter < limit and ampere < ampere_limit):
        print("M1 ON")
        motor_counter = motor_counter + 1
        m1_button["background"] = "#7CFC00"
        GPIO.output(2, 0)
    elif (m1_button["background"] == "#7CFC00"):
        motor_counter = motor_counter - 1
        print("M1 OFF")
        GPIO.output(2, 1)
        m1_button["background"] = "red"
    print(motor_counter)


def m2_on_off():
    global b2
    global motor_counter
    if (m2_button["background"] == "red" and motor_counter < limit and ampere < ampere_limit):
        GPIO.output(3, 0)
        motor_counter = motor_counter + 1
        print("M2 ON")
        m2_button["background"] = "#7CFC00"

    elif (m2_button["background"] == "#7CFC00"):
        GPIO.output(3, 1)
        motor_counter = motor_counter - 1
        print("M2 OFF")
        m2_button["background"] = "red"
    print(motor_counter)


def m3_on_off():
    global b3
    global motor_counter
    if (m3_button["background"] == "red" and motor_counter < limit and ampere < ampere_limit):
        GPIO.output(4, 0)
        motor_counter = motor_counter + 1
        print("M3 ON")
        m3_button["background"] = "#7CFC00"
    elif (m3_button["background"] == "#7CFC00"):
        GPIO.output(4, 1)
        motor_counter = motor_counter - 1
        print("M3 OFF")
        m3_button["background"] = "red"
    print(motor_counter)


def m4_on_off():
    global b4
    global motor_counter
    if (m4_button["background"] == "red" and motor_counter < limit and ampere < ampere_limit):
        GPIO.output(17, 0)
        motor_counter = motor_counter + 1
        print("M4 ON")
        m4_button["background"] = "#7CFC00"
    elif (m4_button["background"] == "#7CFC00"):
        GPIO.output(17, 1)
        motor_counter = motor_counter - 1
        print("M4 OFF")
        m4_button["background"] = "red"
    print(motor_counter)


def m5_on_off():
    global b5
    global motor_counter
    if (m5_button["background"] == "red" and motor_counter < limit and ampere < ampere_limit):
        GPIO.output(22, 0)
        motor_counter = motor_counter + 1
        print("M5 ON")
        m5_button["background"] = "#7CFC00"
    elif (m5_button["background"] == "#7CFC00"):
        GPIO.output(22, 1)
        motor_counter = motor_counter - 1
        print("M5 OFF")
        m5_button["background"] = "red"
    print(motor_counter)


def m6_on_off():
    global b6
    global motor_counter
    if (m6_button["background"] == "red" and motor_counter < limit and ampere < ampere_limit):
        GPIO.output(10, 0)
        motor_counter = motor_counter + 1
        print("M6 ON")
        m6_button["background"] = "#7CFC00"
    elif (m6_button["background"] == "#7CFC00"):
        GPIO.output(10, 1)
        motor_counter = motor_counter - 1
        print("M6 OFF")
        m6_button["background"] = "red"
    print(motor_counter)


def m7_on_off():
    global b7
    global motor_counter
    if (m7_button["background"] == "red" and motor_counter < limit and ampere < ampere_limit):
        GPIO.output(9, 0)
        motor_counter = motor_counter + 1
        print("M7 ON")
        m7_button["background"] = "#7CFC00"
    elif (m7_button["background"] == "#7CFC00"):
        GPIO.output(9, 1)
        motor_counter = motor_counter - 1
        print("M7 OFF")
        m7_button["background"] = "red"
    print(motor_counter)


def m8_on_off():
    global b8
    global motor_counter
    if (m8_button["background"] == "red" and motor_counter < limit and ampere < ampere_limit):
        GPIO.output(11, 0)
        motor_counter = motor_counter + 1
        print("M8 ON")
        m8_button["background"] = "#7CFC00"
    elif (m8_button["background"] == "#7CFC00"):
        GPIO.output(11, 1)
        motor_counter = motor_counter - 1
        print("M8 OFF")
        m8_button["background"] = "red"
    print(motor_counter)


def m9_on_off():
    global b9
    global motor_counter
    if (m9_button["background"] == "red" and motor_counter < limit and ampere < ampere_limit):
        GPIO.output(5, 0)
        motor_counter = motor_counter + 1
        print("M9 ON")
        m9_button["background"] = "#7CFC00"
    elif (m9_button["background"] == "#7CFC00"):
        GPIO.output(5, 1)
        motor_counter = motor_counter - 1
        print("M9 OFF")
        m9_button["background"] = "red"
    print(motor_counter)


def m10_on_off():
    global b10
    global motor_counter
    if (m10_button["background"] == "red" and motor_counter < limit and ampere < ampere_limit):
        GPIO.output(6, 0)
        motor_counter = motor_counter + 1
        print("M10 ON")
        m10_button["background"] = "#7CFC00"
    elif (m10_button["background"] == "#7CFC00"):
        GPIO.output(6, 1)
        motor_counter = motor_counter - 1
        print("M10 OFF")
        m10_button["background"] = "red"
    print(motor_counter)


def m11_on_off():
    global b11
    global motor_counter
    if (m11_button["background"] == "red" and motor_counter < limit and ampere < ampere_limit):
        GPIO.output(13, 0)
        print("M11 ON")
        motor_counter = motor_counter + 1
        GPIO.output(20, 1)
        m11_button["background"] = "#7CFC00"
    elif (m11_button["background"] == "#7CFC00"):
        GPIO.output(13, 1)
        motor_counter = motor_counter - 1
        print("M11 OFF")
        m11_button["background"] = "red"
    print(motor_counter)


def m12_on_off():
    global b12
    global motor_counter
    if (m12_button["background"] == "red" and motor_counter < limit and ampere < ampere_limit):
        GPIO.output(19, 0)
        motor_counter = motor_counter + 1
        print("M12 ON")
        m12_button["background"] = "#7CFC00"
    elif (m12_button["background"] == "#7CFC00"):
        GPIO.output(19, 1)
        motor_counter = motor_counter - 1
        print("M12 OFF")
        m12_button["background"] = "red"
    print(motor_counter)


def m13_on_off():
    global b13
    global motor_counter
    if (m13_button["background"] == "red" and motor_counter < limit and ampere < ampere_limit):
        GPIO.output(26, 0)
        motor_counter = motor_counter + 1
        print("M13 ON")
        m13_button["background"] = "#7CFC00"
    elif (m13_button["background"] == "#7CFC00"):
        GPIO.output(26, 1)
        motor_counter = motor_counter - 1
        print("M13 OFF")
        m13_button["background"] = "red"
    print(motor_counter)


def m14_on_off():
    global b14
    global motor_counter
    if (m14_button["background"] == "red" and motor_counter < limit and ampere < ampere_limit):
        GPIO.output(14, 0)
        motor_counter = motor_counter + 1
        print("M14 ON")
        m14_button["background"] = "#7CFC00"
    elif (m14_button["background"] == "#7CFC00"):
        GPIO.output(14, 1)
        motor_counter = motor_counter - 1
        print("M14 OFF")
        m14_button["background"] = "red"
    print(motor_counter)


def m15_on_off():
    global b15
    global motor_counter
    if (m15_button["background"] == "red" and motor_counter < limit and ampere < ampere_limit):
        GPIO.output(15, 0)
        motor_counter = motor_counter + 1
        print("M15 ON")
        m15_button["background"] = "#7CFC00"
    elif (m15_button["background"] == "#7CFC00"):
        GPIO.output(15, 1)
        motor_counter = motor_counter - 1
        print("M15 OFF")
        m15_button["background"] = "red"
    print(motor_counter)


def m16_on_off():
    global b16
    global motor_counter
    if (m16_button["background"] == "red" and motor_counter < limit and ampere < ampere_limit):
        GPIO.output(18, 0)
        motor_counter = motor_counter + 1
        print("M16 ON")
        m16_button["background"] = "#7CFC00"
    elif (m16_button["background"] == "#7CFC00"):
        GPIO.output(18, 1)
        motor_counter = motor_counter - 1
        print("M16 OFF")
        m16_button["background"] = "red"
    print(motor_counter)


def m17_on_off():
    global b17
    global motor_counter
    if (m17_button["background"] == "red" and motor_counter < limit and ampere < ampere_limit):
        GPIO.output(23, 0)
        motor_counter = motor_counter + 1
        print("M17 ON")
        m17_button["background"] = "#7CFC00"
    elif (m17_button["background"] == "#7CFC00"):
        GPIO.output(23, 1)
        motor_counter = motor_counter - 1
        print("M17 OFF")
        m17_button["background"] = "red"
    print(motor_counter)


def m18_on_off():
    global b18
    global motor_counter
    if (m18_button["background"] == "red" and motor_counter < limit and ampere < ampere_limit):
        GPIO.output(24, 0)
        motor_counter = motor_counter + 1
        print("M18 ON")
        m18_button["background"] = "#7CFC00"
    elif (m18_button["background"] == "#7CFC00"):
        GPIO.output(24, 1)
        motor_counter = motor_counter - 1
        print("M18 OFF")
        m18_button["background"] = "red"
    print(motor_counter)


def m19_on_off():
    global b19
    global motor_counter
    if (m19_button["background"] == "red" and motor_counter < limit and ampere < ampere_limit):
        GPIO.output(25, 0)
        motor_counter = motor_counter + 1
        print("M19 ON")
        m19_button["background"] = "#7CFC00"
    elif (m19_button["background"] == "#7CFC00"):
        GPIO.output(25, 1)
        motor_counter = motor_counter - 1
        print("M19 OFF")
        m19_button["background"] = "red"
    print(motor_counter)


def m20_on_off():
    global b20
    global motor_counter
    if (m20_button["background"] == "red" and motor_counter < limit and ampere < ampere_limit):
        GPIO.output(8, 0)
        motor_counter = motor_counter + 1
        print("M20 ON")
        m20_button["background"] = "#7CFC00"
    elif (m20_button["background"] == "#7CFC00"):
        GPIO.output(8, 1)
        motor_counter = motor_counter - 1
        print("M20 OFF")
        m20_button["background"] = "red"
    print(motor_counter)


def m21_on_off():
    global b21
    global motor_counter
    if (m21_button["background"] == "red" and motor_counter < limit and ampere < ampere_limit):
        GPIO.output(7, 0)
        motor_counter = motor_counter + 1
        print("M21 ON")
        m21_button["background"] = "#7CFC00"
    elif (m21_button["background"] == "#7CFC00"):
        GPIO.output(7, 1)
        motor_counter = motor_counter - 1
        print("M21 OFF")
        m21_button["background"] = "red"
    print(motor_counter)


def m22_on_off():
    global b22
    global motor_counter
    if (m22_button["background"] == "red" and motor_counter < limit and ampere < ampere_limit):
        GPIO.output(12, 0)
        motor_counter = motor_counter + 1
        print("M22 ON")
        m22_button["background"] = "#7CFC00"
    elif (m22_button["background"] == "#7CFC00"):
        GPIO.output(12, 1)
        motor_counter = motor_counter - 1
        print("M22 OFF")
        m22_button["background"] = "red"
    print(motor_counter)


def m23_on_off():
    global b23
    global motor_counter
    if (m23_button["background"] == "red" and motor_counter < limit and ampere < ampere_limit):
        GPIO.output(16, 0)
        motor_counter = motor_counter + 1
        print("M23 ON")
        m23_button["background"] = "#7CFC00"
    elif (m23_button["background"] == "#7CFC00"):
        GPIO.output(16, 1)
        motor_counter = motor_counter - 1
        print("M23 OFF")
        m23_button["background"] = "red"
    print(motor_counter)


def m24_on_off():
    global b24
    global motor_counter
    if (m24_button["background"] == "red" and motor_counter < limit and ampere < ampere_limit):
        GPIO.output(20, 0)
        motor_counter = motor_counter + 1
        print("M24 ON")
        m24_button["background"] = "#7CFC00"
    elif (m24_button["background"] == "#7CFC00"):
        GPIO.output(20, 1)
        motor_counter = motor_counter - 1
        print("M24 OFF")
        m24_button["background"] = "red"
    print(motor_counter)

from subprocess import call
num_run=0
btn_funcid=0
text_=""
def exitProgram():
    print("Exit Button pressed")
    top = Toplevel(win)
    
    top.lift(aboveThis=win)
    #top.attributes("-topmost",True)
    L1 = Label(top, text="User Name")
    L1.grid(row=0, column=0, padx=(4, 4), pady=4)
    E1 = Entry(top, bd=5)
    E1.grid(row=0, column=1, padx=(4, 10), pady=4)
    L1 = Label(top, text="Password")
    L1.grid(row=1, column=0, padx=(4, 4), pady=4)
    E2 = Entry(top, bd=5, show="*")
    E2.grid(row=1, column=1, padx=(4, 10), pady=4)
    myFont = font.Font(family='Helvetica', size=8, weight='bold')
    
    def back():
        top.destroy()
        print("Back")

    exitButton = Button(top, text="Back", font=myFont, command=back, height=1, width=5)
    exitButton.grid(row=2, column=0, padx=(5, 5), pady=4)

    def exitProgram():
        ID = E1.get()
        print(ID)
        pwd = E2.get()
        print(pwd)
        if (E1.get() == "thetools" and E2.get() == "03462791445"):
            GPIO.cleanup()
            time.sleep(2)
            win.destroy()
        print("exit")

    backButton = Button(top, text="Setting", font=myFont, command=exitProgram, height=1, width=5)
    #backButton.grid(row=2, column=2, padx=(0, 0), pady=4)
    backButton.place(x=200,y=76)
    
    def changeAmp():
        if (E1.get() == "thetools" and E2.get() == "03462791445"):
            ampWin = Toplevel(top)
            ampWin.lift()
            ampWin.geometry("120x170")
            from functools import partial

            def saveFile(amp):
                global ampere_limit
                with open('/home/pi/Documents/amp.txt', 'w') as the_file:
                    the_file.write(amp)
                ampere_limit = int(amp)

            def click(btn):
                global num_run, text_

                text = "%s" % btn
                if not text == "Del" and not text == "Save":
                    text_ = text_ + btn
                    print(text_)
                    e.insert(END, text)
                if text == 'Del':
                    text_ = ""
                    e.delete(0, END)
                if text == 'Save':
                    if(len(text_)>0):
                        saveFile(text_)
                        text_ = ""
                        ampWin.destroy()
                        num_run = 0
                    # win.unbind('<Button-1>', btn_funcid)

            def close():
                global num_run, btn_funcid
                if num_run == 1:
                    ampWin.destroy()
                    num_run = 0
                    ampWin.unbind('<Button-1>', btn_funcid)

            def run():
                global num_run, btn_funcid
                if num_run == 0:
                    num_run = 1
                    btn_funcid = win.bind('<Button-1>', close)

            e = Entry(ampWin, font='Verdana  8 bold',width=11, justify='right', bd=3)
            e.grid(row=0, column=0, padx=(1, 1), pady=4)

            lf = LabelFrame(ampWin, text=" Ampere ", bd=3)
            lf.grid(padx=(1, 1), pady=(35, 5))

            btn_list = [
                '7', '8', '9',
                '4', '5', '6',
                '1', '2', '3',
                '0', 'Del', 'Save']
            r = 1
            c = 0
            n = 0
            btn = list(range(len(btn_list)))
            for label in btn_list:
                cmd = partial(click, label)
                btn[n] = Button(lf, text=label, width=1, height=1, command=cmd)
                btn[n].grid(row=r, column=c)
                n += 1
                c += 1
                if c == 3:
                    c = 0
                    r += 1
            e.bind('<Button-1>', run)
            e.place(x=10, y=10)
    changeAmpere = Button(top, text="Ampere", font=myFont, command=changeAmp, height=1, width=5)
    #changeAmpere.grid(row=2, column=1, padx=(0, 0), pady=4)
    changeAmpere.place(x=105, y=76)
    
    
import time  
    
def sysOff():
    GPIO.cleanup()
   # time.sleep(2)
    win.destroy()
    call("sudo shutdown -h now",shell=True)
    print("off")
    
myFontCurr = font.Font(family='Helvetica', size=15, weight='bold')

ct=0
def current():
    global ampere
    global ct
    print(ampere_limit)
    am=ser.readline()
    am=am.decode('utf-8')[:4]
    print(am)
    ampere=math.floor(float(am))
    if(ampere>0):
        ampere=ampere-1
    print("ampere=",ampere)
    if(ct==0):
        time.sleep(2)
        ct=1
    if("0.0" in str(am)):
        stri="Wait"
    else:
        stri="Ampere: "+ str(ampere)
    w = Label(win, text=stri, font=myFontCurr)
    w.grid(row=3, column=5, padx=(4, 30), pady=(90,10))

    '''
    if (ampere < 10):
        stri = "Ampere: 0" + str(ampere)
    elif (ampere >= 10):
        stri = "Ampere: " + str(ampere)
    
    
    # w.pack(side=RIGHT)
    if (ampere == 99):
        # time.sleep(5)
        ampere = 0
    ampere = ampere + 1
    '''
    w.after(250, current)


win.title("Cont: 0346-2791445")
#win.geometry('800x480')
RWidth=win.winfo_screenwidth()
RHeight=win.winfo_screenheight()
win.wm_attributes("-type",'splash')
win.wm_attributes("-fullscreen",True)
#win.overrideredirect(True)
win.geometry(("%dx%d")%(RWidth,RHeight+20))
win.resizable(False, False)
text = Text(win)


headerFont= font.Font(family = 'Helvetica', size = 22, weight = 'bold')
w = Label(win, text="AL-RAHIM CONTROLLED ATMOSPHERIC STORAGE (PVT.)", font=headerFont)
#w = Label(win, text="          CONTROLLED ATMOSPHERIC STORAGE (PVT.)", font=headerFont)

w.grid(row=1, column=2, padx=(4, 4), pady=(40,4))
w.place(x = 100, y = 40)

m1_button = Button(win, text="Pump: 1", font=myFont, command=m1_on_off, height=2, width=8, bg=b1)
m1_button.grid(row=button_row + 2, column=0, padx=10, pady=20)

m2_button = Button(win, text="Pump: 2", font=myFont, command=m2_on_off, height=2, width=8, bg=b2)
m2_button.grid(row=button_row + 2, column=1, padx=20, pady=6)

m3_button = Button(win, text="Pump: 3", font=myFont, command=m3_on_off, height=2, width=8, bg=b2)
m3_button.grid(row=button_row + 2, column=2, padx=20, pady=6)

m4_button = Button(win, text="Pump: 4", font=myFont, command=m4_on_off, height=2, width=8, bg=b2)
m4_button.grid(row=button_row + 2, column=3, padx=20, pady=6)

m5_button = Button(win, text="Pump: 5", font=myFont, command=m5_on_off, height=2, width=8, bg=b2)
m5_button.grid(row=button_row + 2, column=4, padx=20, pady=6)

m6_button = Button(win, text="Pump: 6", font=myFont, command=m6_on_off, height=2, width=8, bg=b1)
m6_button.grid(row=button_row + 2, column=5, padx=(16,35), pady=6)


m7_button = Button(win, text="Pump: 7", font=myFont, command=m7_on_off, height=2, width=8, bg=b2)
m7_button.grid(row=button_row + 3, column=0, padx=10, pady=6)

m8_button = Button(win, text="Pump: 8", font=myFont, command=m8_on_off, height=2, width=8, bg=b2)
m8_button.grid(row=button_row + 3, column=1, padx=20, pady=6)

m9_button = Button(win, text="Pump: 9", font=myFont, command=m9_on_off, height=2, width=8, bg=b2)
m9_button.grid(row=button_row + 3, column=2, padx=20, pady=6)

m10_button = Button(win, text="Pump: 10", font=myFont, command=m10_on_off, height=2, width=8, bg=b2)
m10_button.grid(row=button_row + 3, column=3, padx=20, pady=6)

m11_button = Button(win, text="Pump: 11", font=myFont, command=m11_on_off, height=2, width=8, bg=b1)
m11_button.grid(row=button_row + 3, column=4, padx=20, pady=6)

m12_button = Button(win, text="Pump: 12", font=myFont, command=m12_on_off, height=2, width=8, bg=b2)
m12_button.grid(row=button_row + 3, column=5, padx=(16,35), pady=6)

m13_button = Button(win, text="Pump: 13", font=myFont, command=m13_on_off, height=2, width=8, bg=b2)
m13_button.grid(row=button_row + 4, column=0, padx=20, pady=10)

m14_button = Button(win, text="Pump: 14", font=myFont, command=m14_on_off, height=2, width=8, bg=b2)
m14_button.grid(row=button_row + 4, column=1, padx=20, pady=6)

m15_button = Button(win, text="Pump: 15", font=myFont, command=m15_on_off, height=2, width=8, bg=b2)
m15_button.grid(row=button_row + 4, column=2, padx=20, pady=6)

m16_button = Button(win, text="Pump: 16", font=myFont, command=m16_on_off, height=2, width=8, bg=b1)
m16_button.grid(row=button_row + 4, column=3, padx=20, pady=6)

m17_button = Button(win, text="Pump: 17", font=myFont, command=m17_on_off, height=2, width=8, bg=b2)
m17_button.grid(row=button_row + 4, column=4, padx=20, pady=6)

m18_button = Button(win, text="Pump: 18", font=myFont, command=m18_on_off, height=2, width=8, bg=b2)
m18_button.grid(row=button_row + 4, column=5, padx=(16,35), pady=6)

m19_button = Button(win, text="Pump: 19", font=myFont, command=m19_on_off, height=2, width=8, bg=b2)
m19_button.grid(row=button_row + 5, column=0, padx=20, pady=10)

m20_button = Button(win, text="Pump: 20", font=myFont, command=m20_on_off, height=2, width=8, bg=b2)
m20_button.grid(row=button_row + 5, column=1, padx=20, pady=4)

m21_button = Button(win, text="Pump: 21", font=myFont, command=m21_on_off, height=2, width=8, bg=b2)
m21_button.grid(row=button_row + 5, column=2, padx=20, pady=4)


m22_button = Button(win, text="Pump: 22", font=myFont, command=m22_on_off, height=2, width=8, bg=b2)
m22_button.grid(row=button_row + 5, column=3, padx=20, pady=4)

m23_button = Button(win, text="Pump: 23", font=myFont, command=m23_on_off, height=2, width=8, bg=b2)
m23_button.grid(row=button_row + 5, column=4, padx=20, pady=4)

m24_button = Button(win, text="Pump: 24", font=myFont, command=m24_on_off, height=2, width=8, bg=b2)
m24_button.grid(row=button_row + 5, column=5, padx=(16,35), pady=4)

photo=PhotoImage(file="/home/pi/Documents/tool.png")
photo = photo.subsample(4, 4)
b = Button(win,image=photo, command=exitProgram,height=30, width=165)
b.place(x=840,y=560)

pow=PhotoImage(file="/home/pi/Documents/power.png")
pow = pow.subsample(5, 5)
pw = Button(win,image=pow, command=sysOff,height=50, width=50)
pw.place(x=20,y=80)

footerFont= font.Font(family = 'Helvetica', size = 14, weight = 'bold')
w = Label(win, text="Talha Ahmed, Contractor and supplier. Contact: 0333-3394352, 0346-2791445",fg="grey", font=footerFont)

w.grid(row=1, column=2, padx=(4, 4), pady=4)
w.place(x = 70, y = 565)



current()
    
win.mainloop()





