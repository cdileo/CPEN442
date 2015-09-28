from PyCRC import CRC32
import string
import itertools
from datetime import datetime

PossChars = list(string.ascii_uppercase + string.digits)
c = CRC32
t = c.CRC32()

myHash = 'DC61E5A9956BDBDA4F5A669ECC31FA90'
hashToFind = t.calculate('DC61E5A9956BDBDA4F5A669ECC31FA90')

startTime = datetime.now()
print('Starting Search at {} for {}'.format(str(startTime), hashToFind))

i = 0

for j in range(8,9):
	CombIterator = itertools.combinations_with_replacement(PossChars, j)
	for valueToHash in CombIterator:
		v = ''.join(valueToHash)
		h = t.calculate(v)
		i += 1
		if i > 1000000:
			print('At try {}'.format(v))
			i = 0
		if h == hashToFind:
			print('\a')
			print('Last Value is: ' + v)
			print('Hash value is: ' + str(h))
			print('end summary')
			break

endTime = datetime.now()
print('Search ended at {}'.format(str(endTime)))
print('\a')
# found hash value is 2051433057
# value 1 is 		  acccddf4
# value 2 is 		  aack8899
# 1 minute 16 seconds