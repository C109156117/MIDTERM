M=int(input("月:"))
D=int(input("日:"))
s=(M*2+D)%3
if s==0:
    print("普通")
elif s==1:
    print("吉")
elif s==2:
    print("大吉")