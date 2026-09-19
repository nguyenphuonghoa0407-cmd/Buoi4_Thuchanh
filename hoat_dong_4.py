
print("- HOẠT ĐỘNG 4 -")


chuoi_so = "25"
so = int(chuoi_so)
print(so, type(so))

so_thuc = float("3.14")
print(so_thuc, type(so_thuc))

danh_sach = list((1, 2, 3))         
bo_ba = tuple([4, 5, 6])            
tap_hop = set([1, 2, 2, 3, 3, 3])    
tu_dien = dict([("a", 1), ("b", 2)]) 

print(danh_sach, bo_ba, tap_hop, tu_dien)


print("\nQuan sát lỗi ép kiểu:")
try:
    int("abc")
except ValueError as e:
    print("Lỗi int('abc'):", e)

try:
    int("3.14")
except ValueError as e:
    print("Lỗi int('3.14'):", e)


so_hop_le = int(float("3.14"))
print("Sau khi ép qua float rồi int:", so_hop_le)


ket_qua = 5 + 2.5                    
print(ket_qua, type(ket_qua))

ket_qua_2 = "Diem: " + str(8.5)     
print(ket_qua_2)