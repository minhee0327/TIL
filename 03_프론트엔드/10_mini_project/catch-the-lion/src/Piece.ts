import { Cell, Position } from './Board';
import { PlayerType, Player } from './Player';
// 이미지 파일을 모듈로 인식할 수 있도록 global.d.ts에서 설정.
import chickenImage from './images/chicken.png';
import elephantImage from './images/elephant.png';
import giraffeImage from './images/giraffe.png';
import lionImage from './images/lion.png';

console.log(lionImage);

export class MoveResult {
    constructor(private killedPiece: Piece) {}
    getKilled() {
        return this.killedPiece;
    }
}

export interface Piece {
    ownerType: PlayerType;
    currentPosition: Position;
    move(from: Cell, to: Cell): MoveResult;
    render(): string;
}

abstract class DefaultPieace implements Piece {
    constructor(public readonly ownerType: PlayerType, public currentPosition: Position) {}
    move(from: Cell, to: Cell): MoveResult {
        if (!this.canMove(to.position)) {
            alert('해당말은 이곳으로 움직일 수 없습니다.. 다시선택해주세요');
            // throw new Error(`Cannot move to this location`);
        }
        const moveResult = new MoveResult(to.getPiece() != null ? to.getPiece() : null);
        to.put(this);
        from.put(null);
        this.currentPosition = to.position;
        return moveResult;
    }
    // 동물의 종류별로 움직임이 가능한 타입과, 보여지는것이 다르기때문에 하위타입에서 구현할 항목들(canMove, render)
    abstract canMove(position: Position): boolean;
    abstract render();
}

export class Lion extends DefaultPieace {
    canMove(position: Position): boolean {
        const canMove =
            (position.row === this.currentPosition.row && position.col === this.currentPosition.col + 1) ||
            (position.row === this.currentPosition.row && position.col === this.currentPosition.col - 1) ||
            (position.row === this.currentPosition.row + 1 && position.col === this.currentPosition.col) ||
            (position.row === this.currentPosition.row - 1 && position.col === this.currentPosition.col) ||
            (position.row === this.currentPosition.row + 1 && position.col === this.currentPosition.col + 1) ||
            (position.row === this.currentPosition.row + 1 && position.col === this.currentPosition.col - 1) ||
            (position.row === this.currentPosition.row - 1 && position.col === this.currentPosition.col + 1) ||
            (position.row === this.currentPosition.row - 1 && position.col === this.currentPosition.col - 1);
        return canMove;
    }
    render(): string {
        return `<img class="piece ${this.ownerType}" src ="${lionImage}" width="90%" height ="90%"/>`;
    }
}

export class Elephant extends DefaultPieace {
    canMove(position: Position): boolean {
        const canMove =
            (position.row === this.currentPosition.row + 1 && position.col === this.currentPosition.col + 1) ||
            (position.row === this.currentPosition.row + 1 && position.col === this.currentPosition.col - 1) ||
            (position.row === this.currentPosition.row - 1 && position.col === this.currentPosition.col + 1) ||
            (position.row === this.currentPosition.row - 1 && position.col === this.currentPosition.col - 1);
        return canMove;
    }
    render(): string {
        return `<img class="piece ${this.ownerType}" src ="${elephantImage}" width="90%" height ="90%"/>`;
    }
}

export class Giraffe extends DefaultPieace {
    canMove(position: Position): boolean {
        const canMove =
            (position.row === this.currentPosition.row && position.col === this.currentPosition.col + 1) ||
            (position.row === this.currentPosition.row && position.col === this.currentPosition.col - 1) ||
            (position.row === this.currentPosition.row + 1 && position.col === this.currentPosition.col) ||
            (position.row === this.currentPosition.row - 1 && position.col === this.currentPosition.col);
        return canMove;
    }
    render(): string {
        return `<img class="piece ${this.ownerType}" src ="${giraffeImage}" width="90%" height ="90%"/>`;
    }
}

export class Chicken extends DefaultPieace {
    canMove(position: Position): boolean {
        const canMove = position.row === this.currentPosition.row + (this.ownerType === 'UPPER' ? 1 : -1);
        return canMove;
    }
    render(): string {
        return `<img class="piece ${this.ownerType}" src ="${chickenImage}" width="90%" height ="90%"/>`;
    }
}
