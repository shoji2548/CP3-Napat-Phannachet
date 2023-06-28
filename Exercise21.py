from tkinter import *
import math
def leftClickButton(event):
    BMI = round(float(textboxWeight.get())/math.pow(float(textboxHight.get())/100,2),1)
    labelResult.configure(text=BMI)
    if BMI >= 30.0 :
        labelPhyCondition.configure(text="อ้วนมาก")
    elif BMI <= 29.9 :
        labelPhyCondition.configure(text="อ้วน")
    elif 23.0 <= BMI <= 24.9 :
        labelPhyCondition.configure(text='น้ำหนักเกิน')
    elif 18.6 <= BMI <= 22.9 :
        labelPhyCondition.configure(text='น้ำหนักปกติ เหมาะสม')
    else:
        labelPhyCondition.configure(text='ผอนเกินไป')


MainWindow = Tk()
labelHight = Label(MainWindow,text='ส่วนสูง(cm)',font=('Tahoma',10)).grid(row=0,column=0)
textboxHight = Entry(MainWindow)
textboxHight.grid(row=0,column=1)
labelWeight = Label(MainWindow,text='น้ำหนัก(kg)',font=('Tahoma',10)).grid(row=1,column=0)
textboxWeight = Entry(MainWindow)
textboxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text='คำนวณ',font=('Tahoma',10))
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2,column=0)
labelResult = Label(MainWindow,text='ผลลัพธ์',font=('Tahoma',10))
labelResult.grid(row=2,column=1)
labelPhyCondition = Label(MainWindow,text='สภาพร่างกาย',font=('Tahoma',10))
labelPhyCondition.grid(row=3,column=1)
MainWindow.mainloop()