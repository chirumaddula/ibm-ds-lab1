i = 0
while True:
    #print(i)
    s = map(int,str(i))
    h = 0
    for c in s:
        h = h + (c**c)
    #print(h)
    if h == i:
        print('       ',i)
    i = i + 1
    if i == 9999:
        break
print('done')
