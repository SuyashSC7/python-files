def minNumberOperations(target: list[int]) -> int:
    operations = target[0]
    for i in range(1, len(target)):
        if target[i] > target[i - 1]:
            operations += target[i] - target[i - 1]
    return operations

li=[3, 1, 5, 4, 2]
print(minNumberOperations(li))