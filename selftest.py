class selftest(object):
    name = "123"
    def __init__(self):
        print ("")
    def a(self,name):
        print (self.name)
        self.name = name
        print(self.name) 
    
    
if __name__ == '__main__':
    
    fun = selftest()
    fun.a("456")