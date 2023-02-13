class soltype:
    none = 0
    only_one = 1
    infinite = 2


def add_rows(first, second, a, b):
    """
    first = a * first + b * second
    """
    assert len(first) == len(second), "row lengths must be the same"
    for i in range(len(first)):
        first[i] = a * first[i] + b * second[i]


def gauss_jordan_elimination(equations: list[list[int]]):
    """
    solve system of equations using Gauss-Jordan elimination method
    time complexity: O(n^3)
    """

    n = len(equations)

    # when an equation have a₁₂ = 0, this equation can be used to
    # get the value of x₂, hence it can't be at the 2nd row
    # to fix the i-th row we need to add any row with non-zero value
    non_zero = [-1] * n
    for i in range(n):
        eq = equations[i]
        if len(eq) != n + 1:
            return {"type": soltype.none}
        for j in range(len(eq) - 1):
            if eq[j] != 0:
                non_zero[j] = i

    for i in range(n):
        if equations[i][i] != 0:
            continue
        if non_zero[i] == -1:
            # either no solutions or infinite number of them
            continue
        add_rows(equations[i], equations[non_zero[i]], 1, 1)

    for i in range(n):
        for j in range(n):
            if i == j or equations[i][i] == 0:
                continue
            add_rows(equations[j], equations[i],
                     equations[i][i], -equations[j][i])

    values = [0.0] * n

    is_infinite = False
    for i in range(n):
        if equations[i][i] == 0 and equations[i][n] == 0:
            is_infinite = True
            continue
        if equations[i][i] == 0:
            return {"type": soltype.none}
        values[i] = equations[i][n] / equations[i][i]

    if is_infinite:
        return {"type": soltype.infinite}

    return {"type": soltype.only_one, "values": values}


# if __name__ == "__main__":
#     # # infinite number of solutions
#     # eqs = [
#     #     [1, 0, 0],
#     #     [2, 0, 0],
#     # ]
#     # print(gauss_jordan_elimination(eqs))
#     # # no solution exists
#     # eqs = [
#     #     [1, 0, 1],
#     #     [2, 0, 1],
#     # ]
#     # print(gauss_jordan_elimination(eqs))
#     # # no solution
#     # eqs = [
#     #     [1, 1, 1, 1],
#     #     [1, 1, 1, 2],
#     #     [0, 0, 0, 0],
#     # ]
#     # print(gauss_jordan_elimination(eqs))
#     # # no solution
#     # eqs = [
#     #     [1, 0, 0, 1],
#     #     [1, 0, 0, 2],
#     #     [0, 0, 0, 0],
#     # ]
#     # print(gauss_jordan_elimination(eqs))


def main():
    # =======================================================================
    # Writing subscripts into files
    # option 1:
    # \u0x208N for numbers, +, -, =, (, ) (N goes from 0 to F)
    # \u0x209N for letters
    # ex: print(u'H\u2082O\u2082')    >> H₂O₂
    # option 2:
    # using str.maketrans(), translate() methods
    # =======================================================================
    solution = gauss_jordan_elimination()
    file_solution = open("solution.txt", "w", encoding="utf-8")
    if solution["type"] == 1:  # one solution
        file_solution.write("There is one solution\n")
        for i, ans in enumerate(solution["values"]):
            string = 'X'+f"{i}"
            SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
            file_solution.write(
                f"{string.translate(SUB)}" + " = " + str(ans)+"\n")
    elif solution["type"] == 2:  # infinite solution
        file_solution.write("There is infinite solution\n")
    elif solution["type"] == 0:  # no solution
        file_solution.write("There is no solution\n")
    file_solution.close()
    # __file__ print path of of main.py which is the same as solution.txt
    print(__file__.replace("main.py", "solution.txt"))


if __name__ == "__main__":
    eqs = [
        [3, 4, 12],
        [6, 8, 24],
    ]
    ans = gauss_jordan_elimination(eqs)
    print(ans)
