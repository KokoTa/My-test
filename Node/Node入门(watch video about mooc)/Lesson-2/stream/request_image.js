var http = require('http');
var fs = require('fs');
var request = require('request');//请求模块，需安装
http
	.createServer(function(req,res){
		// 方法一
		// fs.readFile('./buffer/1.png', function(err,data){
		// 	if(err){
		// 		res.end('file not exist!');
		// 	}else{
		// 		res.writeHeader(200,{'Context-Type':'text/html'});
		// 		res.end(data);
		// 	}
		// });
		// 方法二
		//fs.createReadStream('../buffer/1.png').pipe(res);

		request('http://www.91danji.com/attachments/201608/25/11/1i7mpmkyy.jpg').pipe(res);//pipe连接请求和要应答的数据


	})
	.listen(8090);