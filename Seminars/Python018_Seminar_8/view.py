def get_name():
    with open('file.txt', 'r', encoding="utf-8") as f:
        for line in f.readlines()[:1]:
            return (line.rstrip('\n')) # пока не поняла, верно ли писать так
        

def get_number():
    with open('file.txt', 'r', encoding="utf-8") as f:
        for line in f.readlines()[1:2]:
            return (line.rstrip('\n'))

def what_to_do():
    with open('file.txt', 'r', encoding="utf-8") as f:
        for line in f.readlines()[2:]:
            return (line.rstrip('\n'))


def export_book(book: dict):
    with open('newfile.txt','a',encoding="utf-8") as newfile:
        newfile.writelines(f"{book}")
        newfile.writelines('\n')

            

# def print_dict(book: dict):
#     for k in book.items():
#         print(f"{k}")
#         for v in str(book[k]):
#             print(f"{str(v)}")