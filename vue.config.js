const webpack = require('webpack')

module.exports = {
 configureWebpack: {
     devServer: {
             proxy: {
                 '/api': {
                     target: 'http://127.0.0.1:5000',
                     changeOrigin: true, //是否跨域
                     ws: true,
                     pathRewrite: {
                     '^/api': '' //规定请求地址以什么作为开头
                     }
                 }
             }
         },
         plugins: [
            new webpack.ProvidePlugin({
                $:"jquery",
                jQuery:"jquery",
                "windows.jQuery":"jquery"
            })
        ]
    }
 }

 