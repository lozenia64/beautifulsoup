f1 = open('perfume.txt', 'r')
lines1 = f1.readlines()
cnt1 = 1
cnt2 = 1
for line1 in lines1:
    if cnt2 == 1:
        f2 = open('url/input'+str(cnt1)+'.txt', 'w')
    else:
        f2 = open('url/input'+str(cnt1)+'.txt', 'a')
    f2.write(line1)
    cnt2+=1
    if cnt2 == 20:
        cnt1+=1
        cnt2=1
f2.close()
