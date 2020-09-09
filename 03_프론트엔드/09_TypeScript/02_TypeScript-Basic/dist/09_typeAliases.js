function createUserAction2() {
    return {
        do() { },
        name: '',
    };
}
class UserImpl {
    login() {
        throw new Error('Method not implemented.');
    }
}
function checkUSer(user) {
    if (user.login()) {
        return 'APPROVED';
    }
    else {
        return 'REJECTED';
    }
}
//# sourceMappingURL=09_typeAliases.js.map