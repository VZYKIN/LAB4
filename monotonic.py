#Лабораторная 4
Print('Это функция,которая принимает список nums и возвращает значение True типа bool, если список монотонный, и bool False, если список не монотонный.')
def is_monotonic(nums):
    d = len(nums)
    b = True
    t = True
#First c
    for i in range (0, d - 1):
        if nums[i] - nums[i + 1] == 0:
            continue
        elif nums[i] - nums[i + 1] == -1:
            t = True
            break
        elif nums[i] - nums[i + 1] == 1:
            t = False
            break
        else:
            return False
#Second c

    for i in range(0, d - 1):
        if t:
            if nums[i] - nums[i + 1] <= 0:
                continue
            else:
                b = False
        else:
            if nums[i] - nums[i + 1] >= 0:
                continue
            else:
                b = False

    return b
#Вывод функции
