f1 = open("out.txt", 'w')
f1.write("Name, Group, MainNote1, MainNote2, MainNote3, Season, Time, Longevity, Sillage, Rate, Count\n")
for i in range(1,4):
    f2 = open("out"+str(i)+".txt", 'r')
    lines = f2.readlines()
    for line in lines:
        try:
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

            A = line[:c1]
            B = line[c1+1:c2]
            C = line[c2+1:c3]
            D = line[c3+1:c4]
            E = line[c4+1:c5]

            season = [line[c5+1:c6], line[c6+1:c7], line[c7+1:c8], line[c8+1:c9]]
            s1 = int(season[0])+int(season[1])+int(season[2])+int(season[3])
            if int(season[0])/s1*100 >= 60:
                F = "Spring"
            elif int(season[1])/s1*100 >= 60:
                F = "Summer"
            elif int(season[2])/s1*100 >= 60:
                F = "Fall"
            elif int(season[3])/s1*100 >= 60:
                F = "Winter"
            elif (int(season[0])+int(season[1]))/s1*100 >= 65:
                F = "Spring/Summer"
            elif (int(season[2])+int(season[3]))/s1*100 >= 65:
                F = "Fall/Winter"
            else:
                F = "All Season"

            dn = [line[c9+1:c10], line[c10+1:c11]]
            d1 = int(dn[0])+int(dn[1])
            if int(dn[0])/d1*100 > 60:
                G = "Day"
            elif int(dn[1])/d1*100 > 60:
                G = "Night"
            else:
                G = "All Time"

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
                H = "poor"
            elif l7 == 90:
                H = "weak"
            elif l7 == 270:
                H = "moderate"
            elif l7 == 570:
                H = "long lasting"
            elif l7 == 720:
                H = "very long lasting"

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
                I = "soft"
            elif s7 == 100:
                I = "moderate"
            elif s7 == 180:
                I = "heavy"
            elif s7 == 300:
                I = "enormous"

            rate = line[c20+1:c21]
            J = str(rate)

            count = line[c21+1:-1]
            K = str(count)

            f1.write(A+","+B+","+C+","+D+","+E+","+F+","+G+","+H+","+I+","+J+","+K+"\n")
        except:
            pass
    f2.close()
f1.close()
