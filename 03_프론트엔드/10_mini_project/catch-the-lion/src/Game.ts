import { Board, Cell, DeadZone } from './Board';
import { Player, PlayerType } from './Player';
import './Piece';
import { Lion } from './Piece';

export class Game {
    private selectedCell: Cell;
    private turn = 0;
    private currentPlayer: Player;
    private gameInfoEl = document.querySelector('.alert');
    // enum도 사용가능하지만, 편의상 union 타입으로 작성, default value 는 started
    private state: 'STARTED' | 'END' = 'STARTED';

    readonly upperPlayer = new Player(PlayerType.UPPER);
    readonly lowerPlayer = new Player(PlayerType.LOWER);

    //board는 계속 쓰이면서, 작업을 고정한 상태이므로, readonly 타입
    readonly board = new Board(this.upperPlayer, this.lowerPlayer);
    readonly upperDeadZone = new DeadZone('upper');
    readonly lowerDeadZone = new DeadZone('lower');

    constructor() {
        console.log(this.upperPlayer);
        console.log(this.lowerPlayer);
        const boardContainer = document.querySelector('.board-container');
        // console.log(boardContainer.firstChild); //text제거한후 childappend해줄것
        boardContainer.firstChild.remove();
        boardContainer.appendChild(this.board._el);

        // 시작은 항상 upper player가 하도록 설정
        this.currentPlayer = this.upperPlayer;

        this.board.render();
        this.renderInfo();

        //event 처리
        this.board._el.addEventListener('click', (e) => {
            if (this.state === 'END') {
                return false;
            }
            //type guard: HTML element만 가져옴
            if (e.target instanceof HTMLElement) {
                let cellEl: HTMLElement;
                // 요소의 클래스명에 cell이 있는 요소와, piece가있는 부모요소를 선택해서 cellEl에 저장하고 나머지 cell은 false로 무시
                if (e.target.classList.contains('cell')) {
                    cellEl = e.target;
                } else if (e.target.classList.contains('piece')) {
                    cellEl = e.target.parentElement;
                } else {
                    return false;
                }

                //board에서 mapping해준 HTML element를 가지고 선택된 peice를 가져옴
                const cell = this.board.map.get(cellEl);

                if (this.isCurrentUserPiece(cell)) {
                    this.select(cell);
                    return false;
                }
                //자기말을 선택한 상태라면 움직이고, 턴은 바꿔줌
                if (this.selectedCell) {
                    this.move(cell);
                    this.changeTurn();
                } else if (!this.selectedCell) {
                    return false;
                } else {
                    alert(`현재 유저는 ${this.currentPlayer.type} 입니다.`);
                    return false;
                }
            }
        });
    }
    move(cell: Cell) {
        this.selectedCell.deactive();
        // selectedCell 을 cell로 이동하는데, getKilled를 했을때 있으면 그걸 가져와서 바꿔준다.
        const killed = this.selectedCell.getPiece().move(this.selectedCell, cell).getKilled();
        this.selectedCell = cell;

        if (killed) {
            if (killed.ownerType === PlayerType.UPPER) {
                this.lowerDeadZone.put(killed);
            } else {
                this.upperDeadZone.put(killed);
            }
            if (killed instanceof Lion) {
                this.state = 'END';
            }
        }
    }
    // 현재 turn의 player와 일치하면서, cell, piece 정보가 있을경우 true반환
    isCurrentUserPiece(cell: Cell) {
        //!= 을 사용한이유: 비어있는경우(undefined)를 고려해서
        return cell != null && cell.getPiece() != null && cell.getPiece().ownerType === this.currentPlayer.type;
    }
    select(cell: Cell) {
        //선택한 piece가 비어있으면 return
        if (cell.getPiece() == null) {
            return;
        }
        // 자기 자신의 말을 선택한게 아니라면 return
        if (cell.getPiece().ownerType !== this.currentPlayer.type) {
            return;
        }

        //즉 자기가 선택한 말이 비어있지않고, 자신의 말이어야지만 움직였을때 반응
        if (this.selectedCell) {
            this.selectedCell.deactive();
            this.selectedCell.render();
        }
        this.selectedCell = cell;
        this.selectedCell.active();
        this.selectedCell.render();
    }
    //턴이 계속 있는 경우에는 parameter가 전달이 안되니까, ?를 붙여서 선택적으로 매개변수를 받는다.
    renderInfo(extraMessgae?: string) {
        this.gameInfoEl.innerHTML = `#${this.turn}턴 ${this.currentPlayer.type} 차례 ${extraMessgae ? '| ' + extraMessgae : ''}`;
    }
    changeTurn() {
        this.selectedCell.deactive();
        this.selectedCell = null;

        if (this.state === 'END') {
            this.renderInfo('END!');
        } else {
            this.turn += 1;
            this.currentPlayer = this.currentPlayer === this.lowerPlayer ? this.upperPlayer : this.lowerPlayer;
            this.renderInfo();
        }
        //매 턴이 지날때마다, 화면에 다시 결과가 그려지도록 한다.
        this.board.render();
    }
}
