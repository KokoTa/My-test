var http = require('http');

http.createServer(function(resquest,response){
	response.writeHead(200,{'Content-Type':'text/plain'});
	response.end('Hello World!!');
	console.log('Already response.')
}).listen(1337,'127.0.0.1');

console.log('Server running now.');