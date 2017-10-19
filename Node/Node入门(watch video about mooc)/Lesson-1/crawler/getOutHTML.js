var url = 'http://nodejs.cn/api/http.html'
var request = require('request')
var fs = require('fs')

request(url).pipe(fs.createWriteStream('out.html'))