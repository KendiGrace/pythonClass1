class bankDetails:
      def __init__(self,name,number,password):
             self.name=name
             self.number=number
             self.password=password

      def deposit(self):
          depo=30000
         
          return "My name is {} and my account number is {}.i want to deposit {}.".format(self.name,self.number,depo)
      def save(self):
           balance=150000
           return "After depositing money yesterday,my new balance is {}.I changed my password to {}.".format(balance,self.password)

