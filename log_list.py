Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> garage = ['Toyota','Honda','Izusu']
>>> garage.append('Suzuki')#append ใช้ในการเพิ่มค่าใหม่ลงใน List
>>> print garage
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(garage)?
>>> print(garange)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(garange)
NameError: name 'garange' is not defined
>>> print(garage)
['Toyota', 'Honda', 'Izusu', 'Suzuki']
>>> print.garage
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print.garage
AttributeError: 'builtin_function_or_method' object has no attribute 'garage'
>>> print(garage)
['Toyota', 'Honda', 'Izusu', 'Suzuki']
>>> print(garage[2])
Izusu
>>> garage.remove('Honda')
>>> print(garage)
['Toyota', 'Izusu', 'Suzuki']
>>> garage.insert(1,'Benz')
>>> print(garage)
['Toyota', 'Benz', 'Izusu', 'Suzuki']
>>> del garage[2]
>>> print(garage)
['Toyota', 'Benz', 'Suzuki']
>>> print(garage[-1])
Suzuki
>>> print(garage[-2])
Benz
>>> print(garage)
['Toyota', 'Benz', 'Suzuki']
>>> mycar = garage.pop(-1)
>>> print(mycar)
Suzuki
>>> print(garage)
['Toyota', 'Benz']
>>> garage.append('Suzuki')
>>> print(garage)
['Toyota', 'Benz', 'Suzuki']
>>> garage[1] = 'Tesla'
>>> print(garage)
['Toyota', 'Tesla', 'Suzuki']
>>> print(len(garage))
3
>>> user  = ['z','r','t','b','n','p']
>>> user.soft()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    user.soft()
AttributeError: 'list' object has no attribute 'soft'
>>> use.sort()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    use.sort()
NameError: name 'use' is not defined
>>> user.sort()
>>> users  = ['z','r','t','b','n','p']
>>> users.sort()
>>> 
>>> print(user)
['b', 'n', 'p', 'r', 't', 'z']
>>> users.sort(reverse=True)
>>> users
['z', 't', 'r', 'p', 'n', 'b']
>>> print.(sorted(users))
SyntaxError: invalid syntax
>>> print.(sorted(users))
SyntaxError: invalid syntax
>>> print(users)
['z', 't', 'r', 'p', 'n', 'b']
>>> users  = ['z','r','t','b','n','p']
>>> users.reverse()
>>> print(users)
['p', 'n', 'b', 't', 'r', 'z']
>>> for u in users:
	print(u)

	
p
n
b
t
r
z
>>> for u in sorted(users):
	print(u)

	
b
n
p
r
t
z
>>> for u in sorted.reverse(users):
	print(u)

	
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    for u in sorted.reverse(users):
AttributeError: 'builtin_function_or_method' object has no attribute 'reverse'
>>> users.revese()
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    users.revese()
AttributeError: 'list' object has no attribute 'revese'
>>> users.reverse()
>>> for u in users():
	print(u)

	
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    for u in users():
TypeError: 'list' object is not callable
>>> users  = ['z','r','t','b','n','p']
>>> users.reverse()
>>> for u in users:
	print(u)

	
p
n
b
t
r
z
>>> for u in users:
	print('สวัสดีทุกคน',u)
	print('สวัสดี'+u)

	
สวัสดีทุกคน p
สวัสดีp
สวัสดีทุกคน n
สวัสดีn
สวัสดีทุกคน b
สวัสดีb
สวัสดีทุกคน t
สวัสดีt
สวัสดีทุกคน r
สวัสดีr
สวัสดีทุกคน z
สวัสดีz
>>> 