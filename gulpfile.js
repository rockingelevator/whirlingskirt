var gulp = require('gulp');
var stylus = require('gulp-stylus');
var watchify = require('watchify');
var gutil = require('gulp-util');
var source = require('vinyl-source-stream');
var browserify = require('browserify');
var reactify = require('reactify');


var STATIC_ROOT = './whirlingskirt/static';


gulp.task('stylus', function() {
    gulp.src('./whirlingskirt/styl/**/*.styl')
        .pipe(stylus())
    .pipe(gulp.dest(STATIC_ROOT + '/css'));
});


gulp.task('default', function(){
    var bundler = watchify(browserify({
        entries: [STATIC_ROOT + '/components/app.jsx'],
        transform: [reactify],
        extensions: ['.jsx'],
        debug: true,
        cache: {},
        packageCache: {},
        fullPaths: true
    }));

    function build(file) {
        if(file) gutil.log('Recompiling ' + file);
        return bundler
            .bundle()
            .on('error', gutil.log.bind(gutil, 'Browserify Error'))
            .pipe(source('main.js'))
            .pipe(gulp.dest(STATIC_ROOT + '/js'));
    };

    build();
    bundler.on('update', build);

    //gulp.start('stylus', 'cssBuild');
    gulp.watch('./whirlingskirt/styl/**/*.styl', ['stylus']);
});



