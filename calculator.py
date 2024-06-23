from colorama import Fore,init,Style
init()
print(Style.BRIGHT)
print(Fore.BLUE	)
import methods
print('calkulator')
print('============')
print('1.addition ')
print('2.subtraction')
print('3.multiplication')
print('4.division')
print('0.exit')
print("___________________")
while True:
	pilih=input('choose: ("0" to exit calculator !) ')
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