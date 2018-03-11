# -*- coding:utf-8 -*-

class dothing(object):
    def strclear(self,s=''):
        if '(' in s:  #去除一些不必要的字串
            s = s[0:s.index('(')]
        if '-' in s:  #去除一些不必要的字串
            s = s[0:s.index('-')]
        return s