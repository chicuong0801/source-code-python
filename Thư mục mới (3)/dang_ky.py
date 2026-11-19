from du_lieu import BANG_GIA
from hoc_vien import tim_hoc_vien
from tien_ich import nhap_chuoi, nhap_so_nguyen, dinh_dang_tien


def dang_ky_khoa_hoc():
    print("\n--- DANG KY KHOA HOC ---")

    ma = nhap_chuoi("Nhap ma hoc vien: ").upper()
    hv = tim_hoc_vien(ma)

    if hv is None:
        print("Khong tim thay hoc vien!")
        return

    print("\nCac khoa hoc hien co:")
    for ma_khoa, thong_tin in BANG_GIA.items():
        ten_khoa, don_gia = thong_tin
        print(ma_khoa + ".", ten_khoa, "-", dinh_dang_tien(don_gia) + "/buoi")

    chon = input("Chon khoa hoc: ").strip()

    if chon not in BANG_GIA:
        print("Khoa hoc khong hop le!")
        return

    so_buoi = nhap_so_nguyen("Nhap so buoi hoc: ", 1)
    ten_khoa, don_gia = BANG_GIA[chon]
    hoc_phi = so_buoi * don_gia

    hv["khoa_hoc"] = ten_khoa
    hv["so_buoi"] = so_buoi
    hv["hoc_phi"] = hoc_phi

    while True:
        thanh_toan = input(
            "Da thanh toan hoc phi chua? (y/n): "
        ).strip().lower()

        if thanh_toan == "y":
            hv["da_thanh_toan"] = True
            break
        elif thanh_toan == "n":
            hv["da_thanh_toan"] = False
            break
        else:
            print("Chi nhap y hoac n!")

    print("Dang ky khoa hoc thanh cong!")
    print("Khoa hoc:", ten_khoa)
    print("So buoi:", so_buoi)
    print("Hoc phi:", dinh_dang_tien(hoc_phi))
