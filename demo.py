from mypackage.Base import dothing
from mypackage.kkboxModle import kkboxModle
from datetime import *

class demo(object):
    def __init__(self):
        self.yesterday = datetime.now() - timedelta(days=1)# 昨天
        self.date = self.yesterday.strftime('20%y-%m-%d')

    

if __name__ == '__main__':
    kk = kkboxModle()
    #kk.weekly()
    bb = dothing()
    i=0
    
    bb.deltest()