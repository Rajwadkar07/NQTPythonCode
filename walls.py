num_int = int(input("Number of interior walls : "))
area_int = 0
area_ext = 0
if num_int > 0:
    for i in range(num_int):
        area_int += float(input("Surface area of each interior wall: "))
num_ext = int(input("Number of exterior walls : "))
if num_ext > 0:
    for i in range(num_ext):
        area_ext += float(input("Surface area of each exterior wall: "))
cost_int = area_int * 18
cost_ext = area_ext * 12
print("Total cost:", cost_int+cost_ext)