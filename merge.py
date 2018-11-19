f = open("out.txt", 'a')
f1 = open("out1.txt", 'r')
f2 = open("out2.txt", 'r')
f3 = open("out3.txt", 'r')

line = f1.readline()
#print(line)

c1 = line.find(',')
c2 = line.find(',', c1+1)
c3 = line.find(',', c2+1)
c4 = line.find(',', c3+1)
c5 = line.find(',', c4+1)
c6 = line.find(',', c5+1)
c7 = line.find(',', c6+1)
c8 = line.find(',', c7+1)
c9 = line.find(',', c8+1)
c10 = line.find(',', c9+1)
c11 = line.find(',', c10+1)
c12 = line.find(',', c11+1)
c13 = line.find(',', c12+1)
c14 = line.find(',', c13+1)
c15 = line.find(',', c14+1)
c16 = line.find(',', c15+1)
c17 = line.find(',', c16+1)
c18 = line.find(',', c17+1)
c19 = line.find(',', c18+1)
c20 = line.find(',', c19+1)
c21 = line.find(',', c20+1)

#print(line[:-1])
print("Name : "+line[:c1])
print("Group : "+line[c1+1:c2])
print("MainNote1 : "+line[c2+1:c3])
print("MainNote2 : "+line[c3+1:c4])
print("MainNote3 : "+line[c4+1:c5])

season = [line[c5+1:c6], line[c6+1:c7], line[c7+1:c8], line[c8+1:c9]]
s1 = int(season[0])+int(season[1])+int(season[2])+int(season[3])
if int(season[0])/s1*100 >= 60:
    print("Season : Spring")
elif int(season[1])/s1*100 >= 60:
    print("Season : Summer")
elif int(season[2])/s1*100 >= 60:
    print("Season : Fall")
elif int(season[3])/s1*100 >= 60:
    print("Season : Winter")
elif (int(season[0])+int(season[1]))/s1*100 >= 65:
    print("Season : Spring/Summer")
elif (int(season[2])+int(season[3]))/s1*100 >= 65:
    print("Season : Fall/Winter")
else:
    print("Season : All Season")

dn = [line[c9+1:c10], line[c10+1:c11]]
d1 = int(dn[0])+int(dn[1])
if int(dn[0])/d1*100 > 60:
    print("Time : Day")
elif int(dn[1])/d1*100 > 60:
    print("Time : Night")
else:
    print("Time : All Time")

long = [line[c11+1:c12], line[c12+1:c13], line[c13+1:c14], line[c14+1:c15], line[c15+1:c16]]
l1 = int(long[0])*45+int(long[1])*90+int(long[2])*270+int(long[3])*570+int(long[4])*720
l2 = int(long[0])+int(long[1])+int(long[2])+int(long[3])+int(long[4])
l1 /= l2
l3 = [45,90,270,570,720]
l5 = 777
l6 = 0
l7 = 0
for l4 in l3:
    l5 = min(l5,abs(l1-l4))
    if l5 == abs(l1-l4):
        l7 = l4
    l6 += 1
if l7 == 45:
    print("Longevity : poor")
elif l7 == 90:
    print("Longevity : weak")
elif l7 == 270:
    print("Longevity : moderate")
elif l7 == 570:
    print("Longevity : long lasting")
elif l7 == 720:
    print("Longevity : very long lasting")

sill = [line[c16+1:c17], line[c17+1:c18], line[c18+1:c19], line[c19+1:c20]]
s1 = int(sill[0])*20+int(sill[1])*100+int(sill[2])*180+int(sill[3])*300
s2 = int(sill[0])+int(sill[1])+int(sill[2])+int(sill[3])
s1 /= s2
s3 = [20,100,180,300]
s5 = 333
s6 = 0
s7 = 0
for s4 in s3:
    s5 = min(s5,abs(s1-s4))
    if s5 == abs(s1-s4):
        s7 = s4
    s6 += 1
if s7 == 20:
    print("Sillage : soft")
elif s7 == 100:
    print("Sillage : moderate")
elif s7 == 180:
    print("Sillage : heavy")
elif s7 == 300:
    print("Sillage : enormous")

rate = line[c20+1:c21]
print("Rate : "+str(rate))

count = line[c21+1:-1]
print("Count : "+count)
