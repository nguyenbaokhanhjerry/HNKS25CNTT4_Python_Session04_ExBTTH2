total = 0
count = 0

for day in range(1, 8, 1):
    revenue = int(input(f"Nhập doanh thu Ngày {day}: "))

    total = total + revenue

    if revenue >= 5000000:
        count = count + 1

print("Tổng doanh thu:", total)
print("Trung bình:", total / 7)
print("Số ngày đạt mục tiêu:", count)
