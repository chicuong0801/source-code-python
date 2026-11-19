from du_lieu import hoc_vien_list
from tien_ich import nhap_chuoi
from hoc_vien import hien_thi_danh_sach


def tim_kiem():
    print("\n--- TIM KIEM HOC VIEN ---")
    print("1. Tim theo ma hoc vien")
    print("2. Tim theo ho ten")
    print("3. Tim theo so dien thoai")
    print("4. Tim theo khoa hoc")

    chon = input("Nhap lua chon: ").strip()

    if chon not in ("1", "2", "3", "4"):
        print("Lua chon khong hop le!")
        return

    tu_khoa = nhap_chuoi("Nhap tu khoa can tim: ").lower()
    ket_qua = []

    for hv in hoc_vien_list:
        if chon == "1" and tu_khoa in hv["ma"].lower():
            ket_qua.append(hv)
        elif chon == "2" and tu_khoa in hv["ten"].lower():
            ket_qua.append(hv)
        elif chon == "3" and tu_khoa in hv["sdt"].lower():
            ket_qua.append(hv)
        elif chon == "4" and tu_khoa in hv["khoa_hoc"].lower():
            ket_qua.append(hv)

    hien_thi_danh_sach(ket_qua)


def sap_xep():
    print("\n--- SAP XEP HOC VIEN ---")
    print("1. Theo ho ten")
    print("2. Theo hoc phi")
    print("3. Theo so buoi hoc")

    chon = input("Chon tieu chi sap xep: ").strip()

    if chon == "1":
        khoa = lambda hv: hv["ten"].lower()
    elif chon == "2":
        khoa = lambda hv: hv["hoc_phi"]
    elif chon == "3":
        khoa = lambda hv: hv["so_buoi"]
    else:
        print("Lua chon khong hop le!")
        return

    print("1. Sap xep tang dan")
    print("2. Sap xep giam dan")
    huong = input("Chon thu tu: ").strip()

    if huong not in ("1", "2"):
        print("Lua chon khong hop le!")
        return

    ds_sap_xep = sorted(
        hoc_vien_list,
        key=khoa,
        reverse=(huong == "2")
    )
    hien_thi_danh_sach(ds_sap_xep)
