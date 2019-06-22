#This script generates vanity addresses for the XEL blockchain
#You need a local XEL server running
#You need the 'requests' Python library

#!/usr/bin/env python3

import requests
import random
import time

BASE58 = '23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
poss = ['1337', '1337-H4X0R']

address = ''
j = 0
print('Searching for strings ', poss)

url_pw = 'http://localhost:17876/nxt?=%2Fnxt&requestType=getAccountId&secretPhrase={}'
url_bal = 'http://localhost:17876/nxt?=%2Fnxt&requestType=getBalance&account={}'

stime = time.time()
found = False
while not found
	passphrase =  ('%s%s' % ('S', ''.join([BASE58[ random.SystemRandom().randrange(0,len(BASE58)) ] for i in range(34)])))
	address = requests.get(url_pw.format(passphrase)).json()['accountRS']
	bal = float(requests.get(url_bal.format(address)).json()['unconfirmedBalanceNQT'])

	j += 1
	print(address, j, passphrase, bal)
	
	if any(str in address for str in poss):
		found = True

	if bal > 0.0:
		input('Continue?')
		continue

print('Found passphrase => ', passphrase)
print('Time taken: ', time.time()-stime)
