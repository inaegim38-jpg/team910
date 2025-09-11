from list_items_func import list_items
from search_items_func import search_items
# 다른 기능도 같은 방식으로 import

def main():
    items = [
        {"name": "아메리카노 캔", "code": "AME001", "price": 1500, "qty": 24},
        {"name": "라떼 캔", "code": "LAT001", "price": 1800, "qty": 12},
    ]

    while True:
        choice = input("메뉴 선택 (L=조회, S=검색, Q=종료): ").upper()

        if choice == "L":
            list_items(items, low_stock_threshold=5)
        elif choice == "S":
            search_items(items)
        elif choice == "Q":
            break
        else:
            print("잘못된 입력입니다.")

if __name__ == "__main__":
    main()
