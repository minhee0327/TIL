var StarbucksGrade;
(function (StarbucksGrade) {
    StarbucksGrade[StarbucksGrade["WELCOME"] = 0] = "WELCOME";
    StarbucksGrade[StarbucksGrade["GREEN"] = 1] = "GREEN";
    StarbucksGrade[StarbucksGrade["GOLD"] = 2] = "GOLD";
})(StarbucksGrade || (StarbucksGrade = {}));
function getDiscound(v) {
    switch (v) {
        case StarbucksGrade.WELCOME:
            return 0;
        case StarbucksGrade.GREEN:
            return 5;
        case StarbucksGrade.GOLD:
            return 10;
    }
}
console.log(getDiscound(StarbucksGrade.GREEN));
console.log(StarbucksGrade.GREEN);
console.log(StarbucksGrade['GOLD']);
console.log(StarbucksGrade[0]);
console.log(StarbucksGrade);
//# sourceMappingURL=05_enum.js.map