import csv
import user
import member
class Login:
	def __init__(self):
		print("Welcome To Gym App...!!!".center(50))
		self.admin_details = {'admin':'admin'}
		self.user_member = []
		self.regimen = []
		cv = csv.reader(open("regimen_list.csv", "r", newline=""))
		for row in cv:
			self.regimen.append(row)
		dv = csv.reader(open("user_member_list.csv", "r", newline=""))
		for row in dv:
			self.user_member.append(row)

	def logger(self):
		while True:
			try:
				n = int(input("Press 1 SuperUSer \nPress 2 Member \nPress C to cancel"))
				if n == 1:
					self.SuperUser_login()
					return False
				elif n == 2:
					self.member_login()
					return False
				elif n.lower() == "c":
					return False
				else:
					print("Enter a Withing a Given Option, Try Again...!!!!")
			except:
				print("enter a Valid Input")

	def SuperUser_login(self):
		while True:
			try:
				print("Welcome SuperUser Admin....!!!".center(50))
				v = int(input("Press 1 To SuperUser Admin Login... \nPress 0 To Exit..."))
				if v == 1:
					admin_id = input("Enter a Admin ID:")
					passw = input("Enter a Password:")
					check = False
					for key, value in self.admin_details.items():
						if key == admin_id and value == passw:
							check = True
							break
					else:
						print("Either Admin Id Or Password Wrong...!!!!")

					if check == True:
						print(admin_id,"Login Successfully...!!!!")
						user_obj = user.superuser()
						user_obj.menu()
						return False
				elif v == 0:
					print("Thank You")
					return False
			except:
				print("Invalid Input....!!!")


	def member_login(self):
		while True:
			try:
				print("Welcome Member...!!!".center(50))
				d = int(input("Press 1 To Member Login... \nPress 0 To Exit..."))
				if d == 1:
					ph_no = int(input("Enter a Mobile Number:"))
					bmi = 0.00
					name = ""
					check = False
					for i in self.user_member:
						if int(i[3]) == ph_no:
							bmi = float(i[5])
							name = i[0]
							check = True
							break
					else:
						print("Either Mobile Number Wrong....!!!")
					if check == True:
						print(ph_no,"Login Successfully....!!!!")
						m_obj = member.memberprofile(ph_no, bmi, name)
						m_obj.member_menu()
						return False

				elif d == 0:
					print("Thank You")
					return False
			except:
				print("login Invalid Input....!!!!")

if __name__ == '__main__':
	login_obj = Login()
	login_obj.logger()


