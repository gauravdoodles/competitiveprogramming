def palindromic_string(input_string):

    max_length = 0

    # if input_string is "aba" than new_input_string become "a|b|a"
    new_input_string = ""
    output_string = ""

    # append each character + "|" in new_string for range(0, length-1)
    for i in input_string[: len(input_string) - 1]:
        new_input_string += i + "|"
    # append last character
    new_input_string += input_string[-1]

    # we will store the starting and ending of previous furthest ending palindromic substring
    l, r = 0, 0

    # length[i] shows the length of palindromic substring with center i
    length = [1 for i in range(len(new_input_string))]

    # for each character in new_string find corresponding palindromic string
    for i in range(len(new_input_string)):
        k = 1 if i > r else min(length[l + r - i] // 2, r - i + 1)
        while (
            i - k >= 0
            and i + k < len(new_input_string)
            and new_input_string[k + i] == new_input_string[i - k]
        ):
            k += 1

        length[i] = 2 * k - 1

        # does this string is ending after the previously explored end (that is r) ?
        # if yes the update the new r to the last index of this
        if i + k - 1 > r:
            l = i - k + 1
            r = i + k - 1

        # update max_length and start position
        if max_length < length[i]:
            max_length = length[i]
            start = i

    # create that string
    s = new_input_string[start - max_length // 2 : start + max_length // 2 + 1]
    for i in s:
        if i != "|":
            output_string += i

    return output_string






