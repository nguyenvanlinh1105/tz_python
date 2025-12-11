# Bài tập 2: Thống kê sản phẩm & hóa đơn
# Đề bài:
# Cho sẵn dữ liệu ban đầu:
# # Mỗi sản phẩm là 1 tuple (product_id, name, price)
products = [
    (1, "Ban Phim", 250_000),
    (2, "Chuot", 150_000),
    (3, "Man Hinh", 3_000_000),
    (4, "Tai Nghe", 500_000),
]
# Danh sách đơn hàng (list dict)
orders = [
    {"order_id": "HD01", "items": [1, 2, 4]},
    {"order_id": "HD02", "items": [2, 3]},
    {"order_id": "HD03", "items": [1, 4]},
]
# Yêu cầu:
# a. Tạo một dict product_map từ products để tra cứu nhanh theo product_id với dạng:
#     {
#         1: {"name": "Ban Phim", "price": 250_000},
#         2: {"name": "Chuot", "price": 150_000},
#         ...
#     }
# b. Với mỗi hóa đơn trong orders, hãy tính tổng tiền của hóa đơn đó, lưu vào key mới "total" trong từng dict hóa đơn
# Hints:
# items là list các product_id
# tra giá ở product_map (dict)
# cộng dồn
# c. In ra danh sách hóa đơn theo format:
#     HD01: 3 san pham, Tong tien = ...
#     HD02: ...
# d. Tạo một set all_products_sold chứa tất cả product_id đã từng được bán trong mọi hóa đơn, sau đó in ra:
#   So luong san pham khac nhau da ban: <len(all_products_sold)>



print("BÀI TẬP 2.a")

product_map = {}
for pid, name, price in products:
    product_map[pid] = {"name": name, "price": price}

print(product_map)


print("BÀI TẬP 2.b")
for order in orders:
    sum = 0;
    items = order["items"]
    for item in items:
        sum += product_map[item]["price"]
    order["total"] = sum

print(orders)


print("BÀI TẬP 2.c")

for order in orders:
    count = len(order["items"])
    print(f"{order['order_id']}: {count} san pham, Tong tien = {order['total']}")


print("BÀI TẬP 2.d")

all_products_sold = set()

for order in orders:
    for pid in order["items"]:
        all_products_sold.add(pid)

print(f"So luong san pham khac nhau da ban: {len(all_products_sold)}")
