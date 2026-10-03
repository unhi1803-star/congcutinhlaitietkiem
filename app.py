import streamlit as st
st.image("Thiết kế chưa có tên3.png")
# ==============================
# CẤU HÌNH TRANG
# ==============================

st.set_page_config(
    page_title="Tính lãi gửi tiết kiệm",
    page_icon="💰",
    layout="centered"
)

st.title("💰 APP TÍNH LÃI GỬI TIẾT KIỆM_NGUYỄN THỊ UYÊN NHI")
st.write("Nhập thông tin tiền gửi để tính tiền lãi và số tiền nhận được.")

st.divider()

# ==============================
# NHẬP DỮ LIỆU
# ==============================

st.subheader("📌 Thông tin tiền gửi")

# Số tiền gửi
so_tien = st.number_input(
    "Số tiền gửi (VNĐ)",
    min_value=0.0,
    value=500_000_000.0,
    step=1_000_000.0,
    format="%.0f"
)

# Kỳ hạn
ky_han = st.number_input(
    "Kỳ hạn (tháng)",
    min_value=1,
    value=3,
    step=1
)

# Lãi suất
lai_suat = st.number_input(
    "Lãi suất (%/tháng)",
    min_value=0.0,
    value=1.0,
    step=0.1,
    format="%.2f"
)

# Hình thức nhận lãi
hinh_thuc = st.selectbox(
    "Hình thức nhận lãi",
    [
        "Cuối kỳ",
        "Hàng tháng",
        "Hàng quý"
    ]
)

st.divider()

# ==============================
# TÍNH TOÁN
# ==============================

if st.button("🧮 TÍNH LÃI", use_container_width=True):

    # Chuyển lãi suất từ % sang số thập phân
    lai_suat_thang = lai_suat / 100

    # Tổng tiền lãi
    tong_lai = so_tien * lai_suat_thang * ky_han

    # Tiền lãi định kỳ
    if hinh_thuc == "Cuối kỳ":

        lai_dinh_ky = tong_lai
        so_ky_nhan_lai = 1

    elif hinh_thuc == "Hàng tháng":

        lai_dinh_ky = so_tien * lai_suat_thang
        so_ky_nhan_lai = ky_han

    else:  # Hàng quý

        # Lãi suất 3 tháng
        lai_dinh_ky = so_tien * lai_suat_thang * 3
        so_ky_nhan_lai = ky_han // 3

        # Nếu kỳ hạn không đủ 3 tháng thì không có kỳ nhận lãi quý
        if so_ky_nhan_lai == 0:
            lai_dinh_ky = 0

    # Tổng số tiền gốc + lãi
    tong_tien = so_tien + tong_lai

    # ==============================
    # HIỂN THỊ KẾT QUẢ
    # ==============================

    st.success("✅ KẾT QUẢ TÍNH TOÁN")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "💵 Tiền lãi định kỳ",
            f"{lai_dinh_ky:,.0f} VNĐ"
        )

        st.metric(
            "📈 Tổng tiền lãi",
            f"{tong_lai:,.0f} VNĐ"
        )

    with col2:
        st.metric(
            "🏦 Tiền gốc",
            f"{so_tien:,.0f} VNĐ"
        )

        st.metric(
            "💰 Tổng gốc + lãi",
            f"{tong_tien:,.0f} VNĐ"
        )

    # ==============================
    # CHI TIẾT
    # ==============================

    st.divider()

    st.subheader("📋 Chi tiết")

    st.write(f"**Số tiền gửi:** {so_tien:,.0f} VNĐ")
    st.write(f"**Kỳ hạn:** {ky_han} tháng")
    st.write(f"**Lãi suất:** {lai_suat:.2f}%/tháng")
    st.write(f"**Hình thức nhận lãi:** {hinh_thuc}")

    if hinh_thuc == "Cuối kỳ":
        st.info(
            f"Khách hàng nhận toàn bộ tiền lãi "
            f"{tong_lai:,.0f} VNĐ khi đáo hạn."
        )

    elif hinh_thuc == "Hàng tháng":
        st.info(
            f"Mỗi tháng khách hàng nhận "
            f"{lai_dinh_ky:,.0f} VNĐ tiền lãi."
        )

    elif hinh_thuc == "Hàng quý":
        if ky_han >= 3:
            st.info(
                f"Mỗi quý khách hàng nhận "
                f"{lai_dinh_ky:,.0f} VNĐ tiền lãi."
            )
        else:
            st.warning(
                "Kỳ hạn dưới 3 tháng không đủ để nhận lãi theo quý."
            )
