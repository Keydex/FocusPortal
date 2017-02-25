var gulp = require('gulp'),
    gutil = require('gulp-util'),
    sass = require('gulp-sass'),
    coffee = require('gulp-coffee'),
    uglify = require('gulp-uglify'),
    concat = require('gulp-concat'),
    connect = require('gulp-connect');

var coffeeSources = ['scripts'],
    jsSources = ['scripts/*.js'],
    sassSources = ['styles/*.scss'],
    htmlSources = ['**/*.html']
    outputDir = 'public';
var port = process.env.PORT || 3000;

gulp.task('name', function(){ //Gulp Object, task method



});

gulp.task('watch', function() {
  livereload.listen(port);
  gulp.watch('less/*.less', ['less']);
});
