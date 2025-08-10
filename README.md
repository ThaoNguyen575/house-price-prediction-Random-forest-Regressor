# Dự đoán giá nhà ở California

## 1. Dataset
Dataset gồm **10 cột** với thông tin chi tiết như sau:

| #  | Column              | Non-Null Count | Dtype   | Mô tả                     |
|----|---------------------|----------------|---------|---------------------------|
| 0  | longitude           | 20640          | float64 | Kinh độ                   |
| 1  | latitude            | 20640          | float64 | Vĩ độ                     |
| 2  | housing_median_age  | 20640          | float64 | Tuổi trung bình của nhà    |
| 3  | total_rooms         | 20640          | float64 | Tổng số phòng             |
| 4  | total_bedrooms      | 20433          | float64 | Tổng số phòng ngủ         |
| 5  | population          | 20640          | float64 | Dân số khu vực            |
| 6  | households          | 20640          | float64 | Số hộ gia đình            |
| 7  | median_income       | 20640          | float64 | Thu nhập trung vị         |
| 8  | median_house_value  | 20640          | float64 | Giá nhà trung vị (USD)    |
| 9  | ocean_proximity     | 20640          | object  | Khoảng cách tới biển       |

---

## 2. Mô hình
Mô hình sử dụng thuật toán **Random Forest Regressor** để dự đoán giá nhà dựa trên các đặc trưng như thu nhập trung bình, số phòng ngủ, vị trí địa lý, v.v. Dữ liệu được lấy từ bộ dữ liệu housing.csv.

### Tiền xử lý dữ liệu
- Điền giá trị trung bình cho các giá trị thiếu trong cột `total_bedrooms`.
- Mã hóa biến phân loại `ocean_proximity` thành giá trị số tương ứng.
- Tách dữ liệu thành tập huấn luyện và tập kiểm tra theo tỷ lệ 80% - 20%.

### Mô hình và huấn luyện
- Sử dụng `RandomForestRegressor` với các siêu tham số:  
  - số cây: 100 (`n_estimators=100`)  
  - độ sâu tối đa: 20 (`max_depth=20`)  
  - số mẫu tối thiểu để chia nhánh: 10 (`min_samples_split=10`)  
  - số mẫu tối thiểu ở lá: 4 (`min_samples_leaf=4`)  
- Huấn luyện trên tập huấn luyện.

### Đánh giá mô hình
- Các metric đánh giá: MSE, RMSE, MAE và R² score.
- Mô hình đạt R² khoảng 0.81 trên tập kiểm tra, cho thấy khả năng dự đoán tốt.
- Điểm số huấn luyện và kiểm tra lần lượt là 0.92 và 0.81, cho thấy mô hình không bị overfitting nghiêm trọng.

---

## 3. Kết quả mô hình

| Metric       | Giá trị          |
|--------------|------------------|
| MSE          | 2,553,351,574.61 |
| RMSE         | 50,530.70        |
| MAE          | 32,471.42        |
| R² Score     | 0.81             |

---

## 4. Hướng dẫn cài đặt môi trường
Chạy lệnh sau để cài đặt các thư viện cần thiết:

```bash
pip install -r requirements.txt
```
---

## 5. Hướng phát triển
Mở rộng mô hình với các kỹ thuật khác hoặc tiền xử lý dữ liệu nâng cao để cải thiện độ chính xác.
