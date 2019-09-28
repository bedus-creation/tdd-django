const mix = require('laravel-mix');
const tailwindcss = require('tailwindcss');

require('laravel-mix-purgecss');

mix.webpackConfig({
    resolve: {
        extensions: ['.js', '.vue', '.json'],
        alias: {
            '@': __dirname + '/resources/js'
        },
    },
    output: {
        chunkFilename: 'js/chunks/[name].js?id=[hash]',
    },
});


mix.js('resources/js/app.js', 'static/js')
    .extract(['vue']);
mix.sass('resources/sass/app.scss', 'static/css');
mix.postCss('resources/sass/tailwind.css', 'static/css', [
    require('tailwindcss'),
]).purgeCss();
