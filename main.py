from getting_info import getting_equations, examples


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


def fix_row(equations, i):
    """
    when i-th row in equations contains 0 in the main diagonal (equations[i][i])
    this function will try to fix this row by using any other none zero
    """
    pass


def gauss_jordan_elimination(equations):
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

    for i in range(n): # for each number in the diagonal
        if equations[i][i] == 0:
            continue
            fix_row(equations, i)
        for j in range(n):
            if i == j:
                continue
            add_rows(equations[j], equations[i],
                     equations[i][i], -equations[j][i])

    # if there exists a solution, we will have the main diagonal with no zeros

    values = [0.0] * n

    is_infinite = False
    for i in range(n):
        if equations[i][i] == 0 and equations[i][n] == 0:
            # 0/0 can be any value using limit (it is indeterminate)
            is_infinite = True
            continue
        if equations[i][i] == 0:
            # 0 = -6?
            # -6/0 is -infinity which indicates no solution
            return {"type": soltype.none}
        values[i] = equations[i][n] / equations[i][i]

    if is_infinite:
        return {"type": soltype.infinite}

    return {"type": soltype.only_one, "values": values}


def main():
    if not examples():
        return

    print()
    try:
        ans = input("Please follow instruction in user_manual.txt, type (y/Y) to continue: ")
        if ans.strip().lower() != 'y':
            return
    except:
        return

    equations = getting_equations()
    if not equations:
        print("Solution file is not generated")
        return

    solution = gauss_jordan_elimination(equations)
    filepath = __file__.replace("main.py", "solution.txt")
    file = open(filepath, "w", encoding="utf-8")
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

    if solution["type"] == soltype.none:
        file.write("There is no solution\n")
    elif solution["type"] == soltype.infinite:
        file.write("There is infinite solution\n")
    elif solution["type"] == soltype.only_one:
        assert isinstance(solution["values"], list)
        file.write("There is one solution:\n\n")
        for i, ans in enumerate(solution["values"]):
            string = 'x' + str(i + 1)
            file.write(f"{string.translate(SUB)}" + " = " + str(ans)+"\n")

    file.close()
    print("Solution file in generated at:")
    print(filepath)


if __name__ == "__main__":
    main()

