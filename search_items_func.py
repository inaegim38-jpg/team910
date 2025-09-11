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
