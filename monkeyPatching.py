# In python ,the term monkey patching refers to dynamic(on-run-time) modifications of a class or module.
class Test:
    def __init__(self,a):
        self.a=a
    def getData(self):
        print("Message from Database.",self.a)
    def fun(self):
        self.getData()
t=Test(1)
t.fun()
def newGetData(self):
    print("Message from testData.",self.a)
Test.getData=newGetData # here, newGetData is not been called as function ,rather it is used as referencing
print("After Monkey patching....")
t.fun()