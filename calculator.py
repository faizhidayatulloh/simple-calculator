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
print("___________________")
print('type "000" to exit')
print("__________________")
pilih=input('choose: ')
if pilih== "1":
	methods.jumlah()
elif pilih=="2":
	methods.kurang()
elif pilih=="3":
	methods.kali()
elif pilih=="4":
	methods.bagi()
elif pilih == "000":
	print('Good Bye !!!')
else:
	print('just choose 1, 2, 3 or 4')





print('------------------------')
print('THANK YOU VERY MUCH')
print('=========================')