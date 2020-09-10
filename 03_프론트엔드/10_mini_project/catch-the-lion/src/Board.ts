import { Piece } from './Piece';

export interface Position {
    row: number;
    col: number;
}

export class Cell {
    private isActive = false;
    readonly _el: HTMLElement = document.createElement('div');

    constructor(public readonly position: Position, private piece: Piece) {
        this._el.classList.add('cell');
    }

    put(piece: Piece) {
        this.piece = piece;
    }
    getPiece() {
        return this.piece;
    }
    active() {
        this.isActive = true;
    }
    deactive() {
        this.isActive = false;
    }
    render() {
        if (this.isActive) {
            this._el.classList.add('active');
        } else {
            this._el.classList.remove('active');
        }
        this._el.innerHTML = this.piece ? this.piece.render() : '';
    }
}

//Board는 여러 cell들의 집합으로 이루어져있다.
export class Board {
    cells: Cell[] = [];
    _el: HTMLElement = document.createElement('div');

    constructor() {
        this._el.className = 'board';

        for (let row = 0; row < 4; row++) {
            const rowEl = document.createElement('div');
            rowEl.className = 'row';
            this._el.appendChild(rowEl);
            for (let col = 0; col < 3; col++) {
                // 보드판에 기본 cell을 만드는과정, 2번째파라미터 null(아무것도 올려져 있지 않다는 뜻.)
                const cell = new Cell({ row, col }, null);
                this.cells.push(cell);
                rowEl.appendChild(cell._el);
            }
        }
    }

    render() {
        this.cells.forEach((v) => v.render());
    }
}

export class DeadZone {
    private cells: Cell[] = [];
    readonly deadZoneEl = document.getElementById(`${this.type}_deadzone`).querySelector('.card-body');

    constructor(public type: 'upper' | 'lower') {
        // deadzone에 올수있는 말의 개수는 4개이므로 열 4개만큼만 반복
        for (let col = 0; col < 4; col++) {
            const cell = new Cell({ row: 0, col }, null);
            this.cells.push(cell);
            this.deadZoneEl.appendChild(cell._el);
        }
    }

    put(piece: Piece) {
        const emptyCell = this.cells.find((v) => v.getPiece() == null);
        emptyCell.put(piece);
        emptyCell.render();
    }

    render() {
        this.cells.forEach((v) => v.render());
    }
}
