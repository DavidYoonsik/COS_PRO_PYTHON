#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(n):
    # 여기에 코드를 작성해주세요.
    answer = 0

    # n * n
    a = [[i, j] for i in range(n) for j in range(n)]


    # 0시작, 4끝, 4시작, 0끝, 1시작, 3끝, 3시작, 1끝, 2시작
    # 0시작, 3끝, 3시작, 0끝, 1시작, 2끝, 2시작
    # 0시작, 2끝, 2시작, 0끝, 1시작

    cnt=0
    st=0
    et=n-1

    while cnt < 9 and st <= et:

        for j in range(n**2):
            if len(a[j]) == 1:
                continue
            if a[j][0] == st:
                cnt += 1
                a.pop(j)
                a.insert(j, [cnt])

        for k in range(n**2):
            if len(a[k]) == 1:
                continue

            if a[k][1] == et:
                cnt += 1
                a.pop(k)
                a.insert(k, [cnt])

        for k in range(n**2):
            if len(a[k]) == 1:
                continue

            if a[k][0] == et:
                cnt += 1
                a.pop(k)
                a.insert(k, [cnt])

        for k in range(n ** 2):
            if len(a[k]) == 1:
                continue

            if a[k][1] == st:
                cnt += 1
                a.pop(k)
                a.insert(k, [cnt])

        st += 1
        et -= 1


    total = 0
    res = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            print(res[i][j], i, j)
            res[i][j] = a.pop(0)[0]
            if i == j:
                total += res[i][j]


    print("total", total)

    # [0,0],[0,1],[0,2], ... ,[0,n],
    # [1,n], [2,n], ... ,[n,n],[n,n-1],[n, n-2], ... ,[n. 1]

    return answer


#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
n1 = 4
ret1 = solution(n1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")
    
n2 = 2
ret2 = solution(n2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")