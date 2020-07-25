i = 0
while True:
    #print(i)
    s = list(map(int,str(i)))
    l = len(s)
    if l%2!=0:
        i = i + 1
        continue
    h = 0
    j = 1
    for g in range(int(l/2)):
        x = s[h]
        y = s[j]
        count = 0
        for c in s:
            if c == y:
                count = count + 1
        if x != count:
            break
        if j == (l-1):
            print(i)
        h = h + 2
        j = j + 2
    i = i + 1
    if i == 9999999999:
        break
print('done')
