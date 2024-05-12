def is_palindrome(num_str):
    return num_str == num_str[::-1]
for i in range(10, 1000):
    if all(is_palindrome(str(x)) for x in (i, i**2, i**3)):
        print(f"{i}, {i**2}, {i**3}")