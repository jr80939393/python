file = open('股票債券資訊表.txt','r',encoding='utf-8')
list_lines=file.readlines()
file.close()
for line in list_lines:
    print(line, end='')
    
dict1={'A':12,'B':20,'C':14,'D':35}
dict2={'A':14,'B':30,'C':15,'D':32}

while True:
    x = input('請輸入想要選擇的債券(A或C):')
    if x == 'A' or x == 'C' :
        break
    else :
        print("輸入錯誤，請重新輸入。")
        continue
while True:
    y = input('請輸入想要選擇的股票(B或D):')
    if y == 'B' or y == 'D' :
        break
    else :
        print("輸入錯誤，請重新輸入。")
        continue
        
a = float(dict1[x]/100)
b = float(dict1[y]/100)

if x == 'A':
    if y == 'B':
        c = 0.85
    else:
        c = -0.2
else:
    if y == 'B':
        c = -0.33
    else:
        c = 0.64
d=float(dict2[x]/100)
e=float(dict2[y]/100)

WD=((a-0.06)*e**2-(b-0.06)*c)/((a-0.06)*e**2+(b-0.06)*d**2-(a-0.06+b-0.06)*c)
WE=1-WD

if x == 'A' and y == 'B':
    print('WD=投資在A的最適比例=',WD)
    print('WE=投資在B的最適比例=',WE)
elif x == 'A' and y == 'D':
    print('WD=投資在A的最適比例=',WD)
    print('WE=投資在D的最適比例=',WE)
elif x == 'C' and y == 'B':
    print('WD=投資在C的最適比例=',WD)
    print('WE=投資在B的最適比例=',WE)
else :
    print('WD=投資在C的最適比例=',WD)
    print('WE=投資在D的最適比例=',WE)

print('測驗您的風險厭惡程度，現在你要玩刮刮樂，請選擇1~4其中一個選項。\n1.10000元一張，頭獎2億，中獎率0.000000001，回本率25%(回本率:不虧也不賺的機率\n2.2000元一張，頭獎1千萬，中獎率0.000001，回本率35%\n3.500元一張，頭獎2百萬，中獎率0.00001，回本率45%\n4.200元一張，頭獎50萬，中獎率0.001，回本率55%')
ans={'1':1,'2':3,'3':5,'4':7}
z=input('請輸入您的選擇:')
while z not in ans :
    z = input('輸入錯誤，請重新輸入。')
    
投資組合的預期報酬=WD*a+WE*b
P = (WD*d)**2+(WE*e)**2+2*(WD*d)*(WE*e)*(c/d*e)
投資組合的風險 = P**0.5
投資在風險性資產的比例 = (投資組合的預期報酬-0.06)/(ans[z]*P)
名字={'A':'國泰銀行債券','B':'台泥股票','C':'花旗銀行債券','D':'聯發科股票'}

print('投資組合的預期報酬:',投資組合的預期報酬)
print('投資組合的風險:',投資組合的風險)
print('投資在風險性資產的比例:',投資在風險性資產的比例)
