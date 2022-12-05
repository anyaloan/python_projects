def Thermoconverter(temp: int, form: str, conv_to: str):
    temp = int(temp)
    res = 0
    def k_to_c(k):
        c = k - 273.15
        return f"{c:.2f} C"
    def c_to_k(c):
        k = c + 273.15
        return f"{k:.2f} K"
    def k_to_f(k):
        f = 1.8*(k-273) + 32
        return f"{f:.2f} F"
    def f_to_k(f):
        k = (f - 32)/1.8 + 273
        return f"{k:.2f} K"
    def f_to_c(f):
        c = (f - 32) * 5 / 9
        return f"{c:.2f} C"
    def c_to_f(c):
        f = c * 9 / 5 + 32
        return f"{f:.2f} F"

    if form == "c":
        if conv_to == "k":
            res = c_to_k(temp)
        elif conv_to == "f":
            res = c_to_f(temp)
    elif form == "k":
        if conv_to == "c":
            res = k_to_c(temp)
        elif conv_to == "f":
            res = k_to_f(temp)
    elif form == "f":
        if conv_to == "k":
            res = f_to_k(temp)
        elif conv_to == "c":
            res = f_to_c(temp)
    else:
        print("No such format")
        return
    print(res)
    return res

if __name__ == "__main__":
    myform = ["k", "f", "c"]
    while True:
        try:
            temp, form = input("Enter the temperature you want to convert: ").lower().split()
            if temp.isnumeric:
                if form in myform:
                    break
        except Exception:
            pass
        print("Not valid format")
    conv_to = input("In which format do you want to convert? K/F/C").lower()
    if conv_to in myform:
        Thermoconverter(temp, form, conv_to)
