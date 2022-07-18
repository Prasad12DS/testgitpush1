class bank:
    def transaction(self):
        print("total transaction value")

    def account_opening(self):
        print("this will show you your account open status")

    def deposite(self):
        print("this will show you your deposit amount")

    def test(self):
        print("this is from 1 class")

class HDFC_bank:
    def hdfc_TO_icici(self):
        print("this will show you all transactions happen to icici through HDFC")

    def test(self):
        print("this is from 2 class")

class icici(HDFC_bank,bank):
    pass

c1 = icici()

c1.hdfc_TO_icici()
c1.deposite()
c1.transaction()
c1.account_opening()
c1.test()


class ineuron:
    def student(self):
        print("the details of all the students")

    def achievers(self):
        print("print all achievers details ")

    def hall_of_fame(self):
        print("print every one from hall of fame")

class ineuron_vision(ineuron):

    def student(self):
        print("these are the filter students list")

iv = ineuron_vision()
iv.student()