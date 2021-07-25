avg = []
for i in range(1,4):
    r1 = int(input("Enter oxyen level after round 1:"))
    r2 = int(input("Enter oxyen level after round 2:"))
    r3 = int(input("Enter oxyen level after round 3:"))
    a = (r1+r2+r3)/3
    avg.append(a)
if len(avg) == 0:
    print("All trainees are unfit!")
else:
    for i in avg:
        if i > 70:
            print("Trainer "+str(avg.index(i)+1)+" is fit. with value "+str(i)+"!")