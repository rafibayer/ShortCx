const path = require('path');

module.exports = {
  entry: {
    index: './src/index.js',
    short: './src/short.js'
  },
  output: {
    filename: '[name].bundle.js',
    path: path.resolve(__dirname, 'dist'),
  },
};