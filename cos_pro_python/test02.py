'''
    S 등급 : 5% 할인
    G 등급 : 10% 할인
    V 등급 : 15% 할인

    총 할인 금액 VS. 지불금액
'''

from pprint import pprint

def solution(user_price_data):
    import json

    tot_dsc_price = 0

    "UserName, UserGrade, Price"
    answer = []

    for i in user_price_data:

        if i['UserGrade'] == "S":
            tot_dsc_price = i['Price'] * 0.05
        elif i['UserGrade'] == "G":
            tot_dsc_price = i['Price'] * 0.1
        elif i['UserGrade'] == "V":
            tot_dsc_price = i['Price'] * 0.15

        answer.append(
            {
                'UserName': i['UserName'],
                'Price': tot_dsc_price
            }
        )

    return json.dumps(answer)

data = [
    {
        'UserName' : 'David',
        'UserGrade' : 'S',
        'Price' : 100000
    },
    {
        'UserName' : 'GoLuck',
        'UserGrade' : 'G',
        'Price' : 150000
    },
    {
        'UserName' : 'Spark',
        'UserGrade' : 'V',
        'Price' : 130000
    },
    {
        'UserName' : 'Yarn',
        'UserGrade' : 'V',
        'Price' : 500000
    }
]

pprint(solution(data))
