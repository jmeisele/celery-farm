import React, { useState } from "react";
import Card from "../UI/Card";
import Button from "../UI/Button";
import "./AddSolver.css";

const AddSolver = () => {
  // States
  const [enteredUsername, setEnteredUsername] = useState("");
  const [enteredAge, setEnteredAge] = useState("");
  const [enteredCustomers, setEnteredCustomers] = useState("");
  const [enteredFacilities, setEnteredFacilities] = useState("");
  const [enteredTransportation, setTransportation] = useState("");
  const [enteredFacility, setFacility] = useState("");
  const [enteredFacilityCost, setFacilityCost] = useState("");
  const [enteredDemand, setDemand] = useState("");
  const [enteredBoolean, setBoolean] = useState(false);

  const addSolverHandler = (event) => {
    event.preventDefault();
    // Validate input
    if (enteredUsername.trim().length === 0 || enteredAge.trim().length === 0) {
      return;
    }
    // + in front of str will force to number data type
    if (+enteredAge < 1) {
      return;
    }
    console.log(enteredUsername, enteredAge);
    // Reset states
    setEnteredUsername("");
    setEnteredAge("");
  };

  const usernameChangeHandler = (event) => {
    setEnteredUsername(event.target.value);
  };

  const ageChangeHandler = (event) => {
    setEnteredAge(event.target.value);
  };

  // Changehandlers
  const customersChangeHandler = (event) => {
    setEnteredCustomers(event.target.value);
  };

  const facilitiesChangeHandler = (event) => {
    setEnteredFacilities(event.target.value);
  };

  const transportationChangeHandler = (event) => {
    setTransportation(event.target.value);
  };

  const facilityChangeHandler = (event) => {
    setFacility(event.target.value);
  };

  const facilitycostChangeHandler = (event) => {
    setFacilityCost(event.target.value);
  };

  const demandChangeHandler = (event) => {
    setDemand(event.target.value);
  };

  const booleanChangeHandler = (event) => {
    setBoolean(event.target.value);
  };

  // Placeholders
  const customersPlaceholder = ["c1", "c2", "c3", "c4", "c5"];
  const facilitiesPlaceholder = ["f1", "f2", "f3"];
  const transportationPlaceholder = {
    c1: { f1: 4, f2: 6, f3: 9 },
    c2: { f1: 5, f2: 4, f3: 7 },
    c3: { f1: 6, f2: 3, f3: 4 },
    c4: { f1: 8, f2: 5, f3: 3 },
    c5: { f1: 10, f2: 8, f3: 4 },
  };
  const facilityPlaceholder = { f1: 500, f2: 500, f3: 500 };
  const facilitycostPlaceholder = { f1: 1000, f2: 1000, f3: 1000 };
  const demandPlaceholder = { c1: 80, c2: 270, c3: 250, c4: 160, c5: 180 };
  const booleanPlaceholder = false;

  return (
    <Card className="input">
      <form onSubmit={addSolverHandler}>
        <h2>Problem Data</h2>
        {/* <input
          id="username"
          type="text"
          value={enteredUsername}
          onChange={usernameChangeHandler}
        /> */}
        <label htmlFor="customers">Customers</label>
        <input
          id="customers"
          type="text"
          value={enteredCustomers}
          onChange={customersChangeHandler}
          placeholder={customersPlaceholder}
        />
        <label htmlFor="facilities">Facilities</label>
        <input
          id="facilities"
          type="text"
          value={enteredFacilities}
          onChange={facilitiesChangeHandler}
          placeholder={facilitiesPlaceholder}
        />
        <label htmlFor="transportation_cost">Transportation Cost</label>
        <input
          id="transportation_cost"
          type="text"
          value={enteredTransportation}
          onChange={transportationChangeHandler}
          placeholder={transportationPlaceholder}
        />
        <label htmlFor="facility_capacity">Facility Capacity</label>
        <input
          id="facility_capacity"
          type="text"
          value={enteredFacility}
          onChange={facilityChangeHandler}
          placeholder={facilityPlaceholder}
        />
        <label htmlFor="facility_installation_cost">
          Facility Installation Cost
        </label>
        <input
          id="facility_installation_cost"
          type="text"
          value={enteredFacilityCost}
          onChange={facilitycostChangeHandler}
          placeholder={facilitycostPlaceholder}
        />
        <label htmlFor="demand">Demand</label>
        <input
          id="demand"
          type="text"
          value={enteredDemand}
          onChange={demandChangeHandler}
          placeholder={demandPlaceholder}
        />
        <h2>Solver Parameters</h2>
        <h5>Boolean</h5>
        <label htmlFor="boolean">True</label>
        <input
          id="boolean"
          type="radio"
          name="boolean"
          value={booleanPlaceholder}
          onChange={booleanChangeHandler}
        />
        <Button type="submit">Submit Solver Problem</Button>
      </form>
    </Card>
  );
};

export default AddSolver;
