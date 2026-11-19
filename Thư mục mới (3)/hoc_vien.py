from du_lieu import hoc_vien_list
from tien_ich import nhap_chuoi


def tim_hoc_vien(ma):
    """Tim hoc vien theo ma hoc vien."""
    for hv in hoc_vien_list:
        if hv["ma"] == ma.upper():
            return hv
    return None


def them_hoc_vien():
    print("\n--- THEM HOC VIEN ---")

    ma = nhap_chuoi("Nhap ma hoc vien: ").upper()

    if tim_hoc_vien(ma) is not None:
        print("Ma hoc vien da ton tai!")
        return

    ten = nhap_chuoi("Nhap ho va ten: ")
    ngay_sinh = nhap_chuoi("Nhap ngay sinh (dd/mm/yyyy): ")
    sdt = nhap_chuoi("Nhap so dien thoai: ")

    hv = {
        "ma": ma,
        "ten": ten,
        "ngay_sinh": ngay_sinh,
        "sdt": sdt,
        "khoa_hoc": "Chua dang ky",
        "so_buoi": 0,
        "hoc_phi": 0,
        "da_thanh_toan": False
    }

    hoc_vien_list.append(hv)
    print("Them hoc vien thanh cong!")


def hien_thi_danh_sach(ds=None):
    if ds is None:
        ds = hoc_vien_list

    print("\n--- DANH SACH HOC VIEN ---")

    if len(ds) == 0:
        print("Danh sach hoc vien dang trong!")
        return

    print("-" * 120)
    print("{:<10} {:<22} {:<13} {:<13} {:<21} {:>8} {:>15} {:<12}".format(
        "Ma HV", "Ho va ten", "Ngay sinh", "SDT",
        "Khoa hoc", "So buoi", "Hoc phi", "Thanh toan"
    ))
    print("-" * 120)

    for hv in ds:
        if hv["da_thanh_toan"]:
            trang_thai = "Da dong"
        else:
            trang_thai = "Chua dong"

        print("{:<10} {:<22} {:<13} {:<13} {:<21} {:>8} {:>15,} {:<12}".format(
            hv["ma"],
            hv["ten"][:21],
            hv["ngay_sinh"],
            hv["sdt"],
            hv["khoa_hoc"][:20],
            hv["so_buoi"],
            hv["hoc_phi"],
            trang_thai
        ))

    print("-" * 120)


def cap_nhat_hoc_vien():
    print("\n--- CAP NHAT HOC VIEN ---")

    ma = nhap_chuoi("Nhap ma hoc vien can cap nhat: ").upper()
    hv = tim_hoc_vien(ma)

    if hv is None:
        print("Khong tim thay hoc vien!")
        return

    print("Bam Enter neu muon giu nguyen thong tin cu.")

    ten = input("Ho va ten [" + hv["ten"] + "]: ").strip()
    ngay_sinh = input("Ngay sinh [" + hv["ngay_sinh"] + "]: ").strip()
    sdt = input("So dien thoai [" + hv["sdt"] + "]: ").strip()

    if ten:
        if "|" not in ten:
            hv["ten"] = ten
        else:
            print("Ten khong hop le, giu nguyen ten cu.")

    if ngay_sinh:
        if "|" not in ngay_sinh:
            hv["ngay_sinh"] = ngay_sinh
        else:
            print("Ngay sinh khong hop le, giu nguyen gia tri cu.")

    if sdt:
        if "|" not in sdt:
            hv["sdt"] = sdt
        else:
            print("So dien thoai khong hop le, giu nguyen gia tri cu.")

    print("Cap nhat thanh cong!")


def xoa_hoc_vien():
    print("\n--- XOA HOC VIEN ---")

    ma = nhap_chuoi("Nhap ma hoc vien can xoa: ").upper()
    hv = tim_hoc_vien(ma)

    if hv is None:
        print("Khong tim thay hoc vien!")
        return

    xac_nhan = input("Ban co chac chan muon xoa? (y/n): ").lower()

    if xac_nhan == "y":
        hoc_vien_list.remove(hv)
        print("Da xoa hoc vien!")
    else:
        print("Da huy thao tac!")
