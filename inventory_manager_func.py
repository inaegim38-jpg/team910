# ---------------- 입고 함수 ----------------
def product_input():
    print("=== 상품 입고 ===")
    code_pattern = re.compile(r'^[A-Za-z]{3}\d{3}$')

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
def product_output():
    print("=== 상품 출고 ===")
    code_pattern = re.compile(r'^[A-Za-z]{3}\d{3}$')

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

