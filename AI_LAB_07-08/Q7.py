from ortools.sat.python import cp_model

model = cp_model.CpModel()
n = 4
queens = [model.new_int_var(0, n-1, f'q{i}') for i in range(n)]

model.add_all_different(queens)

for i in range(n):
    for j in range(i+1, n):

        model.add(queens[i] - queens[j] != i - j)
        model.add(queens[i] - queens[j] != j - i)

solver = cp_model.CpSolver()
status = solver.solve(model)
if status in (cp_model.FEASIBLE, cp_model.OPTIMAL):
    for i in range(n):
        col = solver.value(queens[i])
        print(' '.join('Q' if c == col else '_' for c in range(n)))
