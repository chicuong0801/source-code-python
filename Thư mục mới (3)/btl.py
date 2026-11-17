# DE TAI 13: QUAN LY TRUNG TAM NGOAI NGU
# Sinh vien: Hoang Chi Cuong
# Truong: Dai hoc Dai Nam
# Chuong trinh nay quan ly thong tin hoc vien, dang ky khoa hoc, tinh hoc phi,
# tim kiem, sap xep va luu doc du lieu tren file TXT.

import os

# Danh sach chua toan bo hoc vien duoc them vao trong chuong trinh
hoc_vien_list = []

# Duong dan den file du lieu nam cung thu muc voi chuong trinh
# dung de luu va doc thong tin hoc vien khi chay lai.
TEN_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "hoc_vien.txt")

# Bang gia cac khoa hoc, voi cau truc: ma khoa hoc -> (ten khoa hoc, don gia / buoi)
BANG_GIA = {
    "1": ("Tieng Anh giao tiep", 80000),
    "2": ("IELTS co ban", 120000),
    "3": ("Tieng Nhat N5", 100000),
    "4": ("Tieng Trung co ban", 90000)
}


# 1. Nhap chuoi va kiem tra du lieu
# Ham nay dung de nhap thong tin text, loai bo khoang trang thua va kiem tra
# khong de trong va khong chua ky tu | vi ky tu nay dung de phan tach du lieu trong file.
def nhap_chuoi(thong_bao):
    while True:
        gia_tri = input(thong_bao).strip()

        if gia_tri == "":
            print("Thong tin khong duoc de trong!")
        elif "|" in gia_tri:
            print("Khong duoc nhap ky tu | !")
        else:
            return gia_tri


# 2. Nhap so nguyen va kiem tra
# Ham nay yeu cau nguoi dung nhap mot so nguyen va khong cho phep gia tri am
# neu duoc truyen tham so toi_thieu.
def nhap_so_nguyen(thong_bao, toi_thieu=0):
    while True:
        try:
            so = int(input(thong_bao))

            if so < toi_thieu:
                print("Gia tri phai lon hon hoac bang", toi_thieu)
            else:
                return so

        except ValueError:
            print("Vui long nhap mot so nguyen hop le!")


# 3. Tim hoc vien theo ma
# Tim trong danh sach hoc_vien_list xem co hoc vien nao co ma trung khong.
def tim_hoc_vien(ma):
    for hv in hoc_vien_list:
        if hv["ma"] == ma.upper():
            return hv

    return None


# 4. Them hoc vien
# Thuc hien them mot hoc vien moi vao danh sach neu ma chua ton tai.
def them_hoc_vien():
    print("\n--- THEM HOC VIEN ---")

    ma = nhap_chuoi("Nhap ma hoc vien: ").upper()

    if tim_hoc_vien(ma) is not None:
        print("Ma hoc vien da ton tai!")
        return

    ten = nhap_chuoi("Nhap ho va ten: ")
    ngay_sinh = nhap_chuoi("Nhap ngay sinh (dd/mm/yyyy): ")
    sdt = nhap_chuoi("Nhap so dien thoai: ")

    # Dung dictionary de luu thong tin chi tiet cua hoc vien
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


# 5. Dinh dang tien
# Chuyen doi so tien thanh dinh dang co dau cham phan ngan va them don vi dong.
def dinh_dang_tien(so_tien):
    return format(so_tien, ",").replace(",", ".") + " dong"


# 6. Hien thi danh sach hoc vien
# Hien thi toan bo hoc vien theo mot bang de quan sat nhanh.
# Neu duoc truyen ds, se hien thi danh sach con thay vi danh sach goc.
def hien_thi_danh_sach(ds=None):
    if ds is None:
        ds = hoc_vien_list

    print("\n--- DANH SACH HOC VIEN ---")

    if len(ds) == 0:
        print("Danh sach hoc vien dang trong!")
        return

    print("-" * 120)

    # In tieu de cot va khoang cach de hien thi thong tin dung chuan.
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


# 7. Cap nhat hoc vien
# Cho phep sua thong tin ca nhan cua mot hoc vien da ton tai.
# Neu nguoi dung nhap Enter, se giu nguyen du lieu cu.
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

    # Chi cap nhat neu nguoi dung nhap gia tri moi va khong co ky tu |.
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


