import streamlit as st

# Cấu hình tiêu đề trang web
st.set_page_config(page_title="Mini App Tính Lãi Tiết Kiệm", page_icon="💰")

st.title("💰 Ứng Dụng Tính Tiền Lãi Tiết Kiệm")
st.write("Nhập các thông số dưới đây để tính toán số tiền lãi cuối kỳ.")

# --- KHU VỰC NHẬP DỮ LIỆU ---
tiem_goc = st.number_input("Số tiền gửi ban đầu (VND):", min_value=0.0, value=10000000.0, step=1000000.0)
lai_suat = st.number_input("Lãi suất năm (%/năm):", min_value=0.0, value=5.5, step=0.1)
ky_han = st.number_input("Kỳ hạn gửi (tháng):", min_value=1, value=12, step=1)

loai_lai = st.radio("Chọn phương thức tính lãi:", ("Lãi đơn", "Lãi kép"))

# --- XỬ LÝ TÍNH TOÁN ---
# Đổi kỳ hạn từ tháng sang năm để tính toán
thoi_gian_nam = ky_han / 12

if st.button("Tính lãi"):
    if loai_lai == "Lãi đơn":
        # Công thức lãi đơn: A = P * (1 + r * t)
        tien_lai = tiem_goc * (lai_suat / 100) * thoi_gian_nam
        tong_tien = tiem_goc + tien_lai
    else:
        # Công thức lãi kép (giả định gộp lãi cuối kỳ/hàng năm tùy thuộc cấu hình, ở đây tính theo chuẩn thời gian)
        tong_tien = tiem_goc * ((1 + (lai_suat / 100)) ** thoi_gian_nam)
        tien_lai = tong_tien - tiem_goc

    # --- HIỂN THỊ KẾT QUẢ ---
    st.success("### Kết quả tính toán:")
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Tiền lãi nhận được", value=f"{tien_lai:,.0f} VND")
    with col2:
        st.metric(label="Tổng số tiền cuối kỳ (Gốc + Lãi)", value=f"{tong_tien:,.0f} VND")
