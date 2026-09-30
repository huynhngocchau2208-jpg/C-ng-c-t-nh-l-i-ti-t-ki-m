import streamlit as st

st.set_page_config(
    page_title="Tính lãi tiền gửi tiết kiệm",
    page_icon=None,
    layout="centered"
)

st.title("TÍNH LÃI TIỀN GỬI TIẾT KIỆM")

# Nhập thông tin
so_tien_gui = st.number_input(
    "Số tiền gửi (VNĐ)",
    min_value=0.0,
    value=100000000.0,
    step=1000000.0,
    format="%.0f"
)

ky_han = st.number_input(
    "Kỳ hạn (tháng)",
    min_value=1,
    value=3,
    step=1
)

lai_suat = st.number_input(
    "Lãi suất (%/năm)",
    min_value=0.0,
    value=6.0,
    step=0.1,
    format="%.2f"
)

loai_lai = st.selectbox(
    "Phương thức tính lãi",
    [
        "Lãi đơn",
        "Lãi kép"
    ]
)

hinh_thuc_nhan_lai = st.selectbox(
    "Hình thức nhận lãi",
    [
        "Lãnh lãi theo tháng",
        "Lãnh lãi theo quý",
        "Lãnh lãi cuối kỳ"
    ]
)

# Nút tính
if st.button("TÍNH LÃI"):
    
    # Đổi lãi suất năm sang lãi suất tháng
    lai_suat_thang = lai_suat / 100 / 12

    # Tổng số tháng
    so_thang = ky_han

    # Tính lãi theo từng hình thức
    if hinh_thuc_nhan_lai == "Lãnh lãi theo tháng":
        so_ky_nhan_lai = so_thang
        so_thang_moi_ky = 1

    elif hinh_thuc_nhan_lai == "Lãnh lãi theo quý":
        so_ky_nhan_lai = so_thang // 3
        so_thang_moi_ky = 3

    else:
        so_ky_nhan_lai = 1
        so_thang_moi_ky = so_thang

    # Lãi đơn
    if loai_lai == "Lãi đơn":
        
        lai_moi_ky = (
            so_tien_gui
            * lai_suat_thang
            * so_thang_moi_ky
        )

        tong_tien_lai = (
            so_tien_gui
            * lai_suat_thang
            * so_thang
        )

        tong_tien = so_tien_gui + tong_tien_lai

    # Lãi kép
    else:
        
        # Lãi kép theo từng kỳ nhận lãi
        lai_suat_ky = (
            1 + lai_suat_thang
        ) ** so_thang_moi_ky - 1

        tien_cuoi_ky = (
            so_tien_gui
            * (1 + lai_suat_ky) ** so_ky_nhan_lai
        )

        tong_tien_lai = tien_cuoi_ky - so_tien_gui

        # Tiền lãi của kỳ đầu tiên
        lai_moi_ky = (
            so_tien_gui * lai_suat_ky
        )

        tong_tien = tien_cuoi_ky

    # Hiển thị kết quả
    st.subheader("KẾT QUẢ")

    st.write(
        "Tiền lãi định kỳ:",
        f"{lai_moi_ky:,.0f} VNĐ"
    )

    st.write(
        "Tổng tiền lãi:",
        f"{tong_tien_lai:,.0f} VNĐ"
    )

    st.write(
        "Tổng số tiền gốc và lãi:",
        f"{tong_tien:,.0f} VNĐ"
    )
