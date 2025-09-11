import re
code_pattern = re.compile(r'^[A-Za-z]{3}\d{3}$')

#---------- 상품 등록 함수 -------------------
# 상품 코드 정규식 (영문 3글자 + 숫자 3글자)

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

def find_item(code, itemList):
    """상품 코드로 상품 찾기"""
    code = code.upper()
    for item in itemList:
        if item['code'].upper() == code:
            return item
    return None

def add_product(itemList):
    """R - 상품 등록 기능"""
    print("\n=== R - 상품 등록 ===")
    name = input("상품 이름: ").strip()
    code = validate_code()
    if find_item(code, itemList):
        print(f"⚠️ 경고: '{code}' 코드는 이미 존재합니다.")
        return
    price = get_nonnegative_int("상품 가격: ")
    qty = get_nonnegative_int("초기 수량: ")
    itemList.append({"name": name, "code": code, "price": price, "qty": qty})
    print(f"✅ 신규 상품 {name} 등록 완료. 현재 수량: {qty}")

#---------상품 삭제 함수 ---------------
def validate_code(prompt="상품 코드: "):
    """영문 3글자 + 숫자 3글자 형식(예: ABC123)으로 정확히 받을 때까지 반복"""
    while True:
        code = input(prompt).strip()
        if code_pattern.match(code):
            return code.upper()
        print("❌ 잘못된 코드 형식입니다. 영문 3글자 + 숫자 3글자(예: ABC123)로 입력하세요.")

def find_item(code, itemList):
    """상품 코드로 상품 찾기"""
    code = code.upper()
    for item in itemList:
        if item['code'].upper() == code:
            return item
    return None

def delete_product(itemList):
    """D - 상품 삭제 기능"""
    print("\n=== D - 상품 삭제 ===")
    code_to_delete = validate_code("삭제할 상품 코드: ")
    item = find_item(code_to_delete, itemList)
    if item:
        itemList.remove(item)
        print(f"✅ 상품 '{item['name']}' ({item['code']})가 삭제되었습니다.")
    else:
        print(f"⚠️ 경고: '{code_to_delete}' 코드를 가진 상품을 찾을 수 없습니다.")

# -----------------조회 함수-----------------
def list_items(items, low_stock_threshold=None):
    """전체 재고 목록 출력 + 임계치 이하 상품 표시"""
    if not items:
        print("등록된 상품이 없습니다.")
        return

    print(f"현재 재고 (총 {len(items)}개)")
    print("-" * 60)
    print(f"{'코드':<10} | {'이름':<20} | {'단가':>8} | {'수량':>6}")
    print("-" * 60)
    for p in items:
        print(f"{p['code']:<10} | {p['name']:<20} | {p['price']:>8} | {p['qty']:>6}")
    print("-" * 60)

    if low_stock_threshold is not None:
        lows = [p for p in items if p['qty'] <= low_stock_threshold]
        if lows:
            print(f"임계치(≤{low_stock_threshold}) 이하 상품:")
            for p in lows:
                print(f" - {p['code']} {p['name']} (수량: {p['qty']})")
        else:
            print(f"임계치(≤{low_stock_threshold}) 이하 상품: 없음")

# --------------검색 함수--------------
def search_items(items):
    """상품 코드나 이름 일부로 검색"""
    key = input("검색어(이름/코드 일부): ").strip()
    if not key:
        print("검색어가 비어 있습니다.")
        return
    key_u = key.upper()

    results = [
        p for p in items
        if key_u in p.get('code', '').upper() or key_u in p.get('name', '').upper()
    ]

    if not results:
        print("검색 결과가 없습니다.")
        return

    print(f"검색 결과 (총 {len(results)}개)")
    print("-" * 60)
    print(f"{'코드':<10} | {'이름':<20} | {'단가':>8} | {'수량':>6}")
    print("-" * 60)
    for p in results:
        print(f"{p['code']:<10} | {p['name']:<20} | {p['price']:>8} | {p['qty']:>6}")
    print("-" * 60)


# ---------------- 입고 함수 ----------------
def product_input(itemList):
    print("=== 상품 입고 ===")

    # 코드 입력 및 검증
    while True:
        code = input("상품 코드: ").strip().upper()
        if code_pattern.match(code):
            break
        print("❌ 잘못된 코드 형식입니다. 영문 3글자 + 숫자 3글자(예: ABC123)로 입력하세요.")

    # 코드로 상품 찾기
    item = None
    for it in itemList:
        if it['code'].upper() == code:
            item = it
            break

    if item is None:
        print("해당 코드의 상품이 없습니다.")
        yn = input("신규 등록 후 입고하려면 Y, 취소하려면 아무키를 누르세요: ").strip().upper()
        if yn == 'Y':
            name = input("상품 이름: ").strip()

            # 가격 입력 (0 이상 정수만)
            while True:
                price = input("상품 가격: ").strip()
                if price.isdigit():
                    price = int(price)
                    break
                print("❌ 0 이상의 정수를 입력하세요.")

            # 수량 입력
            while True:
                qty = input("입고 수량: ").strip()
                if qty.isdigit():
                    qty = int(qty)
                    break
                print("❌ 0 이상의 정수를 입력하세요.")

            itemList.append({"name": name, "code": code, "price": price, "qty": qty})
            print(f"신규 상품 {name} 등록 및 입고 완료. 현재 수량: {qty}")
        else:
            print("입고 취소")
    else:
        # 기존 상품 수량 증가
        while True:
            qty = input("입고 수량: ").strip()
            if qty.isdigit():
                qty = int(qty)
                break
            print("❌ 0 이상의 정수를 입력하세요.")

        item['qty'] += qty
        print(f"{item['name']} 입고 완료. 현재 수량: {item['qty']}")


# ---------------- 출고 함수 ----------------
def product_output(itemList):
    print("=== 상품 출고 ===")

    # 코드 입력 및 검증
    while True:
        code = input("상품 코드: ").strip().upper()
        if code_pattern.match(code):
            break
        print("❌ 잘못된 코드 형식입니다. 영문 3글자 + 숫자 3글자(예: ABC123)로 입력하세요.")

    # 코드로 상품 찾기
    item = None
    for it in itemList:
        if it['code'].upper() == code:
            item = it
            break

    if item is None:
        print("해당 코드의 상품이 없습니다. 출고 불가.")
    else:
        # 출고 수량 입력
        while True:
            qty = input("출고 수량: ").strip()
            if qty.isdigit():
                qty = int(qty)
                break
            print("❌ 0 이상의 정수를 입력하세요.")

        if qty > item['qty']:
            print(f"출고 불가: 재고부족 (현재 재고: {item['qty']})")
        else:
            item['qty'] -= qty
            print(f"{item['name']} 출고 완료. 남은 수량: {item['qty']}")