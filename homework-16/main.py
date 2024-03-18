def is_palindrome(numbers: list[int]) -> bool:
    a = ''
    b = ''

    for number in numbers:
        a += str(number)

    for number in range(len(numbers) - 1, -1, -1):
        b += str(numbers[number])

    print(a, b)
    return a == b


print(is_palindrome([1, 2, 1]))


def reverse(sentence: str) -> str:
    result = ''
    word = ''

    for i in range(len(sentence) - 1, -1, -1):
        if sentence[i] == ' ' or i == 0:
            if i == 0:
                word += sentence[i]

            for j in range(len(word) - 1, -1, -1):
                result += word[j]
            result += ' '

            word = ''

        else:
            word += sentence[i]

    return result


print(reverse('hello world'))
