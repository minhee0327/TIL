//걸프 의존성 
const gulp = require('gulp');
const babel = require('gulp-babel');
const eslint = require('gulp-eslint');

gulp.task('default', function (done) {
    gulp.src(["es6/**/*.js", "public/es6/**/*.js"])
        .pipe(eslint())
        .pipe(eslint.format())

    //node source
    //**: 서브디렉터리를 포함해, 모든 디렉터리를 뜻함.
    gulp.src("es6/**/*.js")
        .pipe(babel({
            presets: ['@babel/preset-env'],
        }))
        .pipe(gulp.dest("dist"))

    //browser source
    gulp.src("public/es6/**/*.js")
        .pipe(babel({
            presets: ['@babel/preset-env'],
        }))
        .pipe(gulp.dest("public/dist"));

    done();
});