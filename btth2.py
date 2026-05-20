total_revenue = 0
revenue_days = 0

for day in range(1, 8, 1):
    revenue = int(input(f"Nhập doanh thu Ngày {day}: "))

    total_revenue += revenue

    if revenue >= 5000000:
        revenue_days += 1

average = total_revenue / 7

print("\n--- BÁO CÁO DOANH THU TUẦN ---")
print("Tổng doanh thu:", total_revenue)
print("Trung bình mỗi ngày:", average)
print("Số ngày đạt mục tiêu:", revenue_days)