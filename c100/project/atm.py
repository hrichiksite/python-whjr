class ATM_MACHINE(object):
    def __init__(self, pin, card, balance, company, bank):
        self.pin = pin
        self.card = card
        self.company = company
        self.bank = bank
        self.balance = balance

    def withdrawl (self, amount, pin):
        if(self.pin == pin):
            print("Withdrawl successful")
            print(f"You have withdrawn {amount}")
        else:
            print("Wrong PIN")
        
    
    def BalanceEnquiry  (self, pin):
        if(self.pin == pin):
            print("Withdrawl successful")
            print(f"Your balance is {self.balance}")
        else:
            print("Wrong PIN")


ATM = ATM_MACHINE('1922', '1232157837485678', '23453', 'Visa', 'SBIBANKIN')

#correct withdrawl with correct pin
ATM.withdrawl( 1000, '1922')
#incorrect withdrawl with incorrect pin
ATM.withdrawl( 1000, '1921')
#correct balance enquiry with correct pin
ATM.BalanceEnquiry('1922')
#incorrect balance enquiry with incorrect pin
ATM.BalanceEnquiry('1921')