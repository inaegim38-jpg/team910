# add_product.py

def add_product(products):
    """
    상품 등록 기능:
    사용자로부터 상품명, 상품코드, 단가, 수량을 입력받아
    딕셔너리에 추가합니다.
    """
    print("\n📦 상품 등록")
    name = input("상품명: ")
    code = input("상품코드: ")
    try:
        price = int(input("단가: "))
        qty = int(input("수량: "))
    except ValueError:
        print("🚨 오류: 단가와 수량은 숫자로 입력해야 합니다.")
        return products

    if code in products:
        print(f"⚠️ 경고: '{code}' 코드는 이미 존재합니다.")
    else:
        products[code] = {"name": name, "price": price, "qty": qty}
        print(f"✅ 상품코드 '{code}'가 목록에 추가되었습니다.")
    return products

if __name__ == '__main__':
    # 이 부분은 단독 실행을 위한 테스트 코드입니다.
    my_products = {}
    print("상품 등록 기능을 테스트합니다.")
    my_products = add_product(my_products)
    print("\n현재 상품 목록:", my_products)