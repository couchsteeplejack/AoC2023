from constraint import *

problem = Problem()

record = "#..###.#.."
code = [1,1,2]
vars = range(len(record))

problem.addVariables(vars, ['#', '.'])

# for i in [0,1]:
#     print(i, record[i])
#     problem.addConstraint(lambda a: a == record[i], [i])
problem.addConstraint(lambda a: a == record[0], [0])
problem.addConstraint(lambda a: a == record[1], [1])


# problem.addConstraint(lambda *args: args[0]==record[0], [0,1,2,3,4,5,6,7,8,9])

solutions = problem.getSolutions()

# print(len(list(solutions)))
print(list(solutions))