# 8. Xoa hoc vien
# Xoa hoc vien theo ma, sau khi can xac nhan phia nguoi dung.
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


# 9. Tim kiem hoc vien
# Tim kiem theo nhieu tieu chi khac nhau: ma, ten, sdt, khoa hoc.
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

    # Duyet tat ca hoc vien va bo sung vao ket_qua neu thoa man dieu kien loc.
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


# 10. Sap xep hoc vien
# Sap xep danh sach theo tieu chi nhap vao va theo thu tu tang/ giam dan.
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


# 11. Dang ky khoa hoc va tinh hoc phi
# Cho phep hoc vien chon khoa hoc, so buoi, tinh tong hoc phi va ghi nhan
# trang thai da thanh toan hay chua thanh toan.
def dang_ky_khoa_hoc():
    print("\n--- DANG KY KHOA HOC ---")

    ma = nhap_chuoi("Nhap ma hoc vien: ").upper()
    hv = tim_hoc_vien(ma)

    if hv is None:
        print("Khong tim thay hoc vien!")
        return

    print("\nCac khoa hoc hien co:")

    # Hien thi danh sach khoa hoc va don gia de nguoi dung chon.
    for ma_khoa, thong_tin in BANG_GIA.items():
        ten_khoa, don_gia = thong_tin

        print(ma_khoa + ".", ten_khoa, "-",
              dinh_dang_tien(don_gia) + "/buoi")

    chon = input("Chon khoa hoc: ").strip()

    if chon not in BANG_GIA:
        print("Khoa hoc khong hop le!")
        return

    so_buoi = nhap_so_nguyen("Nhap so buoi hoc: ", 1)

    ten_khoa, don_gia = BANG_GIA[chon]

    # Tinh tong hoc phi = so buoi * don gia / buoi.
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


# 12. Thong ke
# Tong hop thong tin nhan su va thu chi cua trung tam.
def thong_ke():
    print("\n--- THONG KE ---")

    print("Tong so hoc vien:", len(hoc_vien_list))

    tong_thu = 0

    # Tinh tong hoc phi da thu tu tat ca hoc vien da thanh toan.
    for hv in hoc_vien_list:
        if hv["da_thanh_toan"]:
            tong_thu += hv["hoc_phi"]

    print("Tong hoc phi da thu:", dinh_dang_tien(tong_thu))

    # Tim hoc vien da dong hoc phi cao nhat trong danh sach.
    ds_da_dong = [
        hv for hv in hoc_vien_list
        if hv["da_thanh_toan"] and hv["hoc_phi"] > 0
    ]

    if ds_da_dong:
        hv_cao_nhat = max(ds_da_dong, key=lambda hv: hv["hoc_phi"])

        print(
            "Hoc vien da dong hoc phi cao nhat:",
            hv_cao_nhat["ten"],
            "-",
            dinh_dang_tien(hv_cao_nhat["hoc_phi"])
        )
    else:
        print("Chua co hoc vien nao thanh toan hoc phi.")

    print("\nSo hoc vien theo tung khoa hoc:")

    dem_khoa = {}

    # Dem so luong hoc vien theo ten khoa hoc.
    for hv in hoc_vien_list:
        khoa = hv["khoa_hoc"]

        if khoa in dem_khoa:
            dem_khoa[khoa] += 1
        else:
            dem_khoa[khoa] = 1

    for khoa, so_luong in dem_khoa.items():
        print("-", khoa + ":", so_luong)

    chua_thanh_toan = 0

    # Dem so hoc vien da dang ky khoa hoc nhung chua thanh toan.
    for hv in hoc_vien_list:
        if hv["hoc_phi"] > 0 and not hv["da_thanh_toan"]:
            chua_thanh_toan += 1

    print("So hoc vien chua thanh toan:", chua_thanh_toan)


# 13. Luu du lieu vao file TXT
# Ghi danh sach hoc vien vao file theo dinh dang "|" de doc lai sau nay.
def luu_du_lieu():
    try:
        with open(TEN_FILE, "w", encoding="utf-8") as f:
            for hv in hoc_vien_list:
                dong = [
                    hv["ma"],
                    hv["ten"],
                    hv["ngay_sinh"],
                    hv["sdt"],
                    hv["khoa_hoc"],
                    str(hv["so_buoi"]),
                    str(hv["hoc_phi"]),
                    "1" if hv["da_thanh_toan"] else "0"
                ]

                f.write("|".join(dong) + "\n")

        print("Luu du lieu thanh cong!")

    except OSError as e:
        print("Khong the luu file:", e)


