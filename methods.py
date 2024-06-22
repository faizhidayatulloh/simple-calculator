def jumlah():
	hasil=0
	no=2
	print('type "x" to end')
	while True:
		a=input('angka ke ------- 1 : ')
		b=input('angka ke --------2 : ')
		a=float(a)
		b=float(b)
		hasil=a+b
		print(f'hasil = ({hasil})')
		if hasil!='x':
			break
	while True:
		no+=1
		a=input(f'angka ke -------{no}: ')
		if a=='x':
			break
		a=float(a)
		a=float(a)
		hasil=hasil+a
		print(f'hasil = ({hasil})')
	print(f'                            total = {hasil}')

def kurang():
	hasil=0
	no=2
	print('ketik "x" untuk keluar.')
	while True:
		a=input('angka ke ------- 1 : ')
		b=input('angka ke --------2 : ')
		a=int(a)
		b=int(b)
		hasil=a-b
		print(f'{no}.hasil = ({hasil})')
		if hasil!='x':
			break
	while True:
		no+=1
		a=input(f'angka ke -------{no}: ')
		if a=='x':
			break
		a=int(a)
		hasil-=a
		print(f'hasil = ({hasil})')
	print(f'                              total = {hasil}')
def kali():
	hasil=0
	no=2
	print('ketik "x" untuk keluar')
	while True:
		a=input('angka ke ------- 1 : ')
		b=input('angka ke --------2 : ')
		a=float(a)
		b=float(b)
		hasil=a*b
		print(f'hasil = ({hasil})')
		if hasil!='x':
			break
	while True:
		no+=1
		a=input(f'angka ke -------{no}: ')
		if a=='x':
			break
		a=float(a)
		hasil*=a
		print(f'hasil = ({hasil})')
	print(f'            total = {hasil}')
def bagi():
	hasil=0
	no=2
	print('ketik "x" untuk keluar')
	while True:
		a=input('angka ke ------- 1 : ')
		b=input('angka ke --------2 : ')
		a=int(a)
		b=int(b)
		hasil=a/b
		print(f'hasil = ({hasil})')
		if hasil!='x':
			break
	while True:
		no+=1
		a=input(f'angka ke -------{no}: ')
		if a=='x':
			break
		a=int(a)
		hasil/=a
		print(f'hasil = ({hasil})')
	print(f'                total = {hasil}')