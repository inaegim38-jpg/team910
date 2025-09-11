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
