
import pymysql

conn = pymysql.connect(host = 'localhost',user = 'root',passwd='',db='users')

myCursor = conn.cursor()#allows you to execute queries in mysql

print('------- CHOOSE --------')
print('0 :SEARCH IF USERNAME EXISTS')
print('1 :CREATE NEW USERNAME AND PASSWORD')
print('2 :UPDATE EXISTING USERNAME AND PASSWORD')
print('3 :DELETE EXISTING USERNAME AND PASSWORD')

ans = int(input('PLEASE SELECT AN OPTION:  '))

if ans == 1:

	#create a new user (need to check bring the search function here)
	print('CREATE A NEW ACCOUNT')
	uname =input('ENTER USERNAME:  ')
	passord =input('ENTER PASSWORD: ')

	search = uname
	#search if value exists in the database
	#search = "njehfnga" #enter search value here(need to change to user input)


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
		conn.commit()
		conn.close()


elif ans ==2:
	print('UPDATE EXISTING USERNAME AND PASSWORD\n')
	print('1) CHANGE USERNAME')
	print('2) CHANGE PASSWORD')

	choice = input('ENTER YOUR CHOICE 1/2')
	if choice == 1:

		search = input('ENTER YOUR USERNAME')
	#search if value exists in the database
	#search = "njehfnga" #enter search value here(need to change to user input)


		sqlSEARCH = "SELECT UserID,user_Name , Password FROM `userName_Password` WHERE user_Name like  %s "  


		val = myCursor.execute(sqlSEARCH,search)

		if val == 1:
			print('value found')
			newname = input('ENTER NEW USERNAME: ')


			################################################################################we are here fin a way to search the username given return the id and update from there
			#because you can onlyupdate using the individuals id(primary key)
# 			UPDATE username_password
# SET User_Name = 'AlfredSchmidt'
# WHERE UserID = 1;



		else:
			print('USERNAME DOES NOT EXIST')


	elif choice == 2:

	else :
		print('INVALID OPTION')




elif ans == 3:
	print('NOT YET WRITTEN')

	sqlDELETE = "INSERT INTO username_password(UserID,user_Name,password) VALUES (%s , %s , %s)"
	myCursor.execute(sqlDELETE, (uid ,uname, passord))
	conn.commit()
	conn.close()


elif ans == 0:

	search = input('Enter name to search')
	#search if value exists in the database
	#search = "njehfnga" #enter search value here(need to change to user input)


	sqlSEARCH = "SELECT UserID,user_Name , Password FROM `userName_Password` WHERE user_Name like  %s "  


	val = myCursor.execute(sqlSEARCH,search)

	if val == 1:
		print('value found')

	else:
		print('value was not found')

elif ans > 3:
	print('YOU ENTERED AN INVALID VALUE')

elif ans < 1:
	print('YOU ENTERED AN INVALID VALUE')


















# fname = input('enter first name')

# lname = input('enter last name')

# email = input('enter email')
# #should use the regex to refuse bad /wrong emails


# age = input('enter age')

# uname = input('enter username')
# #should check the db first for existing unames

# pword = input('enter password')
#should be encrypted ;D to the db and displayed as ******
#try(Not Neccesary)... should have capital ,and a number AND longer than 8 characters



#this program gets users information and srores it in database
#should check if the user already exists and/or creates new account
#verification/authentication
