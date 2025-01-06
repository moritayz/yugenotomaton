
Q=['q0', 'q1', 'q2']
Sigma=[0, 1]
F='q2'

jotai=Q[0]

numbers=[]
for i in range(4):
    for j in range(2**i):
        chars=list(f"{j:0{i}b}")
        elem=list(map(lambda x:int(x), chars))
        numbers.append(elem)
print(numbers)

for input in numbers:
    for 
        if jotai==Q[0] && input==Sigma[0]:
            jotai=Q[0]
        if jotai==Q[0] && input==Sigma[1]:
            jotai=Q[1]
        if jotai==Q[1] && input==Sigma[0]:
            jotai=Q[2]
        if jotai==Q[1] && input==Sigma[1]:
            jotai=Q[0]
        if jotai==Q[2] && input==Sigma[0]:
            jotai=Q[0]
        if jotai==Q[2] && input==Sigma[1]:
            jotai=Q[1]

    if jotai==Q[2]:
        print(input)'''
