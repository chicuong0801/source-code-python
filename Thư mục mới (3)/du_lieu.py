import os

# Danh sach chua toan bo hoc vien
hoc_vien_list = []

# File du lieu nam cung thu muc voi cac file Python
TEN_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "hoc_vien.txt")

# Ma khoa hoc: (ten khoa hoc, don gia moi buoi)
BANG_GIA = {
    "1": ("Tieng Anh giao tiep", 80000),
    "2": ("IELTS co ban", 120000),
    "3": ("Tieng Nhat N5", 100000),
    "4": ("Tieng Trung co ban", 90000)
}
