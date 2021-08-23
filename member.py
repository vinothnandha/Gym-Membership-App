import csv
class memberprofile:

    def __init__(self, ph_no, bmi, name):
        self.mobile_no = ph_no
        self.name = name
        self.a_bmi = bmi
        self.user_member = []
        self.regimen = []
        cv = csv.reader(open("regimen_list.csv", "r", newline=""))
        for row in cv:
            self.regimen.append(row)
        dv = csv.reader(open("user_member_list.csv", "r", newline=""))
        for row in dv:
            self.user_member.append(row)

    def my_profile(self):
        n = self.mobile_no
        for i in self.user_member:
            if int(i[3]) == n:
                print("Full Name:{0} \nAge:{1} \nGender:{2} \nMobile Number:{3} \nEmail:{4} \nBMI:{5} \nMembership Duration:{6}".format(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
                break

    def my_regimen(self):
        for i in self.regimen:
            if self.a_bmi == float(i[0]):
                print("{} Your Workout Regimen".format(self.name))
                print("BMI:{} \nMonday:{} \nTuesday:{} \nWednesday:{} \nThursday:{} "
                      "\nFriday:{} \nSaturday:{} \nSunday:{}".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
                break
            elif self.a_bmi < 18.5 and float(i[0]) == 18.5:
                print("{} Your Workout Regimen".format(self.name))
                print("BMI:{} \nMonday:{} \nTuesday:{} \nWednesday:{} \nThursday:{} "
                      "\nFriday:{} \nSaturday:{} \nSunday:{}".format(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
                break
            elif self.a_bmi < 25 and float(i[0]) == 25:
                print("{} Your Workout Regimen".format(self.name))
                print("BMI:{} \nMonday:{} \nTuesday:{} \nWednesday:{} \nThursday:{} "
                      "\nFriday:{} \nSaturday:{} \nSunday:{}".format(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
                break
            elif self.a_bmi <= 29 and float(i[0]) == 29:
                print("{} Your Workout Regimen".format(self.name))
                print("BMI:{} \nMonday:{} \nTuesday:{} \nWednesday:{} \nThursday:{} "
                      "\nFriday:{} \nSaturday:{} \nSunday:{}".format(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
                break
            elif self.a_bmi >= 30 and float(i[0]) == 30:
                print("{} Your Workout Regimen".format(self.name))
                print("BMI:{} \nMonday:{} \nTuesday:{} \nWednesday:{} \nThursday:{} "
                      "\nFriday:{} \nSaturday:{} \nSunday:{}".format(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
                break
        else:
            print("Workout Regimen Not Avalible \n{}-Sorry Sir/Mam Please Ask a SuperUser to Create a Workout Regimen for your BMI".format(self.name))

    def member_menu(self):
        flag = True
        while flag:
            try:
                self.choice = int(input("\nPress 1 To View My Workout Regimen \nPress 2 To View a My Profile \nPress 0 To Exit"))
                if self.choice == 1:
                    self.my_regimen()
                elif self.choice == 2:
                    self.my_profile()
                elif self.choice == 0:
                    print("Thank You....!!!!")
                    flag = False
                else:
                    print("Not Valid Choice, Try Again....!!!!")
            except:
                print("Invalid Input------!!!")

