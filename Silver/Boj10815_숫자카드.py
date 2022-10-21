#https://www.acmicpc.net/problem/10815
#이진 탐색 사용
import sys

#기초 데이터 저장
#찾고자 하는것 : target
n = int(input())
card = list(map(int, sys.stdin.readline().split()))
m = int(input())
check = list(map(int, sys.stdin.readline().split()))

card.sort()


#이진 탐색의 기초
#개념 : 전체를 우선 정렬한다음 둘로 나눈다.
# 가운데서부터 비교한다. 타겟이 비교대상보다 크면 더 큰 비교대상을 찾을수 있게 큰쪽으로 밀고, 타겟이 비교대상보다 작으면 작은쪽으로 민다. 타겟과 비교대상이 같으면 그대로 리턴한다.
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


for i in range(m):
    if binary_search(card, check[i], 0, n - 1) is not None:
        print(1, end='')
    else:
        print(0, end='')
