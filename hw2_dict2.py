dict1={'angel':'天使','angle':'角度','cat':'貓','dog':'狗'}
x=input('請使用者輸入要查詢的單字:')
print(dict1.get(x,'找不到這個水果對應的值'))
nameeng=dict1.copy()
for name in nameeng.keys():
    print({name},':',{nameeng[name]})
