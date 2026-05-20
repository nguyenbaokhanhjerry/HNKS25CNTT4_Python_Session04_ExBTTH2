total = 0
count = 0

for day in range(1, 8, 1):
    revenue = int(input(f"Nhập doanh thu Ngày {day}: "))

    total = total + revenue

    if revenue >= 5000000:
        count = count + 1
print(" --- BÁO CÁO DOANH THU TUẦN RIKKEI STORE")
print("Tổng doanh thu cả tuần:", total, "VND")
print("Doanh thu trung bình mỗi ngày:", total / 7, "VND")
print("Số ngày đạt doanh thu mục tiêu (>= 5,000,000 VND):", count)
