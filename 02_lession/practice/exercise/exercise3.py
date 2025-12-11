# Bài tập 3: Hệ thống tag bài viết & người dùng
# Đề bài:
# Cho sẵn dữ liệu ban đầu:
# # Danh sách user: list tuple (user_id, name)
users = [
    ("U01", "Alice"),
    ("U02", "Bob"),
    ("U03", "Charlie"),
]
#
# # Dict bài viết: key là post_id, value là dict thông tin
posts = {
    "P01": {
        "title": "Hoc Python co ban",
        "author_id": "U01",
        "tags": {"python", "beginner"},
    },
    "P02": {
        "title": "Lam viec voi List va Dict",
        "author_id": "U01",
        "tags": {"python", "data-structure"},
    },
    "P03": {
        "title": "Gioi thieu HTML CSS",
        "author_id": "U02",
        "tags": {"web", "frontend"},
    },
}
# Yêu cầu:
# a. Tạo một dict user_map từ users, map user_id sang name
#     Ví dụ:
#     {
#         "U01": "Alice",
#         "U02": "Bob",
#         "U03": "Charlie",
#     }
# b. Dùng vòng lặp duyệt posts.items() để in ra:
#     [P01] Hoc Python co ban - Alice - Tags: python, beginner
#     [P02] ...
# Hints:
# lấy author_id từ dict posts
# tra tên ở user_map
# tags là set, cần chuyển sang list/sorted trước rồi nối thành chuỗi
# c. Tạo một set all_tags chứa toàn bộ tag xuất hiện trong mọi bài viết
# Hints: duyệt từng post, lấy post["tags"] (set), dùng update() để dồn vào all_tags
# d. Tạo một dict tag_counter để đếm số bài viết chứa mỗi tag
#   Ví dụ:
#   {
#         "python": 2,
#         "beginner": 1,
#         "data-structure": 1,
#         "web": 1,
#         "frontend": 1,
#   }
# Hints:
# Khởi tạo tag_counter = {}
# Duyệt từng post, với mỗi tag trong post["tags"]:
# nếu tag chưa có trong dict => gán = 1
# nếu đã có => tăng lên 1


print("BÀI TẬP 3.a")
user_map = {}
for uid, name in users:
    user_map[uid] = name

print(user_map)

print("BÀI TẬP 3.b")
for post_id, info in posts.items():
    title = info["title"]
    author_name = user_map.get(info["author_id"])
    tags = ", ".join(sorted(info["tags"]))

    print(f"[{post_id}] {title} - {author_name} - Tags: {tags}")

print("BÀI TẬP 3.c")
all_tags = set()
for info in posts.values():
    all_tags.update(info["tags"])

print(all_tags)
print(f"Total tags: {len(all_tags)}")


print("BÀI TẬP 3.d")
tag_counter = {}
for info in posts.values():
    for tag in info["tags"]:
        if tag not in tag_counter:
            tag_counter[tag] = 1
        else:
            tag_counter[tag] += 1

print(tag_counter)

