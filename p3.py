table = {}
table['red'] = {'orange': 'yellow', 'purple':'blue', 'red':'blank'}
table['yellow'] = {'orange':'red', 'green':'blue', 'yellow':'blank'}
table['blue'] = {'purple':'red', 'green':'yellow', 'blue':'blank'}
table['blank'] = {'red':'red', 'yellow':'yellow', 'blue':'blue'}

lst = []

# s = input('input: ')
# s = 'blue blue yellow orange orange green green green blue blue purple red red orange orange purple green yellow red red yellow orange orange green purple purple purple purple green orange red yellow yellow blue blue yellow yellow yellow orange purple green yellow blue purple purple blue red purple green orange red yellow yellow blue purple purple blue yellow green green yellow red purple green green blue red orange yellow blue blue red purple blue yellow yellow red red yellow green purple purple green orange orange orange orange yellow yellow green green yellow red purple blue blank'
# s = 'blue blue yellow orange orange green green green blue blue purple red red orange orange purple green yellow red red yellow orange orange green purple purple purple purple green orange red yellow yellow blue blue yellow yellow yellow orange purple green yellow blue purple purple blue red purple green orange red yellow yellow blue purple purple blue yellow green green yellow red purple green green blue red orange yellow blue blue red purple blue yellow yellow red red yellow green purple purple green orange orange orange orange yellow yellow green green yellow blank'
# s = 'blue blue yellow orange orange green green green blue blue purple red red orange orange purple green yellow red red yellow orange orange green purple purple purple purple green orange red yellow yellow blue blue yellow yellow yellow orange purple green yellow blue purple purple blue red purple green orange red yellow yellow blue purple purple blue yellow green green yellow red purple green green blue red orange yellow blue blue red purple blue yellow yellow red red yellow yellow'
# s = raw_input('input: ')

with open('Xortholian-Paintings_InputForSubmission_1.txt') as f:
    lines = f.readlines()
s = lines[0]

slist = s.split()

lst.append(slist[0])

for i in range(1, len(slist) - 2):
	lst.append(table[lst[-1]][slist[i]])

lst.append(slist[-1])

# print lst
# i = 0
# while i < len(lst):
# 	if lst[i] == 'blank':
# 		del lst[i]
# 	else:
# 		i += 1

res = ''
for word in lst:
	res = res + ' ' + word
res = res[1:]

print res
