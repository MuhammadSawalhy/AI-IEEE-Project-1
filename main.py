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


def non_zero_cell(equations, r, col):
    i, n = r, len(equations)
    while equations[i][col] == 0:
        i += 1
        if i < n:
            continue
        i = r
        col += 1
        if col == n:
            return -1, -1
    return i, col


def reduced_row_echlon(equations):
    vars_order = []
    n = len(equations)

    r = 0
    col = 0
    while r < n and col < n:
        i, col = non_zero_cell(equations, r, col)

        if col == -1:
            break

        vars_order.append(col)

        # swap rows
        equations[i], equations[r] = equations[r], equations[i]

        for j in range(n):
            if j == r:
                continue
            add_rows(equations[j], equations[r],
                     equations[r][col], -equations[j][col])

        r += 1
        col += 1

    return vars_order


def gauss_jordan_elimination(equations):
    """
    solve system of equations using Gauss-Jordan elimination method
    time complexity: O(n^3)
    """

    n = len(equations)
    vars_order = reduced_row_echlon(equations)

    values = [0.0] * n

    if len(vars_order) != n:
        for i in range(len(vars_order), n):
            if equations[i][i] == 0 and equations[i][n] != 0:
                # 0 = -6?
                # -6/0 is -infinity which indicates no solution
                return {"type": soltype.none}
        return {"type": soltype.infinite}

    # all rows are good
    for i in range(n):
        values[i] = equations[i][n] / equations[i][i]

    return {"type": soltype.only_one, "values": values}


def main():
    if not examples():
        return

    print()
    try:
        ans = input(
            "Please follow instruction in user_manual.txt, type (y/Y) to continue: ")
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
