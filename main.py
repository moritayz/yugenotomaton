Q=['q0', 'q1', 'q2'] #状態の有限集合
Sigma=[0, 1] #入力記号の有限集合
F='q2' #最終状態
lange=4

numbers=[] #入力文字列を生成
for i in range(lange+1):
    for j in range(2**i):
        chars=list(f"{j:0{i}b}") #i桁の2進数(文字列)
        elem=list(map(lambda x:int(x), chars)) #整数に変換
        numbers.append(elem)
##print(numbers)

for input in numbers:
    jotai=Q[0] #初期状態
    senni=[jotai]
    for i in input:
        if jotai==Q[0]:
            if i==Sigma[0]:
                jotai=Q[0]
            elif i==Sigma[1]:
                jotai=Q[1]
        elif jotai==Q[1]:
            if i==Sigma[0]:
                jotai=Q[2]
            elif i==Sigma[1]:
                jotai=Q[0]
        elif jotai==Q[2]:
            if i==Sigma[0]:
                jotai=Q[0]
            elif i==Sigma[1]:
                jotai=Q[1]
        senni.append(jotai)

    if jotai==F:
        print("受理")
        print(input)
        print('->'.join(senni))
        print()