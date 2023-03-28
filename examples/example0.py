def get_numbers():
    for i in range(4):  # i = 0    ; i = 0
        yield i         # return 0 ;return 1


a = get_numbers()
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())