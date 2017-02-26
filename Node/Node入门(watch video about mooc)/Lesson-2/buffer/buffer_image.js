var fs = require('fs');//文件处理模块

fs.readFile('1.png',function(err,origin_buffer){//读取文件，传入回调
	console.log(Buffer.isBuffer(origin_buffer));//是否是buffer

	fs.writeFile('1s.png',origin_buffer,function(err){
		if(err) console.log(err);
	});//创建新图

	var base64Image = origin_buffer.toString('base64');

	console.log(base64Image);//编码后的代码

	var decodedImage = Buffer.from(base64Image,'base64');

	console.log(Buffer.compare(origin_buffer,decodedImage));//两者是否一样

	fs.writeFile('1t.png',decodedImage,function(err){
		if(err) console.log(err);
	})
})