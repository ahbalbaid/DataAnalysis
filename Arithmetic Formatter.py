def arithmetic_arranger(problems,solve = False):
  top = []
  middle = []
  bottom = []
  Ansline = []
  if len(problems) > 5:
    return 'Error: Too many problems.'
  arranged =[]
  arranged_problems = ''
  for i in problems:
    A = i.split(' ')
    if A[1] != '+' and A[1] != '-':
      return 'Error: Operator must be \'+\' or \'-\'.'
    try:
      z= int(A[0])
      x= int(A[2])
    except:
      return 'Error: Numbers must only contain digits.'
    if len(A[0]) > 4 or len(A[2]) > 4 :
      return 'Error: Numbers cannot be more than four digits.'
    lenght = max(len(A[0]), len(A[2])) + 2
    lines = ''

    for i in range(lenght):
      lines += '-'

    if solve == True:
      if A[1] == '+':
        answer = int(A[0])+int(A[2])
        spaces = ''
        for i in range(lenght - len(str(answer))):
          spaces +=' '
        arranged.append(f'{A[0].rjust(lenght)}\n{A[1] + A[2].rjust(lenght- 1)}\n{lines}\n{spaces}{answer}')
        for i in arranged:
          arranged_problems += i
      elif A[1] == '-':
        answer = int(A[0]) - int(A[2])
        spaces = ''
        for i in range(lenght - len(str(answer))):
          spaces += ' '
        arranged.append(f'{A[0].rjust(lenght)}\n{A[1] + A[2].rjust(lenght- 1)}\n{lines}\n{spaces}{answer}')
        for i in arranged:
          arranged_problems += i

    else:
      arranged.append(f'{A[0].rjust(lenght)}\n{A[1] + A[2].rjust(lenght - 1)}\n{lines}')

  if solve == True:
    for i in arranged:
      top.append(i.split('\n')[0])
      middle.append(i.split('\n')[1])
      bottom.append(i.split('\n')[2])
      Ansline.append(i.split('\n')[3])

    arranged_problems = ''
    for i in range(len(top)):
      if i == len(top) - 1:
        arranged_problems += top[i]
      else:
        arranged_problems += top[i] + '    '
    arranged_problems += '\n'
    for i in range(len(middle)):
      if i == len(middle) - 1:
        arranged_problems += middle[i]
      else:
        arranged_problems += middle[i] + '    '
    arranged_problems += '\n'
    for i in range(len(bottom)):
      if i == len(bottom) - 1:
        arranged_problems += bottom[i]
      else:
        arranged_problems += bottom[i] + '    '
    arranged_problems += '\n'
    for i in range(len(Ansline)):
      if i == len(Ansline) - 1:
        arranged_problems += Ansline[i]
      else:
        arranged_problems += Ansline[i] + '    '
  else:
    for i in arranged:
      top.append(i.split('\n')[0])
      middle.append(i.split('\n')[1])
      bottom.append(i.split('\n')[2])

    arranged_problems = ''
    for i in range(len(top)):
      if i == len(top) - 1:
        arranged_problems += top[i]
      else:
        arranged_problems += top[i] + '    '
    arranged_problems += '\n'
    for i in range(len(middle)):
      if i == len(middle) - 1:
        arranged_problems += middle[i]
      else:
        arranged_problems += middle[i] + '    '
    arranged_problems += '\n'
    for i in range(len(bottom)):
      if i == len(bottom) - 1:
        arranged_problems += bottom[i]
      else:
        arranged_problems += bottom[i] + '    '





  return arranged_problems


answers = ['  3801      123\n'
        '-    2    +  49\n'
        '------    -----','  1         1\n'
        '+ 2    - 9380\n'
        '---    ------','    3      3801      45      123\n'
        '+ 855    -    2    + 43    +  49\n'
        '-----    ------    ----    -----','  11      3801      1      123         1\n'
        '+  4    - 2999    + 2    +  49    - 9380\n'
        '----    ------    ---    -----    ------','Error: Too many problems.','Error: Operator must be \'+\' or \'-\'.','Error: Numbers cannot be more than four digits.','Error: Numbers must only contain digits.','    3      988\n'
        '+ 855    +  40\n'
        '-----    -----\n'
        '  858     1028','   32         1      45      123      988\n'
        '- 698    - 3801    + 43    +  49    +  40\n'
        '-----    ------    ----    -----    -----\n'
        ' -666     -3800      88      172     1028']
problems = [['3801 - 2', '123 + 49'],['1 + 2', '1 - 9380'],['3 + 855', '3801 - 2', '45 + 43', '123 + 49'],['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380'],['44 + 815', '909 - 2', '45 + 43', '123 + 49','888 + 40', '653 + 87'],['3 / 855', '3801 - 2', '45 + 43', '123 + 49'],['24 + 85215', '3801 - 2', '45 + 43', '123 + 49'],['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49'],['3 + 855', '988 + 40'],['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40']]
'''
for i in range(len(problems)):
  if arithmetic_arranger(problems[i])==answers[i] :
    print(f'{i}- True')
  else:
    print(f'{i}- False\n{arithmetic_arranger(problems[i])} {answers[i]}')
'''
print(f'8- False\n{arithmetic_arranger(problems[8],True)}\n{answers[8]}')
print(f'9- False\n{arithmetic_arranger(problems[9],True)}\n{answers[9]}')
