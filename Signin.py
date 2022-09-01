from time import sleep
your_username = input('nhap ten username: ')
your_password = input('nhap password: ')
print('waiting...')
sleep(3)
print('----------------------------------------------')
print('                  Sign in                     ')
user = input('user: ')
password = input('password: ')
if user == your_username and password == your_password:
	input('Dang nhap thanh cong')
else:
	input('Dang nhap fail roi')
check = {user : your_username, password : your_password }
if user != check[your_username]:
	print(True)
