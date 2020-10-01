function ask(quest, yes, no) {
    if (quest) return yes();
    return no();
}

function checkYes() {
    return "동의합니다."
}

function checkNo() {
    return "동의 불가능!"
}



alert(ask(confirm("동의하시겠습니까?"), checkYes, checkNo));