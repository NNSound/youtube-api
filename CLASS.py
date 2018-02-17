import requests
from bs4 import BeautifulSoup
class ptt_cralwer(object):




	def __init__(self):
    	print('')
	def get_gossiping(self):
    	payload = {
        	'from':'/bbs/Gossiping/index.html',
        	'yes':'yes'
    	}
    	rs = requests.session()
    	res = rs.post('https://www.ptt.cc/ask/over18', verify=False, data=payload)
    	res = rs.get('https://www.ptt.cc/bbs/Gossiping/index.html', verify=False)
    	dom = BeautifulSoup(res.text)
    	for ele in dom.select('.r-ent'):
        	print(ele.select('.date')[0].text +":" + ele.select('.author')[0].text + "\n" + ele.select('.title a')[0].text)
#     	print(res.text)
        
if __name__ == '__main__':
	cralwer = ptt_cralwer()
	cralwer.get_gossiping()


