def examples():
    sub = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    eq = int(input("Please enter the number of equation to be solved : "))
    file = open("user_manual.txt", 'w', encoding="utf-8")
    file.write("This file is your catalogue to use this program.\n\n")
    file.write(
        "First, Store your equations in a text file named 'equations.txt'.\n")
    file.write(
        f"If you have {eq} equations, Your text file should be like this:\n")
    file.write(f"Number of equations: {eq}")
    for i in range(1, eq+1):
        file.write("\n")
        file.write(f"eq{i}: ")
        for j in range(1, eq+1):

            file.write(f"a{i}{j}x{j} ".translate(sub))
            if j < eq:
                file.write("+ ")
            else:
                file.write("= ")

        file.write(f"a{i}0".translate(sub))
    file.write(
        "\n\n##########################################################################################")
    file.close()
    print(__file__.replace("getting_info.py", "user_manual.txt"))


def getting_equations():
    file = open("equations.txt", 'r', encoding="utf-8")
    line1 = file.readline()
    no_eqs = int(line1.split(":")[1].strip())
    # print(no_lines, type(no_lines))
    lines = file.readlines()
    file.close()
    equations = []
    SUB = str.maketrans("₀₁₂₃₄₅₆₇₈₉", "0123456789")
    for line in lines:
        equation = []
        args = {}
        if line.startswith("eq"):
            data = line.split(":")[1].replace(" ", "")
            for i in data:
                if (i == '-'):
                    data = data.replace(i, " -")
                elif (i == '+' or i == '='):
                    data = data.replace(i, " ")
            data = data.split(" ")
            # print(data)
#               ['3x₂', '7x₃', '-1x₁', '0\n']
#               ['3x₃', '8x₁', '', '-1x₂', '', '', '-1\n']
#               ['', '-2x₁', '2x₃', '2']
            d = int(data[-1])
            factors = data[0:-1]
            for var in (factors):
                x = var.translate(SUB)
                if (x != ''):
                    equation.append(x)
                # print(equation)
#               ['3x2', '7x3', '-1x1']
#               ['3x3', '8x1', '-1x2']
#               ['-2x1', '2x3']
            # if (len(equation) == no_eqs):
            for value in equation:
                args[int(value.split("x")[1])] = int(value.split("x")[0])

            # solving problem of removed variables ex: 1x1 + 3x2 = 0
            if (len(equation) < no_eqs):
                for i in range(1, no_eqs+1):
                    if i not in args:
                        args[i] = 0
            # print(args)
    #        {2: 3, 3: 7, 1: -1}
    #        {3: 3, 1: 8, 2: -1}
    #        {1: -2, 3: 2, 2: 0}
    #         # order keyes in dictionary
    #         args = {k: args[k] for k in sorted(args)}
    #         # print(args)
    #     >> [[{1: -1, 2: 3, 3: 7}, 0], [{1: 8, 2: -1, 3: 3}, -1], [{1: -2, 2: 0, 3: 2}, 2]]
            equations.append([args, d])
            # print(equations)
# [[{2: 3, 3: 7, 1: -1}, 0], [{3: 3, 1: 8, 2: -1}, -1], [{1: -2, 3: 2, 2: 0}, 2]]
    # equations should be returned as 2D list
            returned_equations = []
            for list1 in equations:
                eqs = []
                for key, value in list1[0].items():
                    eqs.append(value)
                eqs.append(list1[1])
                returned_equations.append(eqs)
    # print(returned_equations)
    # [[3, 7, -1, 0], [3, 8, -1, -1], [-2, 2, 0, 2]]
    return returned_equations


if __name__ == "__main__":
    pass
