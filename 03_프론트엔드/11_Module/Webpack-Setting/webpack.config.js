const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const OptimizeCssAssetsPlugin = require('optimize-css-assets-webpack-plugin');
const TesrserWebpackPlugin = require('terser-webpack-plugin');
const {
    CleanWebpackPlugin
} = require('clean-webpack-plugin');

module.exports = {
    entry: './index.js',
    output: {
        filename: '[name].[chunkhash].js', //hash, contenthash, chunkhash
        path: path.resolve(__dirname, 'dist')
    },
    module: {
        rules: [{
                test: /\.css$/i,
                use: [
                    // {
                    //     loader: 'style-loader',
                    //     options: {
                    //         injectType: 'singletonStyleTag'
                    //     }
                    // },
                    {
                        loader: MiniCssExtractPlugin.loader
                    },
                    {
                        loader: 'css-loader',
                        options: {
                            modules: true
                        }
                    }
                ]
            },
            {
                test: /\.hbs$/,
                use: ['handlebars-loader']
            }
        ]
    },
    plugins: [
        new CleanWebpackPlugin(),
        new HtmlWebpackPlugin({
            title: 'Webpack',
            meta: {
                viewport: 'width=device-width, initial-scale=1.0'
            },
            minify: {
                collapseWhitespace: true,
                useShortDoctype: true,
                removeScriptTypeAttributes: true,
            },
            template: './template.hbs'
        }),
        new MiniCssExtractPlugin({
            filename: '[contenthash].css' //hash, createhash, chunkhash
        }),
        new OptimizeCssAssetsPlugin({
            assetNameRegExp: /\.css$/g,
            cssProcessor: require('cssnano'),
            cssProcessorPluginOptions: {
                preset: ['default', {
                    discardComments: {
                        removeAll: true
                    }
                }],
            },
            canPrint: true,
        }),
    ],
    optimization: {
        runtimeChunk: {
            name: 'runtime'
        },
        splitChunks: {
            cacheGroups: {
                commons: {
                    test: /[\\/]node_modules[\\/]/,
                    name: 'venders',
                    chunks: 'all'
                }
            }
        },
        minimize: true,
        minimizer: [new TesrserWebpackPlugin({
            cache: true
        })]
    },
    mode: 'none'
}