'''
    S 등급 : 5% 할인
    G 등급 : 10% 할인
    V 등급 : 15% 할인

    총 할인 금액 VS. 지불금액
'''

def solution(user_price_data):
    tot_dsc_price = 0

    "UserName, UserGrade, Price"

    if user_price_data['UserGrade'] == "S":
        tot_dsc_price = user_price_data['Price'] * 0.05
    elif user_price_data['UserGrade'] == "G":
        tot_dsc_price = user_price_data['Price'] * 0.1
    elif user_price_data['UserGrade'] == "V":
        tot_dsc_price = user_price_data['Price'] * 0.15

    return user_price_data['UserName'], tot_dsc_price
