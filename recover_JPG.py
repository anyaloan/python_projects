def recover_as(file1, file2):
    with open(file1, "rb") as f:
        with open(file2, "wb") as f1:
            content = f.read(3072)
            f1.write(content)
            f1.seek(3072)
            content = f.read(1024)
            content = content[::-1]
            f1.write(content)
            counter = 0
            for i in range(4096, 103283, 1024):
                f.seek(i)
                content = f.read(1024)
                counter += 1
                if counter == 3:
                    content = content[::-1]
                    counter = 0
                f1.write(content)


def recover(file1):
    with open(file1, "rb+") as f:
        cont1 = f.read(3072)
        f.seek(3072)
        cont2 = f.read(1024)
        cont2 = cont2[::-1]
        cont_list = [cont1, cont2]
        counter = 0
        for i in range(4096, 103283, 1024):
            f.seek(i)
            content = f.read(1024)
            counter += 1
            if counter == 3:
                content = content[::-1]
                counter = 0
            cont_list.append(content)
        f.seek(0)
        for el in cont_list:
            f.write(el)

# recover("damaged.jpg")
# recover_as("damaged.jpg", "new.jpg")
