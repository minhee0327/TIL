const myTV = {
    turnOn() {
        return true;
    },
    turnOff() { },
};
function tryTurnOn(tv) {
    tv.turnOn();
}
tryTurnOn(myTV);
function createBoard() {
    const cells = [];
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
    move(from, to) {
        return true;
    },
};
//# sourceMappingURL=03_interface.js.map