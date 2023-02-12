# def examples():
#     sub = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
#     eq = int(input("Please enter the number of equation to be solved : "))
#     file = open("user_manual.txt", 'w', encoding="utf-8")
#     file.write("This file is your catalogue to use this program.\n\n")
#     file.write(
#         "First, Store your equations in a text file named 'equations.txt'.\n")
#     file.write(
#         f"If you have {eq} equations, Your text file should be like this:\n")
#     file.write(f"Number of equations: {eq}")
#     for i in range(1, eq+1):
#         file.write("\n")
#         file.write(f"eq{i}: ")
#         for j in range(1, eq+1):

#             file.write(f"a{i}{j}x{j} ".translate(sub))
#             if j < eq:
#                 file.write("+ ")
#             else:
#                 file.write("= ")

#         file.write(f"a{i}0".translate(sub))
#     file.write(
#         "\n\n##########################################################################################")
#     file.close()
#     print(__file__.replace("getting_info.py", "user_manual.txt"))


# def getting_equations():
#     # Number of equations: 3
#     # eq₁: 1x₁ + 3x₂ - 7x₃ = 0
#     # eq₂: 8x₁ - 1x₂ + 3x₃ = -1
#     # eq₃: -2x₁ + 10x₂ + 2x₃ = 2
#     file = open("equations.txt", 'r', encoding="utf-8")
#     lines = file.readlines()
#     file.close()
#     equations = []
#     for line in lines:
#         if line.startswith("eq"):
#             data=line.split(":")[1].strip().split(" ")
#             data = [i for i in data if i != "+" and i != "-" and i != "="]
#             for list_ in data:
#                 # [['-2', '₁₁'], ['10', '₂₁'], ['2', '₃'], ['2']]
#                 if(len(list_)-1 == len(data)):
#                     equations[u'{list_[1]}']=int(list_[0])
#                 else:
#                     for in range():
#                         equations[u'{list_[1]}']=list_[0]
#             #     for i in list_:
#             #        #['1x₁', '+', '3x₂', '-', '7x₃', '=', '0']
#             #        #  clean this to get {1:1,2:3,3:-7}
#     return data
#     #         equations.append(data)
#     # return equations


# if __name__ == "__main__":
#     # examples()
#     # print(getting_equations())
#     print(getting_equations())
