let input = prompt("Who's there?", "");
if (input == 'Admin') {
    let password = prompt("Password?", "");
    if (password === 'TheMaster') {
        alert("Welcome!");
    } else if (!password) {
        alert("Cancled")
    } else {
        alert("Wrong Password")
    }
} else if (!input) {
    alert("Cancled")
} else {
    alert("I don't konw you")
}