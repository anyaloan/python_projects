import json


class Conv_to_txt:
    def __init__(self, file):
        if file.endswith(".json"):
            self.file = file

    def read(self):
        with open(self.file, "r") as f:
            cont = json.load(f)
        return cont

    def write_to_txt(self, file1, name):
        cont = self.read()
        ml = ['A.', "B.", "C.", "D.", "E.", "F.", "G.", "H.", "I.", "J.", 'K.', 'L.', 'M.']
        with open(file1, "w") as f1:
            f1.write(name)
            questions = cont["Questions"]
            for ind, quest in enumerate(questions, start=1):
                f1.write('\n')
                f1.write(f'{ind}.')
                f1.write(quest['question'])
                print(f'{ind}.')
                print(quest['question'])

                for index, item in enumerate(quest["answers"]):
                    print(ml[index])
                    print(item)
                your_ans = input("The correct answer is: ")
                for i, ans in enumerate(quest['answers']):
                    if i == 0:
                        f1.write('\n')
                        if your_ans == "A":
                            f1.write("*")
                        f1.write("A.")
                    elif i == 1:
                        if your_ans == "B":
                            f1.write("*")
                        f1.write("B.")
                    elif i == 2:
                        if your_ans == "C":
                            f1.write("*")
                        f1.write("C.")
                    elif i == 3:
                        if your_ans == "D":
                            f1.write("*")
                        f1.write("D")
                    elif i == 4:
                        if your_ans == "E":
                            f1.write("*")
                        f1.write("E.")
                    f1.write(ans)
                    f1.write('\n')


# myconv = Conv_to_txt("quiz.json")
# myconv.write_to_txt("quiz.txt", "Anna Yayloyan")
