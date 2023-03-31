

def min_and_max(numbers):
    #Find the minimum and maximum numbers in the list.
    if not numbers:
        return None, None
    min_num = max_num = numbers[0]
    
    for num in numbers:
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num
    return min_num, max_num


numbers = [1, 2, 55, 3, 87, 22, 65,-48]
min_num, max_num = min_and_max(numbers)
print(f"Minimum number is: {min_num}")
print(f"Maximum number is: {max_num}")
