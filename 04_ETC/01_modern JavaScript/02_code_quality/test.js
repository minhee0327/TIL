describe("pow", function () {
    // it("2를 세번 곱하면 8 입니다.", function () {
    //     assert.equal(pow(2, 3), 8)
    // })
    // it("3을 네번 곱하면 81 입니다.", function () {
    //     assert.equal(pow(3, 4), 81)
    // })

    // 아래방법은 assert하나에서 error발생하게되면 다음 assert를 테스트 해 볼 수 없다.
    // it("주어진 숫자의 n제곱", function () {
    //     assert.equal(pow(2, 3), 8)
    //     assert.equal(pow(3, 4), 81)
    // })

    describe("x를 세번 곱합니다.", function () {
        function makeTest(x) {
            let expected = x * x * x;
            it(`${x}을/를 세번 곱하면 ${expected}입니다. `, function () {
                assert.equal(pow(x, 3), expected);
            })
        }
        for (let x = 1; x <= 5; x++) {
            makeTest(x);
        }
    })
    // 실패할수밖에 없는 테스트를 추가하고, 테스트를 통과할 수 있게 코드개선
    it("n이 음수일 때 결과는 NaN입니다.", function () {
        assert.isNaN(pow(2, -1));
    });

    it("n이 정수가 아닐 때 결과는 NaN입니다.", function () {
        assert.isNaN(pow(2, 1.5));
    });
})