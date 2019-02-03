import re
string="'THIS IS.', what is this"
print(string)
new  = re.sub('[A-Z.'',]', '', string)
print(new)
