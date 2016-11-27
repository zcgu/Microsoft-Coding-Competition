def findmx(prices, cur):
    last = -1
    hold = False

    s = ''

    for i in range(0, len(prices)):
        
        if not hold:
            # print cur, prices[i]
            if cur >= prices[i]:
                # print 1
                # cur -= prices[i]
                last = prices[i]
                s += 'B'
                hold = True
            else:
                # print cur, prices[i]
                # print 2
                s += ' '
        else:		
            if prices[i] >= last:
                # print 3
                cur += prices[i] - last
                last = prices[i]
                s += '.'
            else:
                # print 4

                if s[-1] == '.':
                    s = s[:-1] + 'S'
                elif s[-1] == 'B':
                    s = s[:-1] + ' '

                s += 'B'
                last = prices[i]
        # print i, cur

    for i in range(len(s) - 1, -1, -1):
        if s[i] == 'S':
            break
        elif s[i] == ' ':
            continue
        elif s[i] == '.':
            s = s[:i] + ' ' + s[i+1:]
        else:
            s = s[:i] + ' ' + s[i+1:]
            # cur += prices[i]
            break
    # print s
    return cur, s



# with open('PracticeInput.txt') as f:
#     lines = f.readlines()
# with open('PracticeInput (1).txt') as f:
#     lines = f.readlines()
with open('Time-Traveling-Day-Trader_InputForSubmission_1.txt') as f:
    lines = f.readlines()

s = lines[0]
origin = float(s)
# print origin

timeline = lines[1]
# print timeline
timelinelist = lines[1].split()
# print timelinelist

mx = 0
ms = ''
mname = ''

for i in range(2, len(lines)):
    prices = lines[i].split()
    name = prices[0]
    prices = prices[1:]

    for i in range(len(prices)):
        prices[i] = float(prices[i])

    curmx, s = findmx(prices, origin)

    if curmx > mx:
        mx = curmx
        ms = s
        mname = name


print mname
mxs = str(mx)
index = mxs.index('.')
# print len(mxs) - index
if len(mxs) - index == 3:
    pass
elif len(mxs) - index == 2:
    mxs += '0'
elif len(mxs) - index == 1:
    mxs += '00'
print mxs

times = ''

for time in timelinelist:
    if len(time) == 1:
        times += time + '    '
    else:
        times += time + '   '

print times

finals = ''
for i in range(len(ms) - 1):
    finals += ms[i] + '    '
    # print finals
    
if ms[i] == ' ':
    pass
else:
    finals += ms[-1]
print finals





