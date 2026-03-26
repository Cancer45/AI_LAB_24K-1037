from ortools.sat.python import cp_model

model = cp_model.CpModel()

A = model.new_int_var(0, 3, 'A')
B = model.new_int_var(0, 3, 'B')
C = model.new_int_var(0, 3, 'C')

model.add(A != B)
model.add(B != C)
model.add(A + B <= 4)

solver = cp_model.CpSolver()
status = solver.solve(model)

if status in (cp_model.FEASIBLE, cp_model.OPTIMAL):
    print(f"A={solver.value(A)}, B={solver.value(B)}, C={solver.value(C)}")
