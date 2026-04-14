def sum_of_two(nums: list, target: int) -> list:

    for el in nums:
        if type(el) is not int:
            raise TypeError('el is not int, but should be')
    if type (nums) is not list:
        raise TypeError('nums is not list, but should be')
    if type (target) is not int:
        raise TypeError('target is not int, but should be')
    
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i] 
        num_to_index[num] = i 
    return []

# ввод с клавиатуры
if __name__ == "__main__":
    nums_input = input("Введите массив чисел через пробел: ")
    nums = [int(x) for x in nums_input.split()]
    target = int(input("Введите target: "))
    result = sum_of_two(nums, target)
    
    if result:
        print(f"Индексы: {result}")
        print(f"{nums[result[0]]} + {nums[result[1]]} = {target}")
    else:
        print("Решение не найдено")    