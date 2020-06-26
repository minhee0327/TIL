const number = document.getElementById('number');
const increase = document.getElementById('increase');
const decrease = document.getElementById('decrease');

increase.onclick = () => {
    num = parseInt(number.innerText);
    number.innerText = num + 1
}

decrease.onclick = () => {
    num = parseInt(number.innerText);
    number.innerText = num - 1;
}

const open = document.getElementById('open');
const close = document.getElementById('close');
const modal = document.querySelector('.modal-wrapper');

open.onclick = () => {
    modal.style.display = "flex"
}

close.onclick = () => {
    modal.style.display = "none"
}