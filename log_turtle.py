Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> tao = turtle.Turtle()
>>> tao.shape('turtle')
>>> tao.forward(100) #Turtle ใช้ในการเรียนภาษาโปรแกรม เพื่อให้เข้าในเรื่องของ Movement
>>> tao.left(90)
>>> tao.forward(100)
>>> tao.left(90)
>>> tao.forward(100)
>>> tao.left(90)
>>> tao.forward(100)
>>> tao.left(90)
>>> tao.reset()
>>> for i in range(4):
	tao.forward(100)
	tao.roght(90)

	
Traceback (most recent call last):
  File "<pyshell#15>", line 3, in <module>
    tao.roght(90)
AttributeError: 'Turtle' object has no attribute 'roght'
>>> tao.reset
<bound method RawTurtle.reset of <turtle.Turtle object at 0x000001EB6F8DC490>>
>>> tao.reset()
>>> for i in range(4):
	tao.forward(100)
	tao.right(90)

	
>>> range(4)
range(0, 4)
>>> list(range(4))
[0, 1, 2, 3]
>>> for i in range(5):
	print(i)

	
0
1
2
3
4
>>> for i in [10,50,90]:
	print(i)

	
10
50
90
>>> tao.reset()
>>> for i in range(4):
	tao.forward(100)
	tao.right(90)
	print('No.',i)

	
No. 0
No. 1
No. 2
No. 3
>>> tao.reset()
>>> for i range(4):
	
SyntaxError: invalid syntax
>>> for i in range(4):
	tao.forward(100)
	tao.left(45)
	print('No.',i)

	
No. 0
No. 1
No. 2
No. 3
>>> for i in range(8):
	tao.forward(100)
	tao.left(45)
	print('No.',i)

	
No. 0
No. 1
No. 2
No. 3
No. 4
No. 5
No. 6
No. 7
>>> tao.reset()
>>> for i in range(8):
	tao.forward(100)
	tao.left(45)
	print('No.',i)

	
No. 0
No. 1
No. 2
No. 3
No. 4
No. 5
No. 6
No. 7
>>> tao.reset()
>>> for i in range(8):
	tao.forward(100)
	tao.left(45)
	print('No.',i)

	
No. 0
No. 1
No. 2
No. 3
No. 4
No. 5
No. 6
No. 7
>>> for i in range(4):
	for j in range(8):
		tao.forward(100)
		tao.left(45)
	print ('8 เหลี่ยมรูปที่',i)

	
8 เหลี่ยมรูปที่ 0
8 เหลี่ยมรูปที่ 1
8 เหลี่ยมรูปที่ 2
8 เหลี่ยมรูปที่ 3
>>> for i in range(4):
	for j in range(8):
		tao.forward(100)
		tao.left(45)
	print ('8 เหลี่ยมรูปที่',i)
	tao.left(90)

	
8 เหลี่ยมรูปที่ 0
8 เหลี่ยมรูปที่ 1
8 เหลี่ยมรูปที่ 2
8 เหลี่ยมรูปที่ 3
>>> tao.reset()
>>> for i in range(4):
	for j in range(8):
		tao.forward(100)
		tao.left(45)
	print ('8 เหลี่ยมรูปที่',i)
	tao.left(180)

	
8 เหลี่ยมรูปที่ 0
8 เหลี่ยมรูปที่ 1
8 เหลี่ยมรูปที่ 2
8 เหลี่ยมรูปที่ 3
>>> for i in range(4):
	for j in range(8):
		tao.forward(100)
		tao.left(45)
	print ('8 เหลี่ยมรูปที่',i)
	tao.left(180)

	
Traceback (most recent call last):
  File "<pyshell#61>", line 3, in <module>
    tao.forward(100)
  File "C:\Python\lib\turtle.py", line 1638, in forward
    self._go(distance)
  File "C:\Python\lib\turtle.py", line 1606, in _go
    self._goto(ende)
  File "C:\Python\lib\turtle.py", line 3159, in _goto
    screen._pointlist(self.currentLineItem),
  File "C:\Python\lib\turtle.py", line 756, in _pointlist
    cl = self.cv.coords(item)
  File "<string>", line 1, in coords
  File "C:\Python\lib\tkinter\__init__.py", line 2763, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"
>>> import turtle
>>> 
>>> 
>>> tao = turtle.Turtle()
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    tao = turtle.Turtle()
  File "C:\Python\lib\turtle.py", line 3814, in __init__
    RawTurtle.__init__(self, Turtle._screen,
  File "C:\Python\lib\turtle.py", line 2558, in __init__
    self._update()
  File "C:\Python\lib\turtle.py", line 2661, in _update
    self._update_data()
  File "C:\Python\lib\turtle.py", line 2647, in _update_data
    self.screen._incrementudc()
  File "C:\Python\lib\turtle.py", line 1293, in _incrementudc
    raise Terminator
turtle.Terminator
>>> tao.shape('turtle')
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    tao.shape('turtle')
  File "C:\Python\lib\turtle.py", line 2779, in shape
    self._update()
  File "C:\Python\lib\turtle.py", line 2661, in _update
    self._update_data()
  File "C:\Python\lib\turtle.py", line 2651, in _update_data
    self.screen._drawline(self.currentLineItem, self.currentLine,
  File "C:\Python\lib\turtle.py", line 546, in _drawline
    self.cv.coords(lineitem, *cl)
  File "<string>", line 1, in coords
  File "C:\Python\lib\tkinter\__init__.py", line 2763, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"
>>> tao.shape('turtle')
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    tao.shape('turtle')
  File "C:\Python\lib\turtle.py", line 2779, in shape
    self._update()
  File "C:\Python\lib\turtle.py", line 2661, in _update
    self._update_data()
  File "C:\Python\lib\turtle.py", line 2651, in _update_data
    self.screen._drawline(self.currentLineItem, self.currentLine,
  File "C:\Python\lib\turtle.py", line 546, in _drawline
    self.cv.coords(lineitem, *cl)
  File "<string>", line 1, in coords
  File "C:\Python\lib\tkinter\__init__.py", line 2763, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"
>>> import turtle
>>> tao = turtle.Turtle()
>>> tao.shape('turtle')
>>> for i in range(4):
	for j in range(8):
		tao.forward(100)
		tao.left(45)
	print ('8 เหลี่ยมรูปที่',i)
	tao.left(135)

	
8 เหลี่ยมรูปที่ 0
8 เหลี่ยมรูปที่ 1
8 เหลี่ยมรูปที่ 2
8 เหลี่ยมรูปที่ 3
>>> tao.reset
<bound method RawTurtle.reset of <turtle.Turtle object at 0x000001EB6F9B6CD0>>
>>> tao.reset()
>>> for i in range(10):
	for j in range(8):
		tao.forward(100)
		tao.left(45)
	print ('8 เหลี่ยมรูปที่',i)
	tao.left(36)

	
8 เหลี่ยมรูปที่ 0
8 เหลี่ยมรูปที่ 1
8 เหลี่ยมรูปที่ 2
8 เหลี่ยมรูปที่ 3
8 เหลี่ยมรูปที่ 4
8 เหลี่ยมรูปที่ 5
8 เหลี่ยมรูปที่ 6
8 เหลี่ยมรูปที่ 7
8 เหลี่ยมรูปที่ 8
8 เหลี่ยมรูปที่ 9
>>> tao.reset()
>>> def regtangle():
	for i in range(4):
		tao.forward(100)
		tao.left(90)

		
>>> regtangle()
>>> tao.reset()
>>> for i in range(10):
	regtangle()
	tao.left(36)

	
>>> 