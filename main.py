Day = [1, 2, 3, 4, 5, 8, 11, 14]
Temp = [20.1, 22.3, 22.1, 22.7, 23.5, 24.0, 24.1, 23.7]

######################## 코드를 작성 시작 ########################
## Day는 1부터 시작 리스트 인덱싱은 0부터 시작 차이 보정

f_Temp = [0 for i in range(14)]
f_Day = [i + 1 for i in range(14)]

cnt = 0

for i in f_Day:
    if i not in Day:
        f_Temp[i - 1] = -9999
    else:
        f_Temp[i - 1] = Temp[cnt]
        cnt = cnt + 1

######################### 코드를 작성 끝 #########################

print(f_Day)
print(f_Temp)
