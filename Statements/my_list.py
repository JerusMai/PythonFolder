my_list = [0,1,2,3,4,5,6,7,8,9,10]
for num in my_list:
    #print(num)
    if num % 2 == 0:
        print(num)
    else:
        print(f'odd number:{num}')

list_sum = 0
for num in my_list:
     list_sum = list_sum + num
     print(list_sum)


