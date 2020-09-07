interface TV {
    turnOn(): boolean;
    turnOff(): void;
}

const myTV: TV = {
    turnOn() {
        return true;
    },
    turnOff() {},
};

function tryTurnOn(tv: TV) {
    tv.turnOn();
}

tryTurnOn(myTV);

//행위는 없고, 데이터만 담은 속성.(데이터 타입으로 interface정의)
interface Cell {
    row: number;
    col: number;
    piece?: Piece; //옵셔널한 속성임을 ? 키워드로 주었음.(속성을 갖지 않아도 cell타입객체 가능)
}

interface Piece {
    move(from: Cell, to: Cell): boolean;
}

function createBoard() {
    const cells: Cell[] = [];

    for (let row = 0; row < 4; row++) {
        for (let col = 0; row < 3; row++) {
            cells.push({
                row,
                col,
            });
        }
    }
    return cells;
}

const board = createBoard();
board[0].piece = {
    move(from: Cell, to: Cell) {
        return true;
    },
};
