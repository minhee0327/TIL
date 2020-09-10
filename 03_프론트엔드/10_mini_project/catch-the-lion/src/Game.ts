import { Board, DeadZone } from './Board';

export class Game {
    //board는 계속 쓰이면서, 작업을 고정한 상태이므로, readonly 타입
    readonly board = new Board();
    readonly upperDeadZone = new DeadZone('upper');
    readonly lowerDeadZone = new DeadZone('lower');

    constructor() {
        const boardContainer = document.querySelector('.board-container');
        // console.log(boardContainer.firstChild); //text제거한후 childappend해줄것
        boardContainer.firstChild.remove();
        boardContainer.appendChild(this.board._el);
    }
}
