class Bank():
	def __init__(self):
		self.Name=[]
		self.Amount=[]
		self.z=123000
		self.Account=[]
		self.num=1	
	def CreateAccount(self,name,amount) :
		self.Name.append(name)
		self.Amount.append(amount)	
		self.Account.append(self.z)
		accountNumber = self.z
		self.z=self.z+1	
		print("Your Account number is :", accountNumber)

	def BalanceEnquiry(self,account) :
		k=self.Account.index(account)
		print("Your balance is :",self.Amount[k])

	def DepositAmount(self,account,amount) :
		k=self.Account.index(account)
		self.Amount[k]=self.Amount[k]+amount
		print("Your final balance is :", self.Amount[k])
		
	def WithdrawAmount(self,account,amount) :	
		k=self.Account.index(account)
		self.Amount[k]=self.Amount[k]-amount
		print ("Your final balance is :",self.Amount[k])
num=1
B=Bank()
while num<=5 :
	print("1.Create account\n2.Balance Enquiry\n3.Deposit Amount\n4.Withdraw Amount.\n5.exit")
	num=int(input())	
	if num==1 :
		print ("Enter your name :")
		name=input()
		print ("Enter the amount :")
		amount=int(input())
		B.CreateAccount(name,amount)
			
	if num==2 :
		print ("Enter your account number :"),
		account=int(input())
		B.BalanceEnquiry(account)

	if num==3 :
		print ("Enter your Account number :")
		account=int(input())
		print ("Enter the amount to be deposited :")
		amount=int(input())
		B.DepositAmount(account,amount)

	if num==4 :
		print ("Enter your Account number :")
		account=int(input())
		print ("Enter the amount to be withdrawn :")
		amount=int(input())
		B.WithdrawAmount(account,amount)

	
	
