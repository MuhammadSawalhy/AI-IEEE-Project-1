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
        assert len(eq) == n + 1, "row length must equals no. of unkowns + 1"
        for j in eq:
            if j != 0:
                non_zero[j] = i

    for i in range(n):
        if equations[i][i] != 0:
            continue
        if non_zero[i] == -1:
            # can't find a row with non-zero i-th element
            return {"type": soltype.none}
        add_rows(equations[i], equations[non_zero[i]], 1, 1)

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            add_rows(equations[j], equations[i], equations[i][i], -equations[j][i])

    values = [0.0] * n
    for i in range(n):
        if equations[i][i] == 0:
            return {"type": soltype.infinite}
        values[i] = equations[i][n] / equations[i][i]

    return {"type": soltype.only_one, "values": values}


if __name__ == "__main__":
    eqs = [
        [1, 1, 1],
        [0, 1, 1],
    ]
    ans = gauss_jordan_elimination(eqs)
    print(ans)
