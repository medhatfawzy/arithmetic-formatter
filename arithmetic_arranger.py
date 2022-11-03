def arithmetic_arranger(problems, get_results=False):
#   if len(problems) > 5: 
#     return "Error: Too many problems."

  parser_result = problems_parser(problems)
  # the function only return a string when there's an error 
  # in such case we want to return that error string
  if type(parser_result) is type(str()):
    return parser_result
    
  first_operands, operators, second_operands = parser_result

  # could be improved
  results = []
  if get_results:
    results = calc_results(first_operands, operators, second_operands)

  first_operands_string, second_operands_string, dashes_string, results_string = stringifier(first_operands, operators, second_operands, results)

  arranged_problems = f"{first_operands_string}\n{second_operands_string}\n{dashes_string}"
  return arranged_problems

def problems_parser(problems):
  first_operands = []
  operators = []
  second_operands = []
  
  for problem in problems:
    if not any(operator in problem for operator in ('+', '-', '*', '/')):  
        return "Error: Operator must be '+', '-', '*' or '/'."

    for operator in ('+', '-', '*', '/'):
        operator_index = problem.find(operator)
        if operator_index != -1: 
            break

    try:  
      first_operand, second_operand = problem.split(problem[operator_index])
    except:
      return "Error: More than three operands in the problem"

    first_operand = first_operand.strip()
    second_operand = second_operand.strip()
    # if len(first_operand) > 4 or len(second_operand) > 4:
    #   return "Error: Numbers cannot be more than four digits."
    
    try:
      first_operand = int(first_operand)
      second_operand = int(second_operand)
    except:
      return "Error: Numbers must only contain digits."
      
    first_operands.append(first_operand)
    operators.append(problem[operator_index])
    second_operands.append(second_operand)

  return first_operands, operators, second_operands

def calc_results(first_operands, operators, second_operands):
  results = []
  for i in range(len(first_operands)):
    results.append(eval(f"{first_operands[i]}{operators[i]}{second_operands[i]}"))
  return results

def stringifier(first_operands, operators, second_operands, results):
  first_operands_string = ""
  second_operands_string = ""
  dashes_string = ""
  results = ""
  for i in range(len(first_operands)):
    first_operand = str(first_operands[i])
    second_operand = str(second_operands[i])
    
    first_second = len(first_operand) - len(second_operand)
    second_first = len(second_operand) - len(first_operand)
    # we add 2 for the first operand because of the operator 
    # and the space between it and the second operatand
    if first_second >= second_first:
      first_operands_string += f"{' '*2}{first_operand}"
      
      space_before_second = ' ' * (first_second + 1)
      second_operands_string += f"{operators[i]}{space_before_second}{second_operand}"
      
      dashes = '-' * (len(first_operand) + 2)
      dashes_string += f"{dashes}"
    else:
      space_before_first = ' ' * (second_first + 2)
      first_operands_string += f"{space_before_first}{first_operand}"
      
      second_operands_string += f"{operators[i]} {second_operand}"
      
      dashes = '-' * (len(second_operand) + 2)
      dashes_string += f"{dashes}"
    
    if i != len(first_operands) - 1:
      first_operands_string += "    "
      second_operands_string += "    "
      dashes_string += "    "
      # results += "    "
  return first_operands_string, second_operands_string, dashes_string, results