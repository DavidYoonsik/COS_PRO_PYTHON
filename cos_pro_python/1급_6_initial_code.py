#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(pos):
    # 여기에 코드를 작성해주세요.
    answer = 0

    dx = [1, -1, 2, -2]
    dy = [ [2, -2], [-2, 2], [1, -1], [-1, 1] ]
    cx = ord(pos[0]) - ord("A") + 1
    cy = ord(pos[1]) - ord("0")


    ans = 0
    for i, v in enumerate(dx):
        for j in dy[i]:
            hor = cx + v
            ver = cy + j
            if hor > 0 and hor < 9 and ver > 0 and ver < 9:
                ans += 1

    print(ans)

    # for i in range(8):
    #     nx = cx + dx[i]
    #     ny = cy + dy[i]
    #     if nx >= 0 and nx < 8 and ny >= 0 and ny < 8:
    #         ans += 1
    #
    # answer = ans

    return ans

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
pos = "D4"
ret = solution(pos)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")