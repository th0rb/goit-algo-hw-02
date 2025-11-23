def check_brackets(sequence: str):

    bracket_pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    stack = []

    for char in sequence:
        if char in bracket_pairs.values():
            # Якщо це відкриваюча дужка, додаємо її в стек
            stack.append(char)
        elif char in bracket_pairs.keys():
            # Якщо це закриваюча дужка - дивимось вершину стеку
            if stack == [] or bracket_pairs[char] != stack.pop():
                return "Несиметрично"
        
    
    # Якщо стек порожній після обробки, дужки симетричні
    return "Симетрично" if stack == [] else "Несиметрично"


test_strings = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}",
    "( 23 ( 2 - 3);",
    "( 11 }"
]

for test in test_strings:
    print(f"{test} : {check_brackets(test)}")
