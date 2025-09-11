import re

# 샘플 초기 재고 데이터 (테스트용)
itemList = [
    {"name": "아메리카노 캔", "code": "AME001", "price": 1500, "qty": 24},
    {"name": "라떼 캔", "code": "LAT001", "price": 1800, "qty": 12},
]

# 상품 코드 정규식 (영문 3글자 + 숫자 3글자)
code_pattern = re.compile(r'^[A-Za-z]{3}\d{3}$')

def validate_code(prompt="상품 코드: "):
    """영문 3글자 + 숫자 3글자 형식(예: ABC123)으로 정확히 받을 때까지 반복"""
    while True:
        code = input(prompt).strip()
        if code_pattern.match(code):
            return code.upper()
        print("❌ 잘못된 코드 형식입니다. 영문 3글자 + 숫자 3글자(예: ABC123)로 입력하세요.")

def get_nonnegative_int(prompt="수량 입력: "):
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

def add_product():
    """R - 상품 등록 기능"""
    print("\n=== R - 상품 등록 ===")
    name = input("상품 이름: ").strip()
    code = validate_code()
    if find_item(code):
        print(f"⚠️ 경고: '{code}' 코드는 이미 존재합니다.")
        return
    price = get_nonnegative_int("상품 가격: ")
    qty = get_nonnegative_int("초기 수량: ")
    itemList.append({"name": name, "code": code, "price": price, "qty": qty})
    print(f"✅ 신규 상품 {name} 등록 완료. 현재 수량: {qty}")

if __name__ == "__main__":
    # 이 부분은 단독 실행을 위한 테스트 코드입니다.
    print("상품 등록 기능을 테스트합니다.")
    add_product()
    print("\n현재 상품 목록:", itemList)
#ddddd