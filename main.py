from arithmetic_arranger import arithmetic_arranger

# tests = [
#             ['3801 - 2', '123 + 49'],
#             ['1 + 2', '1 - 9380'],
#             ['3 + 855', '3801 - 2', '45 + 43', '123 + 49'],
#             ['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380'],
#             ['44 + 815', '909 - 2', '45 + 43', '123 + 49', '888 + 40', '653 + 87'],
#             ['3 / 855', '3801 - 2', '45 + 43', '123 + 49'],
#             ['24 + 85215', '3801 - 2', '45 + 43', '123 + 49'],
#             ['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49'],
#             (['3 + 855', '988 + 40'], True),
#             (['32 - 698', '1 - 3801', '45 + 43', '9999 * 9999', '988 + 40'], True)
# ]
if __name__ == "__main__":
    while True:
        operations = input("""
Input the operations in the following format:
32 - 698, 1 - 3801, 45 + 43, 9999 * 9999, 988 + 40
To quit type 'q': """)

        if operations == 'q':
            break

        operations = operations.strip().replace("'","").split(',')
        cacl_results = input("""
Do you want to calculate the results? 
type 'y' if yes or 'n' if no: """)

        if cacl_results.__contains__('y'):
            cacl_results = True
        else: cacl_results = False
        print(arithmetic_arranger(operations, cacl_results), "\n")
