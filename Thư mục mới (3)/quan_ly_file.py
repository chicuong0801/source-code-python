import os
from du_lieu import hoc_vien_list, TEN_FILE


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
