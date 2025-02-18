total=int(input())
book,add_book=0,0
for _ in range(9):
    book=int(input())
    add_book+=book
print(total-add_book)