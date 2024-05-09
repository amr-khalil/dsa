
def reverse_int(num):
    if num < 0:
        num = -num
        ans = "-" + str(num)[::-1]
    else:
        ans = str(num)[::-1]
    return int(ans)

if __name__ == "__main__":
    num = -90
    print(reverse_int(num))