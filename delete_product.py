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

def find_item(code):
    """상품 코드로 상품 찾기"""
    code = code.upper()
    for item in itemList:
        if item['code'].upper() == code:
            return item
    return None

def delete_product():
    """D - 상품 삭제 기능"""
    print("\n=== D - 상품 삭제 ===")
    code_to_delete = validate_code("삭제할 상품 코드: ")
    item = find_item(code_to_delete)
    if item:
        itemList.remove(item)
        print(f"✅ 상품 '{item['name']}' ({item['code']})가 삭제되었습니다.")
    else:
        print(f"⚠️ 경고: '{code_to_delete}' 코드를 가진 상품을 찾을 수 없습니다.")

if __name__ == "__main__":
    # 이 부분은 단독 실행을 위한 테스트 코드입니다.
    print("상품 삭제 기능을 테스트합니다.")
    delete_product()
    print("\n현재 상품 목록:", itemList)