# nums = [2, 9, 4, 8]
#
# print(len(nums))
# print(sorted(nums))
# print(nums)
# nums.sort()
# print(nums)
#
#
# for x in nums:
#     print(x)
#
# for i in range(len(nums)):
#     print(nums[i])
#
#
# for (i, num) in enumerate(nums, start = 1):
#     print(i, num)
#
# students = ["A", "B", "C", "D"]
# math = [9.0, 7.5, 8.0]
# english = [8.5, 6.0, 9.0]
#
# for s, m, e in zip(students, math, english):
#     print(s, m, e)
#
#
# new_list = [n + 1 for n in nums]
# print(new_list)
#
# new_list_1 = [n + 1 for n in nums if n % 2 == 0]
# print(new_list_1)


# BÀI TẬP THỰC HÀNH 01
scores = [7.5, 8.0, 6.5, 9.0, 8.5]
# Cách 1
average = 0;
max = scores[0];
min = scores[0];
for score in scores:
    sum = 0;
    count = 0;
    for i in range(len(scores)):
        sum += scores[i]
        count += 1
        if(scores[i] > max):
            max = scores[i];
        if(scores[i] < min):
            min = scores[i];

average = sum / count
print(f"Điểm trung bình là: {average}")
print(f"Điểm lớn nhất là: {max}")
print(f"Điểm nhỏ nhất là: {min}")

# cách 2
# avg = sum(scores) / len(scores)
# print(f"Điểm trung bình là: {avg}")
# print(f"Điểm lớn nhất là: {max(scores)}")
# print(f"Điểm nhỏ nhất là: {min(scores)}")
# giỡn giỡn

# bài tập 2

nums = [5, -2, 8, -1, 0, 3, -10]

new_nums = [n for n in nums if n > 0]
print(new_nums)

array = [[1,2,3],[4,5],[6]]
new_array = [a for sub in nums for a in sub]
print(new_array)
print(new_array)