const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const webpack = require('webpack');
const isProduction = process.env.NODE_ENV === 'PRODUCTION';

module.exports = {
  entry: './index.js',
  output: {
    filename: '[name].[chunkhash].js', //hash, contenthash, chunkhash
    path: path.resolve(__dirname, 'dist'),
  },
  module: {
    rules: [
      {
        test: /\.css$/i,
        use: [
          // {
          //     loader: 'style-loader',
          //     options: {
          //         injectType: 'singletonStyleTag'
          //     }
          // },
          {
            loader: MiniCssExtractPlugin.loader,
          },
          {
            loader: 'css-loader',
            options: {
              modules: true,
            },
          },
        ],
      },
      {
        test: /\.hbs$/,
        use: ['handlebars-loader'],
      },
    ],
  },
  plugins: [
    new CleanWebpackPlugin(),
    new HtmlWebpackPlugin({
      title: 'Webpack',
      template: './template.hbs',
      meta: {
        viewport: 'width=device-width, initial-scale=1.0',
      },
      minify: isProduction
        ? {
            collapseWhitespace: true,
            useShortDoctype: true,
            removeScriptTypeAttributes: true,
          }
        : false,
    }),
    new MiniCssExtractPlugin({
      filename: '[contenthash].css', //hash, createhash, chunkhash
    }),
    new webpack.DefinePlugin({
      IS_PRODUCTION: isProduction,
    }),
  ],
};
