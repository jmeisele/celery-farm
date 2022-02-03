import uuid
from typing import Dict, List, Optional

from pydantic import BaseModel, Field, constr


class ProblemData(BaseModel):
    """
    Definition of a problem instance with sets and parameters requiered to model the problem.
    Example: facility location problem, see https://scipbook.readthedocs.io/en/latest/flp.html
    """

    # id: str = Field(default_factory=uuid.uuid4, alias="_id")
    customers: List[str]
    facilities: List[str]
    transportation_cost: Dict[str, Dict[str, int]]
    facility_capacity: Dict[str, int]
    facility_installation_cost: Dict[str, int]
    demand: Dict[str, int]

    class Config:
        schema_extra = {
            "example": {
                # "id": "00010203-0405-0607-0809-0a0b0c0d0e0f",
                "customers": ["c1", "c2", "c3", "c4", "c5"],
                "facilities": ["f1", "f2", "f3"],
                "transportation_cost": {
                    "c1": {"f1": 4, "f2": 6, "f3": 9},
                    "c2": {"f1": 5, "f2": 4, "f3": 7},
                    "c3": {"f1": 6, "f2": 3, "f3": 4},
                    "c4": {"f1": 8, "f2": 5, "f3": 3},
                    "c5": {"f1": 10, "f2": 8, "f3": 4},
                },
                "facility_capacity": {"f1": 500, "f2": 500, "f3": 500},
                "facility_installation_cost": {"f1": 1000, "f2": 1000, "f3": 1000},
                "demand": {"c1": 80, "c2": 270, "c3": 250, "c4": 160, "c5": 180},
            }
        }


# give some example data for sets and parameter to show in openapi doc
def get_schema_extra() -> ProblemData:
    return {
        "customers": ["c1", "c2", "c3", "c4", "c5"],
        "facilities": ["f1", "f2", "f3"],
        "transportation_cost": {
            "c1": {"f1": 4, "f2": 6, "f3": 9},
            "c2": {"f1": 5, "f2": 4, "f3": 7},
            "c3": {"f1": 6, "f2": 3, "f3": 4},
            "c4": {"f1": 8, "f2": 5, "f3": 3},
            "c5": {"f1": 10, "f2": 8, "f3": 4},
        },
        "facility_capacity": {"f1": 500, "f2": 500, "f3": 500},
        "facility_installation_cost": {"f1": 1000, "f2": 1000, "f3": 1000},
        "demand": {"c1": 80, "c2": 270, "c3": 250, "c4": 160, "c5": 180},
    }


class SolverParameters(BaseModel):
    """
    Definition of parameters to control the behavior of the solver (e.g. run time, gap, etc.).
    Example with SCIP solver parameters which can be found at https://www.scipopt.org/doc/html/PARAMETERS.php
    """

    setBoolParam: Optional[Dict[str, bool]] = None
    setIntParam: Optional[Dict[str, int]] = None
    setRealParam: Optional[Dict[str, float]] = None
    setCharParam: Optional[Dict[str, constr(min_length=1, max_length=1)]] = None
    setStringParam: Optional[Dict[str, str]] = None

    # example for solver settings to show in openapi doc
    class Config:
        schema_extra = {
            "example": {
                "setBoolParam": {
                    "branching/preferbinary": False,
                    "branching/delaypscostupdate": True,
                },
                "setIntParam": {"conflict/minmaxvars": 0, "conflict/maxlploops": 2},
                "setRealParam": {"branching/scorefac": 0.167, "branching/clamp": 0.2},
                "setCharParam": {
                    "branching/scorefunc": "p",
                    "branching/lpgainnormalize": "s",
                },
                "setStringParam": {
                    "visual/bakfilename": "-",
                    "heuristics/undercover/fixingalts": "li",
                },
            }
        }

class SCIPInstance(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    problem_data: ProblemData
    solver_params: SolverParameters
