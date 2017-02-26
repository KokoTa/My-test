var http = require('http');

http.createServer(function(resquest,response){
	response.writeHead(200,{'Content-Type':'text/plain'});
	response.write("Hello World!!")
	response.end();
	console.log('Already response.')
}).listen(1337,'127.0.0.1');

console.log('Server running now.');