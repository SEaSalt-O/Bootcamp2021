# GUITranslator.py

#จาก Librera : tkinter, * คือให้ดึงความสามารถหลักมาทั้งหมด
from tkinter import *

from tkinter import ttk #ttk is them of tk

from googletrans import Translator #เรียก Google Translate เข้ามา
translator = Translator()

#สร้างหน้าต่างหลัก
GUI = Tk()
GUI.geometry('500x300') #ขยายขนาดหน้าจอ กว้างxสูง
GUI.title('โปรแกรมแปลภาษา by Big')
#-------config------
FONT = ('Angsana New',14)
#-------Label------

L = ttk.Label(GUI,text='กรุณากรอกคำศัพท์ที่ต้องการแปล',font=FONT)
L.pack()

#-------Entry(ช่องกรอกข้อความ)------
v_vocab = StringVar()#กล่องเก็บข้อความ

E1 = ttk.Entry(GUI,textvariable = v_vocab,font=FONT,width=40)
E1.pack(pady=20)


#-------Buttom(ปุ่มแปล)------------
def Translate():
    vocab = v_vocab.get()#.get คือให้แสดงผลออกมา
    meaning = translator.translate(vocab,dest='th')
    print( vocab + ' : ' + meaning.text)
    print( meaning.pronunciation)
    v_result.set(vocab + ' : ' + meaning.text)

B1 = ttk.Button(GUI,text='Translate',command=Translate) #ปุ่มจาก ttk สวยขึ้น
B1.pack(ipadx=20,ipady=10) # show ปุ่มขึ้นมาวางจากบนลงล่าง

#-------Label------

L = ttk.Label(GUI,text='คำแปล',font=FONT)
L.pack()

#-------Result------
v_result = StringVar()#กล่องเก็บคำแปล
FONT2 = ('Angsana New',20)
R1 = ttk.Label(GUI,textvariable = v_result,font=FONT2, foreground='green')
R1.pack()



#Mainloop คือให้โปรแกรม Run ได้ตลอดเวลา โดยไม่ต้องเขียน Code ใหม่จนกว่าปิดโปรแกรม
#GUI.mainloop() ต้องอยู่บรรทัดสุดท้ายเท่านั้น
GUI.mainloop()

