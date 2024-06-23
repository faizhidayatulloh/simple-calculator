from colorama import Fore,init,Style
init()
print(Style.BRIGHT)
print(Fore.BLUE	)
import methods
print("Simple Calculator")
print("_________________")
while True:
	print('1.addition\n2.substractin\n3.multiplication\n4.division\n0.exit')
	print("__________________________")
	pilih=input('Choose :')
	if pilih== "1":
		methods.jumlah()
	elif pilih== "2":
		methods.kurang()
	elif pilih=='3':
		methods.kali()
	elif pilih=="4":
		methods.bagi()
	elif pilih == "0":
		print("GOOD BYE !!!")
		break
	else:
		print("___________________")
		print("Only 1,2,3,4 or 0")
		print("____________________")





print('------------------------')
print('THANK YOU VERY MUCH')
print('=========================')