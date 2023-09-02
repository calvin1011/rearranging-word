def rearrangeWord(word):
    char_list = list(word)
    n = len(char_list)

    # Find the rightmost character that can be replaced with a larger character
    for i in range(n - 2, -1, -1):
        if char_list[i] < char_list[i + 1]:
            break
    else:
        return "no answer"  # No rearrangement possible

    # Find the smallest character to the right of char_list[i] that is larger than char_list[i]
    for j in range(n - 1, i, -1):
        if char_list[j] > char_list[i]:
            char_list[i], char_list[j] = char_list[j], char_list[i]
            char_list[i + 1:] = reversed(char_list[i + 1:])  # Reverse the suffix
            return ''.join(char_list)

if __name__ == '__main__':
    # Sample case 1: 'pp'
    word1 = 'pp'
    result1 = rearrangeWord(word1)
    print(result1)  # This will print 'no answer'
    
    # Sample case 2: 'hefg'
    word2 = 'hefg'
    result2 = rearrangeWord(word2)
    print(result2)  # This will print 'hegf'
    
    # Additional case: 'xy'
    word3 = 'xy'
    result3 = rearrangeWord(word3)
    print(result3)  # This will print 'yx'
    
    # Add more sample cases here if needed
