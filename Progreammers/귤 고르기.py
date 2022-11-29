from collections import Counter

# 답변 링크 : https://velog.io/@blaze241/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Lv.2-%EA%B7%A4-%EA%B3%A0%EB%A5%B4%EA%B8%B0
class mandrine:
    k = 2
    tangerine = [1, 1, 1, 1, 2, 2, 2, 3]

    def solution(k: int, tangerine: list):

        """
        종류가 최소화되어야한다. 이는 무엇인가?
        가장 많은 수량을 갖고있는 크기 의 갯수부터 뺀다.
        -> 가장 많이 중복되는 크기순으로 정렬한다.
        -> k개에서 계속 빼나간다.
        -> k가 0이나 더 낮아진다.
        -> 그러면 리턴한다.
        """
        answer = 0
        types_amount = dict(Counter(tangerine))

        # lambda x : x[1]
        types_amount_list = sorted(types_amount.items(), key=lambda x: x[1], reverse=True)
        print(types_amount_list)
        for tup in types_amount_list:
            if k > 0:
                k = k - tup[1]
                answer = answer + 1
            else:
                break

        return answer

    print(solution(k=k, tangerine=tangerine))
