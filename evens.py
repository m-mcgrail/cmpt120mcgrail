Python 3.5.4 (v3.5.4:3f56838, Aug  8 2017, 02:17:05) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> for i in range(10):
	print(i)

	
0
1
2
3
4
5
6
7
8
9
>>> 
======================= RESTART: C:/Python35/evens.py =======================
0
1
2
3
4
5
6
7
8
9
>>> for i in range(10):
	print(2i)
	
SyntaxError: invalid syntax
>>> for i in range(10):
	print(2 x i)
	
SyntaxError: invalid syntax
>>> for i in range(10):
	print(2 * i)

	
0
2
4
6
8
10
12
14
16
18
>>> 
>>> for i in range(11):
	print(2 * i)

	
0
2
4
6
8
10
12
14
16
18
20
>>> for i in range(1 to 11):
	print(2 * i)
	
SyntaxError: invalid syntax
>>> for i in range(1, 11):
	print(2 * i)

	
2
4
6
8
10
12
14
16
18
20
>>> 
======================= RESTART: C:/Python35/evens.py =======================
0
1
2
3
4
5
6
7
8
9
2
4
6
8
10
12
14
16
18
20
>>> 
======================= RESTART: C:/Python35/evens.py =======================
2
4
6
8
10
12
14
16
18
20
>>> for i in range (1, 11):
	print(2 * i)

	
2
4
6
8
10
12
14
16
18
20
>>> 
