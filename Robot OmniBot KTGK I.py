##Loi chao
print("Xin chao! Toi la Robot OmniBot, san long phuc vu quy khach!")
print("----------------------")
#Input nhiem vu
nhiem_vu = int(input("Vui long chon 1 nhiem vu: 1. Lau san nha   2. Tinh toan   3. Ship vat pham: "))
print("----------------------")
#Nhiem vu 1: Lau san nha
if nhiem_vu == 1:
    print("Robot da san sang lau san nha")
    dien_tich_lau = float(input("xin moi nhap dien tich lau (theo don vi dm²): "))
    thoi_gian_lau = dien_tich_lau / 5
    print("Robot se lau xong sau", thoi_gian_lau, "giay")
    print("----------------------")
    print("  Robot da lau xong")
    print("----------------------")
elif nhiem_vu == 2:
    so_nhat = float(input("Nhap so thu nhat: "))
    so_nhi = float(input("Nhap so thu hai: "))
    phep_tinh = int(input("Chon mot phep tinh: 1. Cong   2. Tru   3. Nhan   4. Chia: "))
    if phep_tinh == 1:
        dap_an = so_nhat + so_nhi
        print("Dap an la", dap_an)
    elif phep_tinh == 2:
        dap_an = so_nhat - so_nhi
        print("Dap an la", dap_an)
    elif phep_tinh == 3:
        dap_an = so_nhat * so_nhi
        print("Dap an la", dap_an)
    elif phep_tinh == 4:
        if so_nhi == 0:
            print("Trong toan hoc khong the chia cho 0!!")
        else:
            dap_an = so_nhat / so_nhi
            print("Dap an la", dap_an)
    else:
        print("Robot khong the nhan ra phep tinh")
    print("------------------")
elif nhiem_vu == 3:
    noi_gui = input("Nhap noi gui vat pham: ")
    noi_nhan = input("Nhap noi nhan vat pham: ")
    khoang_cach = float(input("Nhap khoang cach giua noi gui va noi nhan vat pham (theo don vi met): "))
    thoi_gian_cho = khoang_cach / 5
    print("Robot da ship vat pham tu", noi_gui, "den", noi_nhan, "sau", thoi_gian_cho, "giay")
    print("-----------------------")
else:
    print("---ERROR---")
    print("Robot khong hieu nhiem vu nay")