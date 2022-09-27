S = '+7 (812) 134-12-324'
import re
S1 = re.sub('[-| |)|(]','', S)
print (S1)