from du_lieu import hoc_vien_list
from tien_ich import dinh_dang_tien


def thong_ke():
    print("\n--- THONG KE ---")
    print("Tong so hoc vien:", len(hoc_vien_list))

    tong_thu = 0
    for hv in hoc_vien_list:
        if hv["da_thanh_toan"]:
            tong_thu += hv["hoc_phi"]

    print("Tong hoc phi da thu:", dinh_dang_tien(tong_thu))

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

    for hv in hoc_vien_list:
        khoa = hv["khoa_hoc"]
        if khoa in dem_khoa:
            dem_khoa[khoa] += 1
        else:
            dem_khoa[khoa] = 1

    for khoa, so_luong in dem_khoa.items():
        print("-", khoa + ":", so_luong)

    chua_thanh_toan = 0
    for hv in hoc_vien_list:
        if hv["hoc_phi"] > 0 and not hv["da_thanh_toan"]:
            chua_thanh_toan += 1

    print("So hoc vien chua thanh toan:", chua_thanh_toan)
