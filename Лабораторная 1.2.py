def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """

    list_b = list(brackets_row)

    if len(list_b) % 2 == 0:
        return True
    else:
        return False

    stack_ = []

    for i in range(0, len(list_b)):
        if list_b[i] == '(':
            stack_.append(list_b[i])
        if list_b[i] == ')' and len(stack_) != 0:
            stack_.pop()

    if len(stack_) == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
