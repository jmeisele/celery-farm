from typing import Optional

from pydantic import PrivateAttr
from pyscipopt import Model, quicksum

from models.solver import ProblemData, SolverParameters
from optimizer.solver_interface import SolverInterface


class Solver(SolverInterface, ProblemData):
    # Set additional (private) attributes as needed
    _model: str = PrivateAttr()
    _solver_parameters: str = PrivateAttr()

    def __init__(self, **data):
        super().__init__(**data)
        self._model = None
        self._solver_parameters = None

    def set_solver_parameters(self, parameters: Optional[SolverParameters] = None):  # noqa: C901
        if parameters:
            self._solver_parameters = parameters
            if "setBoolParam" in self._solver_parameters:
                for key, value in self._solver_parameters["setBoolParam"].items():
                    self._model.setBoolParam(key, value)
            if "setIntParam" in self._solver_parameters:
                for key, value in self._solver_parameters["setIntParam"].items():
                    self._model.setIntParam(key, value)
            if "setRealParam" in self._solver_parameters:
                for key, value in self._solver_parameters["setRealParam"].items():
                    self._model.setRealParam(key, value)
            if "setCharParam" in self._solver_parameters:
                for key, value in self._solver_parameters["setCharParam"].items():
                    self._model.setCharParam(key, value)
            if "setStringParam" in self._solver_parameters:
                for key, value in self._solver_parameters["setStringParam"].items():
                    self._model.setStringParam(key, value)

    def build_model(self):
        self._model = Model("flp")
        # Define decision variables
        x, y = {}, {}
        for j in self.facilities:
            y[j] = self._model.addVar(vtype="B", name=f"y_{j}")
            for i in self.customers:
                x[i, j] = self._model.addVar(vtype="C", name=f"x_{i,j}")
        # Define constraint set
        for i in self.customers:
            self._model.addCons(
                quicksum(x[i, j] for j in self.facilities) == self.demand[i],
                f"Demand_{i}",
            )
        for j in self.facilities:
            self._model.addCons(
                quicksum(x[i, j] for i in self.customers) <= self.facility_capacity[j] * y[j],
                f"Capacity_{j}",
            )
        for (i, j) in x:
            self._model.addCons(x[i, j] <= self.demand[i] * y[j], f"Strong_{i,j}")
        # Define objective function
        self._model.setObjective(
            quicksum(self.facility_installation_cost[j] * y[j] for j in self.facilities)
            + quicksum(self.transportation_cost[i][j] * x[i, j] for i in self.customers for j in self.facilities),
            "minimize",
        )

    def solve_instance(self):
        self._model.optimize()

    def get_solution_status(self) -> dict:
        if self._model.getStatus() == "optimal":
            return {
                "status": self._model.getStatus(),
                "scip_parameters": self._solver_parameters,
                "objective_function_value": self._model.getObjVal(),
                "solution_time": self._model.getSolvingTime(),
                "gap": self._model.getGap(),
                "number_of_decision_vars": self._model.getNVars(),
                "number_of_constraints": self._model.getNConss(),
                "decision_variables": {var.name: self._model.getVal(var) for var in self._model.getVars()},
            }
        else:
            return {
                "status": self._model.getStatus(),
                "scip_parameters": self._solver_parameters,
            }
