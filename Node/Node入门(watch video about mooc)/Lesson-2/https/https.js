var https = require('https');//https模块
var fs = require('fs');//文件系统操作模块

var options = {
	key: fs.readFileSync('ssh_key.pem'),//读取密匙
	cert : fs.readFileSync('ssh_cert.pem');//读取证书
}

https.createServer(options, function(req,res){//用法和普通的http一样
	res.writeHead(200);
	res.end('Hello World');
}).listen(8090);