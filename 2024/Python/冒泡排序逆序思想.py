def length(v):
    i = 1
    while i * (i - 1) // 2 < v:
        i += 1
    return i
def create_string(length):
    goal_string = ""
    alpha = 'a'
    for _ in range(length):
        goal_string += alpha
        alpha = chr((ord(alpha) - ord('a') + 1) % 26 + ord('a'))
    return goal_string
def add(add_number, demo_string, length):
    list_demo_string = list(demo_string)
    alpha = 'a'
    index = 0
    while add_number > 0:
        # 由于index从0开始，所以插入位置应该对应demo_string的索引+1
        list_demo_string.insert(index + 1, alpha)
        index += 2
        alpha = chr((ord(alpha) - ord('a') + 1) % 26 + ord('a'))
        add_number -= 1
    return ''.join(sorted(list_demo_string,reverse=True))
V = int(input())
len_needed = length(V)
add_chars = len_needed * (len_needed - 1) // 2 - V
demo_string = create_string(len_needed - add_chars)
final_string = add(add_chars, demo_string, len_needed)
print(final_string)