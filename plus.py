f1 = open('select.txt', 'w')

f2 = open('select0.txt', 'r')
lines2 = f2.readlines()
for line2 in lines2:
    f1.write(line2)

f3 = open('select1.txt', 'r')
lines3 = f3.readlines()
for line3 in lines3:
    f1.write(line3)

f4 = open('select2.txt', 'r')
lines4 = f4.readlines()
for line4 in lines4:
    f1.write(line4)

f5 = open('select3.txt', 'r')
lines5 = f5.readlines()
for line5 in lines5:
    f1.write(line5)

f6 = open('select4.txt', 'r')
lines6 = f6.readlines()
for line6 in lines6:
    f1.write(line6)

f6.close()
f5.close()
f4.close()
f3.close()
f2.close()
f1.close()
