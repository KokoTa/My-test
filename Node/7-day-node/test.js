var zlib = require('zlib')
var fs = require('fs')

var input = fs.createReadStream('t.txt')
var output = fs.createWriteStream('tt.gz')

input.pipe(zlib.createGzip()).pipe(output)