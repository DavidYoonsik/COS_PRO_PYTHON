#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(num):
    # 여기에 코드를 작성해주세요.
    answer = 0

    num2 = num + 1

    num3 = str(num2)

    res = ""
    for i in num3:
        print(i)
        if i == '0':
            res += '1'
        else:
            res += i

    print(int(res))

    return int(res)


#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
num = 9949999;
ret = solution(num)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")