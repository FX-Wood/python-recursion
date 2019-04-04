def reverse_string(string):
    if len(string) <= 1:
        return string
    else:
        print
        return string[-1] + reverse_string(string[1:-1]) + string[0]