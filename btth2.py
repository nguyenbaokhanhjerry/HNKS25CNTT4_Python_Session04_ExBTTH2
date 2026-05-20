total = 0
count = 0

for day in range(7):
    revenue = int(input("Nhập doanh thu: "))

    total = total + revenue

    if revenue >= 5000000:
        count = count + 1

print("Tổng doanh thu:", total)
print("Trung bình:", total / 7)
print("Số ngày đạt mục tiêu:", count)
