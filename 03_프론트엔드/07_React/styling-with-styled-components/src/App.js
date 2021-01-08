import React, { useState } from "react";
import styled, { ThemeProvider } from "styled-components";
import Button from "./components/Button";
import Dialog from "./components/Dialog";

const AppBlock = styled.div`
  width: 512px;
  margin: 0 auto;
  margin-top: 4rem;
  padding: 1rem;
  border: 1px solid black;
`;

const ButtonGroup = styled.div`
  & + & {
    margin-top: 1rem;
  }
`;

function App() {
  const [dialog, setDialog] = useState(false);
  const onClick = () => {
    setDialog(true);
  };
  const onConfirm = () => {
    console.log("확인");
    setDialog(false);
  };
  const onCancle = () => {
    console.log("취소");
    setDialog(false);
  };

  return (
    <ThemeProvider
      theme={{ palette: { blue: "#228be6", gray: "#495057", pink: "#f06595" } }}
    >
      <>
        <AppBlock>
          <ButtonGroup>
            <Button size="large">Button</Button>
            <Button>Button</Button>
            <Button size="small">Button</Button>
          </ButtonGroup>
          <ButtonGroup>
            <Button color="gray" size="large">
              Button
            </Button>
            <Button color="gray">Button</Button>
            <Button color="gray" size="small">
              Button
            </Button>
          </ButtonGroup>
          <ButtonGroup>
            <Button color="pink" size="large">
              Button
            </Button>
            <Button color="pink">Button</Button>
            <Button color="pink" size="small">
              Button
            </Button>
          </ButtonGroup>
          <ButtonGroup>
            <Button outline size="large">
              Button
            </Button>
            <Button outline color="gray">
              Button
            </Button>
            <Button outline color="pink" size="small">
              Button
            </Button>
          </ButtonGroup>
          <ButtonGroup>
            <Button fullWidth size="large">
              Button
            </Button>
            <Button fullWidth color="gray" size="large">
              Button
            </Button>
            <Button onClick={onClick} fullWidth color="pink" size="large">
              삭제하기
            </Button>
          </ButtonGroup>
        </AppBlock>
        <Dialog
          title="정말 삭제하시겠습니까?"
          confirmText="삭제"
          cancleText="취소"
          onConfirm={onConfirm}
          onCancle={onCancle}
          visible={dialog}
        >
          데이터를 정말로 삭제하시겠습니까?
        </Dialog>
      </>
    </ThemeProvider>
  );
}
export default App;
