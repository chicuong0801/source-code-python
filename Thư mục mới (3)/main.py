from hoc_vien import (
    them_hoc_vien,
    hien_thi_danh_sach,
    cap_nhat_hoc_vien,
    xoa_hoc_vien
)
from tim_kiem_sap_xep import tim_kiem, sap_xep
from dang_ky import dang_ky_khoa_hoc
from thong_ke import thong_ke
from quan_ly_file import luu_du_lieu, doc_du_lieu


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


if __name__ == "__main__":
    main()
