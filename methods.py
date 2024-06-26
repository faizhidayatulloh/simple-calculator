from colorama import Fore,init,Style
init()
def jumlah():
	def ubah(nilai):
		try :
			return float(nilai)
		except ValueError:
			return None
	hasil=0
	no=2
	while True:
		print('Type "x" to exit !')
		a=input('Number ------- 1th : ')
		if a =='x':
			break
		rubah_a = ubah(a)
		if rubah_a is not None:
			a=float(a)
		else:
			print("________________")
			print("Number Only !")
			print("_________________")
			continue
		b=input('Number --------2th : ')
		if b =="x":
			break
		rubah_b = ubah(b)
		if rubah_b is not None:
			b=float(b)
		else:
			print("________________")
			print("Number Only !")
			print("_________________")
			continue
		hasil=a+b
		print(f'                                               = {hasil}')
		if hasil!='x':
			break
	print('Type lower "x" to exit additoin !')
	while True:
		if a=='x':
			break
		elif b=="x":
			break
		no+=1
		a=input(f'Number -------{no}th: ')
		if a=='x':
			break
		rubah = ubah(a)
		if rubah is not None:
			a=float(a)
		else:
			print("Number Only!!")
			no-=1
			continue
		hasil=hasil+a
		print(f'                                                = {hasil}')
	print(f'                                              total = {hasil}')


def kurang():
	def ubah(nilai):
		try :
			return float(nilai)
		except ValueError:
			return None
	hasil=0
	no=2
	while True:
		print('Type "x" to exit !')
		a=input('Number ------- 1th : ')
		if a =='x':
			break
		rubah_a = ubah(a)
		if rubah_a is not None:
			a=float(a)
		else:
			print("________________")
			print("Number Only !")
			print("_________________")
			continue
		b=input('Number --------2th : ')
		if b =="x":
			break
		rubah_b = ubah(b)
		if rubah_b is not None:
			b=float(b)
		else:
			print("________________")
			print("Number Only !")
			print("_________________")
			continue
		hasil=a-b
		print(f'                                               = {hasil}')
		if hasil!='x':
			break
	print('Type lower "x" to exit additoin !')
	while True:
		if a=='x':
			break
		elif b=="x":
			break
		no+=1
		a=input(f'Number -------{no}th: ')
		if a=='x':
			break
		rubah = ubah(a)
		if rubah is not None:
			a=float(a)
		else:
			print("Number Only!!")
			no-=1
			continue
		hasil=hasil-a
		print(f'                                                = {hasil}')
	print(f'                                              total = {hasil}')

def kali():
	def ubah(nilai):
		try :
			return float(nilai)
		except ValueError:
			return None
	hasil=0
	no=2
	while True:
		print('Type "x" to exit !')
		a=input('Number ------- 1th : ')
		if a =='x':
			break
		rubah_a = ubah(a)
		if rubah_a is not None:
			a=float(a)
		else:
			print("________________")
			print("Number Only !")
			print("_________________")
			continue
		b=input('Number --------2th : ')
		if b =="x":
			break
		rubah_b = ubah(b)
		if rubah_b is not None:
			b=float(b)
		else:
			print("________________")
			print("Number Only !")
			print("_________________")
			continue
		hasil=a*b
		print(f'                                               = {hasil}')
		if hasil!='x':
			break
	print('Type lower "x" to exit additoin !')
	while True:
		if a=='x':
			break
		elif b=="x":
			break
		no+=1
		a=input(f'Number -------{no}th: ')
		if a=='x':
			break
		rubah = ubah(a)
		if rubah is not None:
			a=float(a)
		else:
			print("Number Only!!")
			no-=1
			continue
		hasil=hasil*a
		print(f'                                                = {hasil}')
	print(f'                                              total = {hasil}')

def bagi():
	def ubah(nilai):
		try :
			return float(nilai)
		except ValueError:
			return None
	hasil=0
	no=2
	while True:
		print('Type "x" to exit !')
		a=input('Number ------- 1th : ')
		if a =='x':
			break
		rubah_a = ubah(a)
		if rubah_a is not None:
			a=float(a)
		else:
			print("________________")
			print("Number Only !")
			print("_________________")
			continue
		b=input('Number --------2th : ')
		if b =="x":
			break
		rubah_b = ubah(b)
		if rubah_b is not None:
			b=float(b)
		else:
			print("________________")
			print("Number Only !")
			print("_________________")
			continue
		hasil=a/b
		print(f'                                               = {hasil}')
		if hasil!='x':
			break
	print('Type lower "x" to exit additoin !')
	while True:
		if a=='x':
			break
		elif b=="x":
			break
		no+=1
		a=input(f'Number -------{no}th: ')
		if a=='x':
			break
		rubah = ubah(a)
		if rubah is not None:
			a=float(a)
		else:
			print("Number Only!!")
			no-=1
			continue
		hasil=hasil/a
		print(f'                                                = {hasil}')
	print(f'                                              total = {hasil}')