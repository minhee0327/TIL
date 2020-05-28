module.exports = {
    "env": {
        "browser": true,
        "es6": true,
    },
    "globals": {
        "Atomics": "readonly",
        "SharedArrayBuffer": "readonly",
    },
    "parserOptions": {
        "ecmaVersion": 11,
    },
    "rules": {
        "comma-dangle": [
            2,
            "always-multiline",
        ],
        "indent": [
            2,
            4,
        ],
    },
};
