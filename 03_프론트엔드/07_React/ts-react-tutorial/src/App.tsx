import React from "react";
import SampleReducer from "./ReducerSample";
import { SampleProvider } from "./SampleContext";

function App() {
  // const onSubmit = (form: { name: string; description: string }) => {
  //   console.log(form);
  // };
  return (
    <SampleProvider>
      <SampleReducer />
    </SampleProvider>
  );
}

export default App;
