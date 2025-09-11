# inventory.py

# 상품 데이터가 저장될 딕셔너리 (메모리에서 관리)
# 프로그램이 종료되면 데이터는 사라집니다.
products = {
    "AME001": {"name": "아메리카노 캔", "price": 1500, "qty": 24},
    "LAT001": {"name": "라떼 캔", "price": 1800, "qty": 12}
}

def add_product():
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
        return

    # 상품 코드를 키(key)로 사용하여 딕셔너리에 추가
    if code in products:
        print(f"⚠️ 경고: '{code}' 코드는 이미 존재합니다.")
    else:
        products[code] = {"name": name, "price": price, "qty": qty}
        print(f"✅ 상품코드 '{code}'가 목록에 추가되었습니다.")

def delete_product():
    """
    상품 삭제 기능:
    사용자로부터 삭제할 상품코드를 입력받아
    딕셔너리에서 해당 상품을 삭제합니다.
    """
    print("\n🗑️ 상품 삭제")
    code_to_delete = input("삭제할 상품코드: ")
    
    if code_to_delete in products:
        del products[code_to_delete]
        print(f"✅ 상품코드 '{code_to_delete}'가 삭제되었습니다.")
    else:
        print(f"⚠️ 경고: '{code_to_delete}' 코드를 가진 상품을 찾을 수 없습니다.")

def main():
    """
    메인 함수:
    사용자 입력을 받아 각 기능을 호출합니다.
    """
    while True:
        print("\n--- 재고 관리 시스템 ---")
        print("기능 선택: (R)상품등록, (D)상품삭제, (Q)종료")
        choice = input("> ").upper()

        if choice == 'R':
            add_product()
        elif choice == 'D':
            delete_product()
        elif choice == 'Q':
            print("👋 시스템을 종료합니다.")
            break
        else:
            print("❌ 잘못된 입력입니다. 다시 시도해주세요.")

if __name__ == "__main__":
    main()