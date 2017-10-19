var Readable = require('stream').Readable
var Writable = require('stream').Writable
var http = require('http')
var fs = require('fs')
var html = ''

var read = new Readable()
var write = new Writable()

write._write = function(chunk, encode, cb) {
	console.log(chunk.toString('utf-8'))
	cb()
}

var x = new Promise(function(resolve, reject) {
	http.get('http://www.imooc.com/video/11555', function(res) {
		res.on('data', function(chunk) {
			html += chunk
		})
		res.on('end', function() {
			resolve()
		})
	})
}).then(function() {
	var transform = html.toString('utf-8')
	read.push(transform)
	read.push(null)
	read.pipe(fs.createWriteStream('test.html'))
	// read.writeFile('2.html', html, 'utf-8')
})

