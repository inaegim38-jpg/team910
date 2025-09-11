# delete_product.py

def delete_product(products):
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
    return products

if __name__ == '__main__':
    # 이 부분은 단독 실행을 위한 테스트 코드입니다.
    my_products = {
        "AME001": {"name": "아메리카노 캔", "price": 1500, "qty": 24},
        "LAT001": {"name": "라떼 캔", "price": 1800, "qty": 12}
    }
    print("상품 삭제 기능을 테스트합니다.")
    my_products = delete_product(my_products)
    print("\n현재 상품 목록:", my_products)