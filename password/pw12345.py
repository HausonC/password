password = 'a12345'
y = 3 # input times limitation
# while True:
while y > 0:
	y = y - 1
	pwd = input ('please input password: ')
	if pwd == password:
		print ('log in sucessfully')
		break  #jump out loop
	else:
		if y > 0:
			print ('pw is incorrect! you still have', y,'chance')
		else:
			print ('your account is locked, please contact IT')
		# if y == 0:	//if use while True
		#	break		//if use while True