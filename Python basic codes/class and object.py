class UserInfo:
    def putData(self):
        self.name=input("Enter your name ")
        self.id=int(input("enyer your id "))
        self.salary=float(input("Enter your salary "))
    def display(self):
        print("User name:",self.name)
        print("user id:",self.id)
        print("user salary:",self.salary)

obj=UserInfo()
obj.putData()
obj.display()
