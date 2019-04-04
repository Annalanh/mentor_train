import math
from random import *
#PART 1:

#1. tạo 2 list:
#tên các quận 
district_names = ["ST", "BĐ", "BTL", "CG", "ĐĐ", "HBT"]
#dân số các quận
population = [150300, 247100, 333300, 266800, 420900, 318000]

#2. tìm ra chỉ số của quận có số dân lớn nhất và nhỏ nhất
sorted_population = [150300, 247100, 333300, 266800, 420900, 318000]
sorted_population.sort()

index_of_max = population.index(sorted_population[5])
index_of_min = population.index(sorted_population[0])
print("Index of max population:"+ str(index_of_max))
print("Index of min population:"+ str(index_of_min))

#3. In ra tên của quận có dân số lớn nhất và ít nhất 
print("Name of max population district: "+ district_names[index_of_max])
print("Name of min population district: "+ district_names[index_of_min])

#4. tạo list chứa diện tích của từng quận theo thứ tự từ trên xuống. Tạo 1 list mới chứa mật độ dân cư ( Mật độ = Dân số/Diện tích)
areas = [117.43, 9.224, 43.35, 12.04, 9.96, 10.09]
density = []
for i in range(6):
    density_elem = population[i]/areas[i]
    density.append(density_elem)
print("Population density:")
print(density)

#PART 2:

#5. Khai bao 1 dictionary số lượng máy tính trong kho
computers = {"HP": 20, "DELL": 50, "MACBOOK": 12, "ASUS": 30}
print(computers)
#6 Hiện ra số lương Macbook trong kho
print("Number of Macbook: ")
print(computers["MACBOOK"])
#Không thay đổi khai báo, thêm TOSHIBA có sô lượng là 10
computers["TOSHIBA"] = 10
print(computers)
#8. Tạo 1 dictionary chứa bảng giá
computers_price = {"HP": 600, "DELL": 650, "MACBOOK": 12000, "ASUS": 400, "ACER": 350, "TOSHIBA": 600, "FUJITSU": 900, "ALIENWARE": 1000}
#9. Có một đơn hàng mua ASUS số lượng 5, tính tổng giá trị đơn hàng
bill = computers_price["MACBOOK"]*5
print("TOTAL PAYMENT: "+ str(bill))

#PART 3:
#11. Tạo game giống game vừa chơi 
points = 0
game_over = False
right_result = 0
right_choice = 0
showed_res = 0

while(game_over == False):
    num1 = randint(0, 100)
    num2 = randint(0,100)
    operator = randint(0,20)
    right_or_wrong = randint(0,20)

    if operator % 2 == 0:
        
        right_result = num1 + num2

        if(right_or_wrong % 5 == 0):
            showed_res = num1 + num2
        else: 
            showed_res = randint(-100, 100)
        print(str(num1)+" + "+str(num2)+" = "+str(showed_res))
        if(showed_res == right_result):
            right_choice = 1
        else:
            right_choice = 0

    else:
        right_result = num1 - num2

        if(right_or_wrong % 5 == 0):
            showed_res = num1 - num2
        else: 
            showed_res = randint(-100, 100)
        print(str(num1)+" - "+str(num2)+" = "+str(showed_res))
        if(showed_res == right_result):
            right_choice = 1
        else:
            right_choice = 0       
    choice = int(input("Your choice: 1. True 0. False "))
    
    if(choice == right_choice):
        points+=1
        print("Right")
        print("Your points = "+str(points))
    else:
        game_over = True
        print("Game over")
        print("Your points = "+str(points))
       
    

