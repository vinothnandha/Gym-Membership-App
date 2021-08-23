import csv
class superuser:

    def __init__(self):
        self.user_member = []
        self.regimen = []
        cv = csv.reader(open("regimen_list.csv", "r", newline=""))
        for row in cv:
            self.regimen.append(row)
        dv = csv.reader(open("user_member_list.csv", "r", newline=""))
        for row in dv:
            self.user_member.append(row)

    def create_member(self):
        print('Member Creation page...!!!'.center(10, '~'))
        while True:
            try:
                full_name = input("Enter a Full Name:")
                age = int(input("Enter a Age:"))
                gender = input("Enter a Gender M or F or T:")
                ph_no = self.ph_no()
                email_id = self.check_email()
                bmi = float(input('Enter a BMI:'))
                duration = self.duration()
                self.user_member.append([full_name.title(), age, gender.upper(), ph_no, email_id, bmi, duration])
                ab = csv.writer(open("user_member_list.csv", 'w', newline=""))
                ab.writerows(self.user_member)
                print("Member Created Successfully...!!!")
                # print(self.user)
                return False
            except:
                print("Invalid Input")

    def ph_no(self):
        flag = True
        while flag:
            try:
                ph_no = input("Enter a Phone Number:")
                if ph_no.isdigit() and len(ph_no) == 10:
                    if self.user_member:
                        for i in self.user_member:
                            if i:
                                if i[3] == ph_no:
                                    print("Entered Phone Number Already Present")
                                    break
                        else:
                            return ph_no
                            flag = False
                    else:
                        return ph_no
                        flag = False
                else:
                    print("Enter in a digit format... \nOnly 10 Number are allowed...")
            except:
                print("Invalid Input.....")

    def check_email(self):
        while True:
            email_id = input("Enter a Email_ID:")
            try:
                if self.user_member:
                    for i in self.user_member:
                        if i:
                            if i[4] == email_id:
                                print("Email ID is Already Available...!!!")
                                break
                    else:
                        return email_id
                        break
                else:
                    return email_id
                    break
            except:
                print("Invalid Input...!!!!")

    def duration(self):
        while True:
            print("Available Duration \nPress 1 for 1-Month Duration \nPress 2 for 3-Month Duration \nPress 3 for 6-Month Duration \nPress 4 for 12-Month Duration \nPress C for Cancel Membership Duration")
            duration = int(input("Enter a Given Available duration:"))
            try:
                if duration == 1:
                    return "1-Month"
                    break
                elif duration == 2:
                    return "3-Month"
                    break
                elif duration == 3:
                    return "6-Month"
                    break
                elif duration == 4:
                    return "12-Month"
                    break
                elif duration.upper() == 'C':
                    return "Cancel Member"
                else:
                    print("Please enter in available duration limit.....!!!")
            except:
                print("Invalid Input...!!!!")


    def view_member(self):
        with open("user_member_list.csv",'r', newline="") as fb:
            read = csv.reader(fb)
            print("List Of Member....!!!")
            first = 1
            for row in read:
                if first:
                    first = 0
                    print("First Name".center(25),"Age".center(10),"Gender".center(10),"Mobile Number".center(20),"Email".center(20),"BMI".center(20),"Membership Duration".center(20), end="\n")
                print(row[0].center(25),row[1].center(10),row[2].center(10),row[3].center(20),row[4].center(20),row[5].center(20),row[6].center(20), end="\n")

    def remove_member(self):
        while True:
            try:
                n = int(input("Enter a Mobile Number of a Member You Want To Remove:"))
                a = 0
                for i in self.user_member:
                    if int(i[3]) == n:
                        a = 1
                        self.user_member.remove(i)
                        print("Successfully Removed....!!!!")
                        break
                if a==0:
                    print("Mobile Number Not Available...!!!")
                else:
                    ab = csv.writer(open("user_member_list.csv",'w', newline=""))
                    ab.writerows(self.user_member)
                    return False
            except:
                print("Invalid Input")

    def update_member(self):
        while True:
            try:
                n = int(input("Enter a Mobile Number of a Member You Want To Edit:"))
                a = 0
                for i in self.user_member:
                    if int(i[3]) == n:
                        a = 1
                        print("Full Name:{0} \nAge:{1} \nGender:{2} \nMobile Number:{3} \nEmail:{4} \nBMI:{5} \nMembership :{6}".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
                        show = int(input("Press 1 To Edit Full Name \nPress 2 To Edit Age \nPress 3 To Edit Gender \nPress 4 To Edit BMI \nPress 5 To Edit Membership Duration \nPress 0 To Exit"))
                        if show == 1:
                            full_name = input("Enter a Full Name:")
                            i[0] = full_name
                            print("Successfully Edited....!!!!")
                            break
                        elif show == 2:
                            age = int(input("Enter a Age:"))
                            i[1] = age
                            print("Successfully Edited....!!!!")
                            break
                        elif show == 3:
                            gender = input("Enter a Gender M or F or T:")
                            i[2] = gender
                            print("Successfully Edited....!!!!")
                            break
                        elif show == 4:
                            bmi = float(input('Enter a BMI:'))
                            i[5] = bmi
                            print("Successfully Edited....!!!!")
                            break
                        elif show == 5:
                            duration = self.duration()
                            i[6] = duration
                            print("Successfully Edited....!!!!")
                            break
                        elif show == 0:
                            print("Quited....!!!!")
                            return False
                        else:
                            print("Enter a Number within a given option...!!!")
                if a == 0:
                    print(n,"-Mobile NUmber is Not Available")
                else:
                    ab = csv.writer(open("user_member_list.csv",'w', newline=""))
                    ab.writerows(self.user_member)
                    return False
            except:
                print("Invalid Input..!!!")

    def create_regimen(self):
        print('Workout Regimen Creation page...!!!!!'.center(10, '~'))
        while True:
            try:
                bmi = float(input("Enter Workout Regimen BMI:"))
                mon = input("Enter a Monday Workout Regimen:")
                tue = input("Enter a Tuesday Workout Regimen:")
                wed = input("Enter a Wednesday Workout Regimen:")
                thu = input("Enter a Thursday Workout Regimen:")
                fri = input("Enter a Friday Workout Regimen:")
                sat = input("Enter a Saturday Workout Regimen:")
                sun = input("Enter a Sunday Workout Regimen:")
                self.regimen.append([bmi, mon.title(), tue.title(), wed.title(), thu.title(), fri.title(), sat.title(), sun.title()])
                cb = csv.writer(open("regimen_list.csv", 'w', newline=""))
                cb.writerows(self.regimen)
                print("Workout Regimen Created Successfully...!!!")
                return False
            except:
                print("Invalid Input")


    def view_regimen(self):
        with open("regimen_list.csv",'r', newline="") as fb:
            read = csv.reader(fb)
            print("List Of Workout Regimen....!!!")
            first = 1
            for row in read:
                if first:
                    first = 0
                    print("BMI".center(10),"Monday".center(10),"Tuesday".center(10),"Wednesday".center(10),"Thursday".center(10),"Friday".center(10),"Saturday".center(10),"Sunday".center(10), end="\n")
                print(row[0].center(10),row[1].center(10),row[2].center(10),row[3].center(10),row[4].center(10),row[5].center(10),row[6].center(10),row[7].center(10), end="\n")

    def remove_regimen(self):
        while True:
            try:
                n = float(input("Enter a BMI of a Workout Regimen You Want To Remove:"))
                a = 0
                for i in self.regimen:
                    if float(i[0]) == n:
                        a = 1
                        self.regimen.remove(i)
                        print("Successfully Removed....!!!!")
                        break
                if a == 0:
                    print("BMI Not Available...!!!")
                else:
                    ab = csv.writer(open("regimen_list.csv",'w', newline=""))
                    ab.writerows(self.regimen)
                    return False
            except:
                print("Invalid Input")

    def update_regimen(self):
        while True:
            try:
                n = float(input("Enter a BMI of a Workout Regimen You Want To Edit:"))
                a = 0
                for i in self.regimen:
                    if float(i[0]) == n:
                        a = 1
                        print("BMI:{0} \nMonday:{1} \nTuesday:{2} \nWednesday:{3} \nThursday:{4} \nFriday:{5} \nSaturday:{5} \nSunday:{6}".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
                        show = int(input("Press 1 To Edit Monday Workout Regimen \nPress 2 To Edit Tuesday Workout Regimen \nPress 3 To Edit Wednesday Workout Regimen \nPress 4 To Edit Thursday Workout Regimen"
                                         " \nPress 5 To Edit Friday Workout Regimen \nPress 6 To Edit Saturday Workout Regimen \nPress 7 To Edit Sunday Workout Regimen \nPress 0 To Exit"))
                        if show == 1:
                            mon = input("Enter a Monday Workout Regimen:")
                            i[0] = mon.title()
                            print("Successfully Edited....!!!!")
                            break
                        elif show == 2:
                            tue = int(input("Enter a Tuesday Workout Regimen:"))
                            i[1] = tue.title()
                            print("Successfully Edited....!!!!")
                            break
                        elif show == 3:
                            wed = input("Enter a Wednesday Workout Regimen:")
                            i[2] = wed.title()
                            print("Successfully Edited....!!!!")
                            break
                        elif show == 4:
                            thu = input('Enter a Thursday Workout Regimen:')
                            i[5] = thu.title()
                            print("Successfully Edited....!!!!")
                            break
                        elif show == 5:
                            fri = input('Enter a Friday Workout Regimen:')
                            i[6] = fri.title()
                            print("Successfully Edited....!!!!")
                            break
                        elif show == 6:
                            sat = input('Enter a Saturday Workout Regimen:')
                            i[6] = sat.title()
                            print("Successfully Edited....!!!!")
                            break
                        elif show == 7:
                            sun = input('Enter a Sunday Workout Regimen:')
                            i[6] = sun.title()
                            print("Successfully Edited....!!!!")
                            break
                        elif show == 0:
                            print("Quited....!!!!")
                            return False
                        else:
                            print("Enter a Number within a given option...!!!")
                if a == 0:
                    print(n,"-Mobile NUmber is Not Available")
                else:
                    ab = csv.writer(open("user_list.csv",'w', newline=""))
                    ab.writerows(self.user_member)
                    return False
            except:
                print("Invalid Input..!!!")

    def menu(self):
        flag = True
        while flag:
            try:
                self.choice = int(input("\nPress 1 To Create a Member \nPress 2 To View a Member \nPress 3 To Remove a Member \nPress 4 To Update a Member \nPress 5 To Create Workout Regimen \nPress 6 To View Workout Regimen \nPress 7 To Remove Workout Regimen \nPress 8 To Update Workout Regimen \nPress 0 To Exit"))
                if self.choice == 1:
                    self.create_member()
                elif self.choice == 2:
                    self.view_member()
                elif self.choice == 3:
                    self.remove_member()
                elif self.choice == 4:
                    self.update_member()
                elif self.choice == 5:
                    self.create_regimen()
                elif self.choice == 6:
                    self.view_regimen()
                elif self.choice == 7:
                    self.remove_regimen()
                elif self.choice == 8:
                    self.update_regimen()
                elif self.choice == 0:
                    print("Thank You....!!!!")
                    flag = False
                else:
                    print("Not Valid Choice, Try Again....!!!!")
            except:
                print("Invalid Input------!!!")

#obj = superuser()
