num = int(input("Enter the number of rows:"))
def pyramid(num):
    count = 1
    while count <= num:
        print((str(count) + " " ) * count)
        count += 1

pyramid(num)


