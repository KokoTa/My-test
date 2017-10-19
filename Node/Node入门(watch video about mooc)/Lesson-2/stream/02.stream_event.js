var fs = require('fs');

var readStream = fs.createReadStream('stream_copy_image.js');//创建可读流,读数据

var n = 0;

readStream
	.on('data', function(chunk){//chunk是数据块,大概每秒64kb
		n++;//计数流的次数

		console.log('data emits');
		console.log(Buffer.isBuffer(chunk));
		//console.log(chunk.toString('utf8'));
		
		readStream.pause();//流暂停
		console.log('data pause');
		setTimeout(function(){
			console.log('data pause end');
			readStream.resume();
		}, 3000);

	})
	.on('readable', function(){
		console.log('data readable');
	})
	.on('end', function(){
		console.log(n);
		console.log('data ends');
	})
	.on('close', function(){
		console.log('data close');
	})
	.on('error', function(err){
		console.log('data error:' + err);
	})