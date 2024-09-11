password = 'a12345'
y = 3 # input times limitation
while y > 0:
	pwd = input ('please input password: ')
	if pwd == password:
		print ('log in sucessfully')
		break  #jump out loop
	else:
		y = y - 1
		print ('pw is incorrect! you still have', y,'chance')
		# if y == 0:	//if use while True
		#	break		//if use while True