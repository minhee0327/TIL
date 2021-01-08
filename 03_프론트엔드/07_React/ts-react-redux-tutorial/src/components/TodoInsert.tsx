import React, { ChangeEvent, FormEvent, useState } from "react";

type TodoInsertProps = {
  onInsert: (text: string) => void;
};

function TodoInsert({ onInsert }: TodoInsertProps) {
  const [value, setValue] = useState("");
  const onChange = (e: ChangeEvent<HTMLInputElement>) => {
    setValue(e.target.value);
  };
  const onSubmit = (e: FormEvent) => {
    e.preventDefault();
    onInsert(value);
    setValue("");
  };
  return (
    <form onSubmit={onSubmit}>
      <input
        value={value}
        onChange={onChange}
        placeholder="할일을 입력하세요"
      />
      <button onSubmit={onSubmit}>등록</button>
    </form>
  );
}

export default TodoInsert;