# 14. Doc du lieu tu file TXT
# Doc lai danh sach hoc vien tu file, kiem tra du lieu va loai bo dong khong hop le.
def doc_du_lieu():
    if not os.path.exists(TEN_FILE):
        print("Chua co file hoc_vien.txt!")
        return

    try:
        ds_moi = []

        with open(TEN_FILE, "r", encoding="utf-8") as f:
            for dong in f:
                dong = dong.strip()

                if not dong:
                    continue

                phan = dong.split("|")

                if len(phan) != 8:
                    print("Bo qua mot dong du lieu khong hop le!")
                    continue

                try:
                    # Chuyen doi du lieu text trong file thanh mot dictionary hoc vien.
                    hv = {
                        "ma": phan[0].strip().upper(),
                        "ten": phan[1].strip(),
                        "ngay_sinh": phan[2].strip(),
                        "sdt": phan[3].strip(),
                        "khoa_hoc": phan[4].strip(),
                        "so_buoi": int(phan[5]),
                        "hoc_phi": int(phan[6]),
                        "da_thanh_toan": phan[7].strip() == "1"
                    }

                    # Kiem tra du lieu co hop le hay khong truoc khi them vao danh sach.
                    if (not hv["ma"] or not hv["ten"] or not hv["sdt"]
                            or hv["so_buoi"] < 0 or hv["hoc_phi"] < 0):
                        print("Bo qua hoc vien co du lieu khong hop le!")
                        continue

                    if any(x["ma"] == hv["ma"] for x in ds_moi):
                        print("Bo qua ma hoc vien bi trung:", hv["ma"])
                        continue

                    ds_moi.append(hv)

                except ValueError:
                    print("Bo qua dong co du lieu so khong hop le!")

        hoc_vien_list.clear()
        hoc_vien_list.extend(ds_moi)

        print("Da doc", len(hoc_vien_list), "hoc vien tu file!")

    except (OSError, UnicodeError) as e:
        print("Khong the doc file:", e)


# 15. Hien thi menu
# In ra menu chuc nang chinh de nguoi dung lua chon thao tac.
def hien_thi_menu():
    print("\n" + "=" * 45)
    print("     QUAN LY TRUNG TAM NGOAI NGU")
    print("         Hoang Chi Cuong - Dai Nam")
    print("=" * 45)
    print("1. Them hoc vien")
    print("2. Hien thi danh sach")
    print("3. Cap nhat hoc vien")
    print("4. Xoa hoc vien")
    print("5. Tim kiem")
    print("6. Sap xep")
    print("7. Dang ky - tinh hoc phi")
    print("8. Thong ke")
    print("9. Luu du lieu")
    print("10. Doc du lieu")
    print("0. Thoat")
    print("=" * 45)


# 16. Ham chinh dieu khien chuong trinh
# Ham main la diem vao chuong trinh, doc du lieu ban dau va chay vong lap menu.
def main():
    doc_du_lieu()

    while True:
        hien_thi_menu()

        chon = input("Nhap lua chon: ").strip()

        if chon == "1":
            them_hoc_vien()

        elif chon == "2":
            hien_thi_danh_sach()

        elif chon == "3":
            cap_nhat_hoc_vien()

        elif chon == "4":
            xoa_hoc_vien()

        elif chon == "5":
            tim_kiem()

        elif chon == "6":
            sap_xep()

        elif chon == "7":
            dang_ky_khoa_hoc()

        elif chon == "8":
            thong_ke()

        elif chon == "9":
            luu_du_lieu()

        elif chon == "10":
            doc_du_lieu()

        elif chon == "0":
            luu_du_lieu()
            print("Cam on ban da su dung chuong trinh!")
            break

        else:
            print("Lua chon khong hop le! Vui long chon lai.")


# Goi ham main khi file duoc chay truc tiep.
if __name__ == "__main__":
    main()


# Bat dau chuong trinh
if __name__ == "__main__":
    main()