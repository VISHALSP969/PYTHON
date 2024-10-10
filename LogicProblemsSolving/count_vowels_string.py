print('Counts vowels in String')


def count_vowels(s):
    count = 0
    for ch in s:
        if ch in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            count += 1
    return count


s = input('Enter the string : ')
print(f'Number of vowels : {count_vowels(s)}')
