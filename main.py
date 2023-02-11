def gauss_jordan_elimination():
    pass
    # return {"one": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]} #example


def main():
    # =======================================================================
    # gauss_jordan_elimination should return dictionary with keys as follows:
    # "one" >> if there is one solution  "one" : [1,2,3] where x1=1,x2=2,x3=3
    # "infinite" >> if there is infinite solution "infinite" :"There is infinite solution."
    # "none" >> if there is no solution   "none": "There is no solution."
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
    if "one" in solution:  # or if solution.get("one") is not None
        file_solution.write("There is one solution:\n")
        for i, ans in enumerate(solution["one"]):
            string = 'X'+f"{i}"
            SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
            file_solution.write(
                f"{string.translate(SUB)}" + " = " + str(ans)+"\n")
    elif "infinite" in solution:
        file_solution.write(solution["infinite"])
    elif "none" in solution:
        file_solution.write(solution["none"])
    file_solution.close()
    # __file__ print path of of main.py which is the same as solution.txt
    print(__file__.replace("main.py", "solution.txt"))


main()
