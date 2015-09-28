from PyCRC import CRC32
import string
import itertools
from datetime import datetime

PossChars = list(string.ascii_lowercase+ string.digits)
CombIterator = itertools.combinations_with_replacement(PossChars, 8)
c = CRC32
t = c.CRC32()

valToHashDict = {}
hashToValDict = {}

v = ''
h = ''

startTime = datetime.now()
print('Starting Search at {}'.format(str(startTime)))

for valueToHash in CombIterator:
	v = ''.join(valueToHash)
	h = t.calculate(v)
	if h in hashToValDict:
		print('\a')
		print('Last Value is: ' + v)
		print('Old value is: ' + str(''.join(hashToValDict[h])))
		print('Hash value is: ' + str(h))
		print('end summary')
		
		break
	else:
		valToHashDict[valueToHash] = h
		hashToValDict[h] = valueToHash

endTime = datetime.now()
print('Search ended at {}'.format(str(endTime)))
print('\a')
# found hash value is 2051433057
# value 1 is 		  acccddf4
# value 2 is 		  aack8899
# 1 minute 16 seconds