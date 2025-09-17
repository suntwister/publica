class Student:
    def __init__(self, name, course, level, state_of_origin):
        #print("creating a new student")
        self.name = name
        self.course = course
        self.level = level
        self.state_of_origin = state_of_origin
        self.cgpa = 0.0
        self.fees_paid = False
        print(f"student {name} has been created successfully")

    def pay_school_fees(self):
        self.fees_paid = True
        return f"{self.name} has paid school fees for {self.level} level"
    
    def register_courses(self):
        if self.fees_paid:
            return f"{self.name} has registered for {self.course}"
        else:
            return f"{self.name} has not paid school fees!"
        
    def calculate_cgpa(self, grades):
        if grades:
            self.cgpa = sum(grades)/ len(grades)
            return f"Your current CGPA is {self.cgpa:.2f}"
        return f"No grades provided"
    
    def get_university(cls):
        return cls.university


kemi = Student("Kemi Oyewusi", "Political Science", "400", "Oyo State")

# class NigerianStudent:
#     def __init__(self, name, state, course):
#         #print(f"step 1, creating stundent object")
#         self.name = name
#         self.state_of_origin = state
#         self.course = course
#         self.student_id = self.generate_id()
#         # print(f"Step 6: {self.name} from {self.state_of_origin} is already")

#     def generate_id(self):
#         import random
#         #return f"LAU15{random.randint(1000,9999)}"

samuel = Student("Oyewusi samuel",  "Pure and Applied Mathematics", "500", "Oyo state")
#print(f"{samuel.name} is a registered student with id {samuel.generate_id()}")


class PhoneUser:
    def __init__(self, name, network):
        self.name = name
        self.network = network
        self.airtime = 0
        print(f"{self.name} joined {self.network} network")

    def buy_airtime(self, amount):
        self.airtime += amount
        return f"{self.name} you have succesfully recharged {amount} your new balance is #{self.airtime}"
    
# abeeb = PhoneUser("Olabiyi Abeeb", "MTN")
# onisemo = PhoneUser("Bello Lanre", "Glo")

# print(abeeb.buy_airtime(500))     # Tunde now has ₦500 airtime
# print(onisemo.buy_airtime(1000)) # Blessing now has ₦1000 airtime
# print(abeeb.airtime)              # 500 (Tunde's airtime unchanged)
# print(onisemo.airtime)           # 1000 (Blessing's airtime unchanged)

# fathia = Student("Fathia Abdul", "Biochemistry", 300, "Ogun state")
# paul = Student("Adewuyi Paul", "Fine Art", 200, "Oyo state")
# emmanuel = Student("Olamide Emmanuel", "Physics", 400, "Lagos state")
# student1 = Student("Anthony Johnson", "Engineering", 200, "Ogun")
# student2 = Student("Fadilat Hassan", "Medicine", 400, "Lagos")

# all_students = [
# Student("Fathia Abdul", "Biochemistry", 300, "Ogun state"),
# Student("Adewuyi Paul", "Fine Art", 200, "Oyo state"),
# Student("Olamide Emmanuel", "Physics", 400, "Lagos state")
# ]

# print(f"ID\t | {"Name":<20}\t | {"Course":<20}\t | CGPA")
# print("-" * 30)
# for i, student in enumerate(all_students):
# print(f"{i+1}\t| {student.name:<20}\t| {student.course:<20}\t| {student.cgpa}")

# print(paul.pay_school_fees())


class BankAccount:
    def __init__(self, owner, bank_name, balance=0):
        self.owner = owner
        self.bank_name = bank_name
        self._balance = balance
        self.__pin = "1234"
        self._transaction_history = []
        self.account_number = self.generate_account_number()

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._transaction_history.append(f"Deposited \u20A6{amount:,}")
            return f"\u20A6{amount:,} has been deposited successfully to {self.bank_name}'s account. your current balance is \u20A6{self.balance}"
        return f"Invalid deposit amount"
    
    def withdraw(self, amount):
        if self.__verify_pin(pin):
            if amount > 0 and amount <= self.balance:
                self._balance -= amount
                self._transaction_history.append(f"Withdrew \u20A6{amount:,}")
                return f"\u20A6{amount:,} withdrawn from {self.owner}'s account. New balance \u20A6{self.balance}"
            return f"Insufficient funds or invalid amount"
        return "Invalid PIN"

    def transfer(self, amount, recipient):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self._transaction_history.append(f"Transfered \u20A6{amount}")
            return f"\u20A6{amount:,} transferred from {self.owner} to {recipient}. Remaining balance is \u20A6{self.balance:,}"
        return "Transfer failed due to insufficient fund" 
    
    def balance_check(self):
        if self.__pin
        return f"{self.owner}'s {self.bank_name} account balance: \u20A6{self.balance:,}"
    
    def generate_account_number(self):
        import random
        return f"01{random.randint(10000000, 99999999)}"
    
    def __verify_pin(self, enterd_pin):
        return self.entered_pin == self.__pin
    
adunni_account = BankAccount("Adunni Olaleye", "AXT Bank", 5000 )



print(adunni_account.deposit(25000))    
print(adunni_account.withdraw(10000))  
print(adunni_account.transfer(15000, "Sunday James"))  
print(adunni_account.balance_check())  

print(f"Name:\t {adunni_account.owner:>20}")
print(f"Bank:\t {adunni_account.bank_name:>15}")
print(f"Account Number: {adunni_account.account_number:>10}")