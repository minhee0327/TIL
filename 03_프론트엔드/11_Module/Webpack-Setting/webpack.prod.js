const { merge } = require('webpack-merge');
const OptimizeCssAssetsPlugin = require('optimize-css-assets-webpack-plugin');
const TesrserWebpackPlugin = require('terser-webpack-plugin');
const common = require('./webpack.common');

const config = {
  plugins: [
    new OptimizeCssAssetsPlugin({
      assetNameRegExp: /\.css$/g,
      cssProcessor: require('cssnano'),
      cssProcessorPluginOptions: {
        preset: [
          'default',
          {
            discardComments: {
              removeAll: true,
            },
          },
        ],
      },
      canPrint: true,
    }),
  ],
  optimization: {
    runtimeChunk: {
      name: 'runtime',
    },
    splitChunks: {
      cacheGroups: {
        commons: {
          test: /[\\/]node_modules[\\/]/,
          name: 'venders',
          chunks: 'all',
        },
      },
    },
    minimize: true,
    minimizer: [
      new TesrserWebpackPlugin({
        cache: true,
      }),
    ],
  },
  mode: 'production',
};

module.exports = merge(common, config);
