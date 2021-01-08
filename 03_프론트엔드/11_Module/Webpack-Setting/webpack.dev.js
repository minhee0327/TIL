const { merge } = require('webpack-merge');
const common = require('./webpack.common');
const StyleLiintPlugin = require('stylelint-webpack-plugin');


const config = {
  mode: 'development',
  devServer: {
    open: true, //새창
    overlay: true, //error msg를 화면에 표현
    historyApiFallback: { // 특정경로 라우팅
      rewrites: [{
          from: /^\/subpage$/,
          to: 'subpage.html'
        },
        {
          from: /./,
          to: '404.html'
        },
      ],
    },
    port: 3333 //포트번호 수정
  },
  plugins:[
    new StyleLiintPlugin()
  ]
};

module.exports = merge(common, config);