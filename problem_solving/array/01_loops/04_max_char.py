
def max_char(string):
    chars = {}
    for ch in string:
        if ch in chars:
            chars[ch] += 1 
        else:
            chars[ch] = 1
    return max(chars, key=chars.get)

def max_char2(string):
    chars = {}
    max_char = ""
    max_count = 0
    for ch in string:
        if ch in chars:
            chars[ch] += 1
        else:
            chars[ch] = 1
        if  max_count < chars[ch]:
            max_char = ch
            max_count = chars[ch]
        
    return max_char

if __name__ == "__main__":
    string = "Hello There!"
    print(max_char2(string))