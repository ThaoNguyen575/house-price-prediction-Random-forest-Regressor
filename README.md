# Dự đoán giá nhà ở California

## Dataset
Dataset gồm **10 cột** với thông tin chi tiết như sau:

| #  | Column              | Non-Null Count | Dtype   | Mô tả |
|----|--------------------|----------------|---------|-------|
| 0  | longitude          | 20640          | float64 | Kinh độ |
| 1  | latitude           | 20640          | float64 | Vĩ độ |
| 2  | housing_median_age | 20640          | float64 | Tuổi trung bình của nhà |
| 3  | total_rooms        | 20640          | float64 | Tổng số phòng |
| 4  | total_bedrooms     | 20433          | float64 | Tổng số phòng ngủ |
| 5  | population         | 20640          | float64 | Dân số khu vực |
| 6  | households         | 20640          | float64 | Số hộ gia đình |
| 7  | median_income      | 20640          | float64 | Thu nhập trung vị |
| 8  | median_house_value | 20640          | float64 | Giá nhà trung vị (USD) |
| 9  | ocean_proximity    | 20640          | object  | Khoảng cách tới biển |

---

## Mô tả dự án
Dự án sử dụng mô hình **RandomForestRegressor** để dự đoán giá nhà tại California dựa trên các thông tin đặc trưng như vị trí địa lý, số phòng, thu nhập trung vị và khoảng cách tới biển.
Dự án được triển khai bằng **Streamlit** để deploy giao diện web
---

## Kết quả mô hình
- **MSE**: `2,553,351,574.61`
- **RMSE**: `50,530.70`
- **MAE**: `32,471.42`
- **R² Score**: `0.81`
---

## Chạy file requirment
pip install -r requirements.txt

