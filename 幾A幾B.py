import random
x = list(random.sample('0123456789',4))
n = 1
while n == 1 :
    a = 0
    b = 0
    y = list(input('請輸入不重複的四位號碼:'))
    t = ''
    for k in y:
        t = t + str(k)
    if (t == 'NEW') :
        x = list(random.sample('0123456789',4))
    else:
        if (t.isdigit()) and (len(set(y)) == 4):
            for i in range(4):
                if x[i]==y[i]:
                    a += 1
            for i in range(4):
                for j in range(4):
                    if i == j:
                        pass
                    else:
                        if x[i] == y[j]:
                            b += 1
            if a < 4:
                print(a,'A',b,'B')
            else:
                print('4A,解題完畢。')
                n = 0
        else:
            print('輸入錯誤!')
