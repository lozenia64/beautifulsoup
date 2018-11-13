f1 = open('select.txt', 'r')
lines1 = f1.readlines()
cnt1 = 1
cnt2 = 1
for line1 in lines1:
    if cnt2 == 1:
        f2 = open('url/url'+str(cnt1)+'.txt', 'w')
    else:
        f2 = open('url/url'+str(cnt1)+'.txt', 'a')
    f2.write(line1)
    cnt2+=1
    if cnt2 == 1000:
        cnt1+=1
        cnt2=1
    f2.close()
f1.close()
