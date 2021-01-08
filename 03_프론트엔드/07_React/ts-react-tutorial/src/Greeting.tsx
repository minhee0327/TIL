import React from "react";

type GreetingsProps = {
  name: string;
  mark: string;
  optional?: string;
  onClick: (name: string) => void; //매개변수type은 string, 반환은 void로 진행
};

// const Greetings = ({ name, mark }: GreetingsProps) => (
//   <div>
//     Hello, {name} {mark}
//   </div>
// );

function Greetings({ name, mark, optional, onClick }: GreetingsProps) {
  const handleClick = () => onClick(name);
  return (
    <div>
      Hello, {name} {mark}
      {optional && { optional }}
      <div>
        <button onClick={handleClick}>Click Me</button>
      </div>
    </div>
  );
}

Greetings.defaultProps = {
  mark: "!",
};

export default Greetings;
