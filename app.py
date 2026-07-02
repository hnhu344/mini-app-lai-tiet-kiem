import streamlit as st

# 1. Cấu hình tiêu đề và biểu tượng trên tab trình duyệt
st.set_page_config(page_title="Mini App Tính Lãi Tiết Kiệm", page_icon="💰", layout="centered")

# 2. Tiêu đề chính của ứng dụng
st.title("💰 Ứng Dụng Tính Tiền Lãi Tiết Kiệm")

# 3. CHÈN ẢNH VÀO ĐẦU TRANG
# Tớ dùng một link ảnh stock sạch sẽ về chủ đề tài chính tiết kiệm. 
# Nếu nhóm bạn có file ảnh riêng (ví dụ: banner.jpg) đã up lên GitHub, hãy thay link dưới đây bằng tên file "banner.jpg" nhé.
st.image(
    "https://images.unsplash.com/photo-1579621970563-ebec7560ff3e?q=80&w=1000&auto=format&fit=crop", 
    caption="Lập kế hoạch tài chính - Tích lũy cho tương lai", 
    use_container_width=True
)

st.write("Nhập các thông số dưới đây để tính toán số tiền lãi cuối kỳ của bạn.")

# 4. KHU VỰC NHẬP DỮ LIỆU CỦA NGƯỜI DÙNG
st.subheader("📌 Thông tin khoản gửi")

# Nhập số tiền gốc
tiem_goc = st.number_input("Số tiền gửi ban đầu (VND):", min_value=0.0, value=10000000.0, step=1000000.0, format="%.0f")

# Tạo 2 cột để giao diện gọn gàng hơn (Lãi suất và Kỳ hạn nằm song song)
col_input1, col_input2 = st.columns(2)
with col_input1:
    lai_suat = st.number_input("Lãi suất năm (%/năm):", min_value=0.0, value=5.5, step=0.1)
with col_input2:
    ky_han = st.number_input("Kỳ hạn gửi (tháng):", min_value=1, value=12, step=1)

# Chọn loại lãi đơn hay lãi kép
loai_lai = st.radio("Chọn phương thức tính lãi:", ("Lãi đơn", "Lãi kép"), horizontal=True)

# 5. XỬ LÝ TÍNH TOÁN KHI BẤM NÚT
# Đổi kỳ hạn từ tháng sang năm để khớp công thức tiêu chuẩn
thoi_gian_nam = ky_han / 12

if st.button("🚀 Tính Tiền Lãi", type="primary"):
    if loai_lai == "Lãi đơn":
        # Công thức lãi đơn: Tiền lãi = Gốc * Lãi suất * Thời gian
        tien_lai = tiem_goc * (lai_suat / 100) * thoi_gian_nam
        tong_tien = tiem_goc + tien_lai
    else:
        # Công thức lãi kép cuối kỳ: Tổng tiền = Gốc * (1 + r)^t
        tong_tien = tiem_goc * ((1 + (lai_suat / 100)) ** thoi_gian_nam)
        tien_lai = tong_tien - tiem_goc

    # 6. HIỂN THỊ KẾT QUẢ ĐÃ TÍNH TOÁN
    st.markdown("---") # Đường kẻ ngang phân cách
    st.success("### 🎉 Kết quả tính toán:")
    
    col_res1, col_res2 = st.columns(2)
    with col_res1:
        st.metric(label="Tổng tiền lãi nhận được", value=f"{tien_lai:,.0f} VND")
    with col_res2:
        st.metric(label="Tổng số tiền nhận về (Gốc + Lãi)", value=f"{tong_tien:,.0f} VND")
