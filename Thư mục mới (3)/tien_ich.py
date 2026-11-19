# Cac ham dung chung trong chuong trinh

def nhap_chuoi(thong_bao):
    """Nhap chuoi, khong de trong va khong chua ky tu phan tach |."""
    while True:
        gia_tri = input(thong_bao).strip()

        if gia_tri == "":
            print("Thong tin khong duoc de trong!")
        elif "|" in gia_tri:
            print("Khong duoc nhap ky tu | !")
        else:
            return gia_tri


def nhap_so_nguyen(thong_bao, toi_thieu=0):
    """Nhap so nguyen va kiem tra gia tri toi thieu."""
    while True:
        try:
            so = int(input(thong_bao))

            if so < toi_thieu:
                print("Gia tri phai lon hon hoac bang", toi_thieu)
            else:
                return so

        except ValueError:
            print("Vui long nhap mot so nguyen hop le!")


def dinh_dang_tien(so_tien):
    """Dinh dang so tien theo dau cham phan tach hang nghin."""
    return format(so_tien, ",").replace(",", ".") + " dong"
