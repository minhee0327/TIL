const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const {
  CleanWebpackPlugin
} = require('clean-webpack-plugin');
const webpack = require('webpack');

const isProduction = process.env.NODE_ENV === 'PRODUCTION';
const postcssLoader = {
  loader: 'postcss-loader',
  options: {
    config: {
      path: 'postcss.config.js'
    }
  }
}

module.exports = {
  entry: './src/index.js',
  output: {
    filename: '[name].[chunkhash].js', //hash, contenthash, chunkhash
    path: path.resolve(__dirname, 'dist'),
  },
  module: {
    rules: [{
        test: /\.s?css$/i,
        oneOf: [{
          test: /\.module\.s?css$/,
          use: [{
              loader: MiniCssExtractPlugin.loader,
            },
            {
              loader: 'css-loader',
              options: {
                modules: true,
              },
            },
            postcssLoader,
            'sass-loader'
          ],
        }, {
          use: [
            MiniCssExtractPlugin.loader,
            'css-loader',
            postcssLoader,
            'sass-loader'
          ]
        }]
      },
      {
        test: /\.hbs$/,
        use: ['handlebars-loader'],
      },
      {
        //svg확장자는 url-loader에서 다룰 예정
        //i의의미: 대소문자 구분 X
        test: /\.(png|jpe?g|gif)$/i,
        use: [{
          loader: 'file-loader',
          options: {
            // ext: 확장자 약어
            name() {
              if (!isProduction) {
                return '[path][name].[ext]'
              }
              return '[contenthash].[ext]'
            },
            publicPath: 'assets/', // 공용으로 사용되는 key (특정로더 뿐만아니라 모듈들에 대해서도 정의할 수 있다.)
            outputPath: 'assets/' // 빌드후, 파일 폴더들이 실제 생성되는 경로를 지정 output에서 설정한 path기준으로 하위 경로 설정
          }
        }]
      },
      {
        test: /\.svg$/i,
        use: [{
          loader: 'url-loader',
          options: {
            limit: 8192
          }
        }]
      },
      {
        test: /.js/,
        exclude: /node_modules/,
        loader: 'babel-loader'
      }
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
      minify: isProduction ? {
        collapseWhitespace: true,
        useShortDoctype: true,
        removeScriptTypeAttributes: true,
      } : false,
    }),
    new MiniCssExtractPlugin({
      filename: '[contenthash].css', //hash, createhash, chunkhash
    }),
    new webpack.DefinePlugin({
      IS_PRODUCTION: isProduction,
    }),
  ],
};