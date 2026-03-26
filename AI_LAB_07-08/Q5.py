from ortools.sat.python import cp_model

model = cp_model.CpModel()

A = model.new_int_var(0, 3, 'A')
B = model.new_int_var(0, 3, 'B')
C = model.new_int_var(0, 3, 'C')

model.add(A != B)
model.add(B != C)
model.add(A + B <= 4)

class SolutionPrinter(cp_model.CpSolverSolutionCallback):
    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.variables = variables

    def on_solution_callback(self):
        vals = {str(v): self.value(v) for v in self.variables}
        print(vals)

solver = cp_model.CpSolver()
callback = SolutionPrinter([A, B, C])
solver.parameters.enumerate_all_solutions = True
solver.solve(model, callback)
