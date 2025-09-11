import re
import inventory_manager_func as imf

# 샘플 초기 재고
itemList = [
    {"name": "아메리카노 캔", "code": "AME001", "price": 1500, "qty": 24},
    {"name": "라떼 캔",     "code": "LAT001", "price": 1800, "qty": 12},
]

while True:
    choice = input('''
    다음 중에서 하실 일을 골라주세요 :
    R - 상품 등록
    D - 상품 삭제
    L - 재고 조회
    S - 상품 검색
    I - 상품 입고
    O - 상품 출고
    Q - 프로그램 종료
    ''').upper().strip()

    if choice == 'R':
        pass
    elif choice == 'D':
        pass
    elif choice == 'L':
        imf.list_items(itemList)
    elif choice == 'S':
        imf.search_items(itemList)
    if choice == 'I':
        imf.product_input()
    elif choice == 'O':
        imf.product_output()
    elif choice == 'Q':
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 선택입니다. 다시 입력하세요.")
