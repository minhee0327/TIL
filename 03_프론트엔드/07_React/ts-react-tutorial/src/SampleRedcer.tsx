import React, { useReducer } from "react";
import { useSampleState, useSampleDispatch } from "./SampleContext";

function SampleReducer() {
  const state = useSampleState();
  const dispatch = useSampleDispatch();

  const setCount = () => dispatch({ type: "SET_COUNT", count: 5 });
  const setText = () => dispatch({ type: "SET_TEXT", text: "bye" });
  const setColor = () => dispatch({ type: "SET_COLOR", color: "orange" });
  const toggleGood = () => dispatch({ type: "TOGGLE_GOOD" });

  return (
    <div>
      <p>
        <code>count: </code> {state.count}
      </p>
      <p>
        <code>text: </code> {state.text}
      </p>
      <p>
        <code>color: </code> {state.color}
      </p>
      <p>
        <code>isGood: </code> {state.isGood ? "true" : "false"}
      </p>

      <button onClick={setCount}>SET_COUNT</button>
      <button onClick={setText}>SET_Text</button>
      <button onClick={setColor}>SET_COLOR</button>
      <button onClick={toggleGood}>TOGGLE_GOOD</button>
    </div>
  );
}

export default SampleReducer;
