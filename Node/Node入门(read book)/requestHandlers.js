var querystring = require("querystring");//Post数据解析模块
var formidable = require("formidable");//处理POST数据的模块,解析复杂的数据（如图像）
var fs = require("fs");//文件读取到服务器的模块

function start(response,request){
	console.log("Request handler 'start' was called.");

	var body = '<html>'+
	  '<head>'+
	  '<meta http-equiv="Content-Type" '+
	  'content="text/html; charset=UTF-8" />'+
	  '</head>'+
	  '<body>'+
	  '<form action="/upload" enctype="multipart/form-data" '+
	  'method="post">'+
	  '<input type="file" name="upload">'+
	  '<input type="submit" value="Upload file" />'+
	  '</form>'+
	  '</body>'+
	  '</html>';
	
	response.writeHead(200, {"Content-Type": "text/html"});
	response.write(body);
	response.end();
}
function upload(response,request){
	console.log("Request handler 'upload' was called.");

	var form = new formidable.IncomingForm();//对提交表单的抽象表示
	console.log("About to parse");
	form.uploadDir='tmp';//跨区选择renameSync会出错,所以写一个临时路径,指向它
	form.parse(request,function(err,fields,files){
	    console.log('parsing done');
	    try{// 同步操作文件，try catch
	        fs.renameSync(files.upload.path,'tmp/test.jpg');//此时的file.upload指向了临时路径,临时路径要对应保存的路径
	    }catch(e){
	        console.log(e);
	    }
	    
	    response.writeHead(200,{'Content-Type':'text/html'});
	    response.write('received img:</br>');
	    response.write('<a href="/show"><img src="/show" /></a>');
	    response.end();
	});
}
function show(response,request){
	console.log("Request handler 'show' was called.");
	fs.readFile("./tmp/test.jpg", "binary",function(error,file){//binary二进制
		if(error){
			response.writeHead(500, {"Content-Type": "text/plain"});
			response.write(error + "\n");
			response.end();
		}else{
			response.writeHead(200, {"Content-Type": "image/jpg"});
			response.write(file, "binary");
			response.end();
		}
	})

}

exports.start = start;
exports.upload = upload;
exports.show = show;