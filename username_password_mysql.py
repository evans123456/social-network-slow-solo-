
import pymysql

conn = pymysql.connect(host = 'localhost',user = 'root',passwd='',db='users')

myCursor = conn.cursor()#allows you to execute queries in mysql

print('------- CHOOSE --------')
print('0 :SEARCH IF USERNAME EXISTS')
print('1 :CREATE NEW USERNAME AND PASSWORD')
print('2 :UPDATE EXISTING USERNAME AND PASSWORD')
print('3 :DELETE EXISTING USERNAME AND PASSWORD')

ans = int(input('PLEASE SELECT AN OPTION:  '))




#################################################################################################################### CREATE USER
if ans == 1:

	#create a new user (need to check bring the search function here)
	print('CREATE A NEW ACCOUNT')
	uname =input('ENTER USERNAME:  ')
	passord =input('ENTER PASSWORD: ')

	search = uname
	
	sqlSEARCH = "SELECT UserID,user_Name , Password FROM `userName_Password` WHERE user_Name like  %s "  


	val = myCursor.execute(sqlSEARCH,search)

	if val == 1:
		print('USERNAME ALREADY EXISTS')

	else:
		print('value was not found ')
		print('name has been accepted')

		#insrt to db area
		sqlinsert = "INSERT INTO username_password(user_Name,password) VALUES ( %s , %s)" #
		myCursor.execute(sqlinsert, (uname, passord))
		print('!!!!!!!!successfull!!!!!!')
		conn.commit()
		conn.close()




#################################################################################################################### UPDATE EXISTING USERNAME
elif ans ==2:
	#update username or password
	print('UPDATE EXISTING USERNAME AND PASSWORD\n')
	print('1) CHANGE USERNAME')
	print('2) CHANGE PASSWORD')

	choice = int(input('ENTER YOUR CHOICE 1/2:  '))

	if choice == 1:
		#wants to change username only


		search = input('ENTER YOUR USERNAME: ')
		#search if value exists in the database
		


		sqlSEARCH = "SELECT UserID,user_Name , Password FROM `userName_Password` WHERE user_Name like  %s "  


		val = myCursor.execute(sqlSEARCH,search)

		if val == 1:
			#after finding value in db
			print('value found')
			#prevname = input('ENTER YOUR CURRENT USERNAME:  ')
			newname = str(input('ENTER NEW USERNAME: '))


			sqlupdate = "UPDATE username_password SET User_Name= %s WHERE User_Name = %s;"

			myCursor.execute(sqlupdate,(newname,search))

			print('!!!!!!!!successfull!!!!!!')
			conn.commit()
			conn.close()

		else:
			print('USERNAME DOES NOT EXIST')


	elif choice == 2:
		#wants to change password
		search = input('ENTER YOUR USERNAME: ')
		#search if value exists in the database
		


		sqlSEARCH = "SELECT UserID,user_Name , Password FROM `userName_Password` WHERE user_Name like  %s "  


		val = myCursor.execute(sqlSEARCH,search)
		#after finding value in db
		print('value found')
		#prevname = input('ENTER YOUR CURRENT USERNAME:  ')
		npassword = str(input('ENTER NEW PASSWORD: '))

#find the mysql statement....trying to get the mysql statement that from the username will go to the password column and edit it
		sqlupdatepass = "UPDATE username_password SET `Password`= %s WHERE User_Name = %s;"

		myCursor.execute(sqlupdatepass,(npassword,search))

		print('!!!!!!!!successfull!!!!!!')
		conn.commit()
		conn.close()
		


		pass

	else:
		print('INVALID OPTION')




#################################################################################################################### DELETE

elif ans == 3:
	print('DELETE YOUR ACCOUNT')

	deluname = input('ENTER YOUR USERNAME: ')
	delpass = input('ENTER YOUR PASSWORD: ')

	sqlDELETE = "DELETE FROM username_password WHERE User_Name = %s AND Password = %s ;"

	
	choice = int(input('ARE YOU SURE (\n1 - YES\n2 - NO)\n: '))
	if choice == 1:

		myCursor.execute(sqlDELETE, (deluname, delpass))
		print('!!!!!!!!successfull!!!!!!')
		conn.commit()
		conn.close()

	elif choice == 2:

		sys.exit()

	else:
		print('here')
		print('INVALID CHOICE ')







#################################################################################################################### SEARCH

elif ans == 0:
	#search only
	search = input('Enter name to search')

	sqlSEARCH = "SELECT UserID,user_Name , Password FROM `userName_Password` WHERE user_Name like  %s "  


	val = myCursor.execute(sqlSEARCH,search)

	if val == 1:
		print('value found')

	else:
		print('value was not found')

else:
	print('YOU ENTERED AN INVALID VALUE')



# pword = input('enter password')
#should be encrypted ;D to the db and displayed as ******
#try(Not Neccesary)... should have capital ,and a number AND longer than 8 characters



#this program gets users information and srores it in database
#should check if the user already exists and/or creates new account
#verification/authentication
