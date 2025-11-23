from collections import deque


def is_palindrome(input_string: str) -> bool:
    # Нормалізація рядка
    normalized_str = ''.join(input_string.lower().split())
    deq = deque(normalized_str)

    # Порівняння символів з обох кінців черги
    while len(deq) > 1:
        if deq.pop() != deq.popleft():
            return False
    return True


print(is_palindrome("ротор"))  # Output: True
print(is_palindrome("1234554321"))  # Output: True
print(is_palindrome("This is not a palindrome"))  # Output: False
