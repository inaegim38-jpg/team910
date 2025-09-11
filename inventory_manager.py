import re

# 샘플 초기 재고
itemList = [
    {"name": "아메리카노 캔", "code": "AME001", "price": 1500, "qty": 24},
    {"name": "라떼 캔",     "code": "LAT001", "price": 1800, "qty": 12},
]

code_pattern = re.compile(r'^[A-Za-z]{3}\d{3}$')

def validate_code(prompt="상품 코드: "):
    """영문 3글자 + 숫자 3글자 형식(예: ABC123)으로 정확히 받을 때까지 반복"""
    while True:
        code = input(prompt).strip()
        if code_pattern.match(code):
            return code.upper()  # 대문자로 통일
        print("❌ 잘못된 코드 형식입니다. 영문 3글자 + 숫자 3글자(예: ABC123)로 입력하세요.")

def get_nonnegative_int(prompt="숫자 입력: "):
    """0 이상의 정수만 받음"""
    while True:
        s = input(prompt).strip()
        if s.isdigit():
            return int(s)
        print("❌ 0 이상의 정수를 입력하세요.")

def find_item(code):
    """상품 코드로 상품 찾기"""
    code = code.upper()
    for item in itemList:
        if item['code'].upper() == code:
            return item
    return None

itemList=[]
item={'name': '', 'code': '', 'price': '', 'qty': ''}

while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    R - 상품 등록
    D - 상품 삭제
    L - 재고 조회
    S - 상품 검색
    I - 상품 입고
    O - 상품 출고
    Q - 프로그램 종료
    ''').upper() 


    # if choice =='I':
    #    print('상품 정보를 입력하시오.')
    #    name = input("상품 이름: ")
    #    code = input("상품 코드: ")
    #    price = input("상품 가격: ")
    #    qty = input("상품 수량: ") 

    if choice == 'I':
        print("=== 상품 입고 ===")
        code = validate_code()
        item = find_item(code)
        if item is None:
            print("해당 코드의 상품이 없습니다.")
            yn = input("신규 등록 후 입고하려면 Y, 취소하려면 아무키를 누르세요: ").strip().upper()
            if yn == 'Y':
                name = input("상품 이름: ").strip()
                price = get_nonnegative_int("상품 가격: ")
                qty = get_nonnegative_int("입고 수량: ")
                itemList.append({"name": name, "code": code, "price": price, "qty": qty})
                print(f"신규 상품 {name} 등록 및 입고 완료. 현재 수량: {qty}")
            else:
                print("입고 취소")
        else:
            qty = get_nonnegative_int("입고 수량: ")
            item['qty'] += qty
            print(f"{item['name']} 입고 완료. 현재 수량: {item['qty']}")

    if choice == 'O':
        print("=== 상품 출고 ===")
        code = validate_code()
        item = find_item(code)
        if item is None:
            print("해당 코드의 상품이 없습니다. 출고 불가.")
        else:
            qty = get_nonnegative_int("출고 수량: ")
            if qty > item['qty']:
                print(f"출고 불가: 재고부족 (현재 재고: {item['qty']})")
            else:
                item['qty'] -= qty
                print(f"{item['name']} 출고 완료. 남은 수량: {item['qty']}")