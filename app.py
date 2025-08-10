import streamlit as st
import pickle
import numpy as np

# Load mô hình đã lưu
with open('house_price_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("Ứng dụng dự đoán giá nhà")

st.write("""
Nhập các thông tin về đặc điểm căn nhà và khu vực để dự đoán giá nhà (đơn vị: USD).
""")

# Nhập dữ liệu từ người dùng (thay đổi theo biến của bạn)
longitude = st.number_input("Kinh độ (longitude)", value=-122.23)
latitude = st.number_input("Vĩ độ (latitude)", value=37.88)
housing_median_age = st.number_input("Tuổi trung bình nhà (housing median age)", value=41)
total_rooms = st.number_input("Tổng số phòng (total rooms)", value=880)
total_bedrooms = st.number_input("Tổng số phòng ngủ (total bedrooms)", value=129)
population = st.number_input("Dân số (population)", value=322)
households = st.number_input("Số hộ gia đình (households)", value=126)
median_income = st.number_input("Thu nhập trung bình (median income)", value=8.3252)

# Biến categorical: ocean_proximity (đã map thành số)
st.write("Vị trí gần biển (ocean proximity):")
ocean_options = {
    "Gần biển <1h": 1,
    "Nội địa (inland)": 2,
    "Gần biển (near ocean)": 3,
    "Gần vịnh (near bay)": 4,
    "Đảo (island)": 5
}
ocean_proximity = st.selectbox("Chọn vị trí", options=list(ocean_options.keys()))
ocean_proximity_value = ocean_options[ocean_proximity]

if st.button("Dự đoán giá nhà"):
    # Tạo input cho model, đảm bảo đúng thứ tự và số chiều
    X = np.array([[longitude, latitude, housing_median_age, total_rooms, total_bedrooms,
                   population, households, median_income, ocean_proximity_value]])
    
    # Dự đoán
    predicted_price = model.predict(X)[0]
    
    # Hiển thị kết quả dưới dạng tiền tệ (USD hoặc bạn muốn)
    st.success(f"Giá nhà dự đoán: ${predicted_price:,.2f} USD")
