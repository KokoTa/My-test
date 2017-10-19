var fs = require('fs');

var readStream = fs.createReadStream('1.mp4');//读
var writeStream = fs.createWriteStream('1-stream.mp4');//写

readStream
	.on('data',function(chunk){
		if(writeStream.write(chunk) === false){//读和写速度不同,保证写完再读,防止爆仓
			console.log('still cached');
			readStream.pause();
		}
	})
	.on('end',function(){
		writeStream.end();
	})

writeStream.on('drain',function(){//块数据写完了,恢复读
	console.log('data drains');

	readStream.resume();
})