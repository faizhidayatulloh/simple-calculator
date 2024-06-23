def jumlah():
	hasil=0
	no=2
	print('type "x" to exit !')
	while True:
		a=input('Number ------- 1th : ')
		b=input('Number --------2th : ')
		a=float(a)
		b=float(b)
		hasil=a+b
		print(f'hasil = ({hasil})')
		if hasil!='x':
			break
	while True:
		print('Type "x" to exit addition !')
		no+=1
		a=input(f'Number -------{no}th: ')
		if a=='x':
			break
		a=float(a)
		hasil=hasil+a
		print(f'hasil = ({hasil})')
	print(f'                            total = {hasil}')

def kurang():
	hasil=0
	no=2
	print('Type "x" to exit !')
	while True:
		a=input('Number ------- 1th : ')
		b=input('Number --------2th : ')
		a=int(a)
		b=int(b)
		hasil=a-b
		print(f'{no}.hasil = ({hasil})')
		if hasil!='x':
			break
	while True:
		no+=1
		a=input(f'Number -------{no}th: ')
		if a=='x':
			break
		a=int(a)
		hasil-=a
		print(f'hasil = ({hasil})')
	print(f'                              total = {hasil}')
def kali():
	hasil=0
	no=2
	print('Type "x" to exit !')
	while True:
		a=input('Number ------- 1th : ')
		b=input('Number --------2th : ')
		a=float(a)
		b=float(b)
		hasil=a*b
		print(f'hasil = ({hasil})')
		if hasil!='x':
			break
	while True:
		no+=1
		a=input(f'Number -------{no}th: ')
		if a=='x':
			break
		a=float(a)
		hasil*=a
		print(f'hasil = ({hasil})')
	print(f'            total = {hasil}')
def bagi():
	hasil=0
	no=2
	print('Type "x" to exit !')
	while True:
		a=input('Number ------- 1th : ')
		b=input('Number --------2th : ')
		a=int(a)
		b=int(b)
		hasil=a/b
		print(f'hasil = ({hasil})')
		if hasil!='x':
			break
	while True:
		no+=1
		a=input(f'Number -------{no}th: ')
		if a=='x':
			break
		a=int(a)
		hasil/=a
		print(f'hasil = ({hasil})')
	print(f'                total = {hasil}')