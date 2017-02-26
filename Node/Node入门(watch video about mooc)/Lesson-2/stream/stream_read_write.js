var Readable = require('stream').Readable;
var Writable = require('stream').Writable;

var readStream = new Readable();//读
var writeStream = new Writable();//写

readStream.push('1');
readStream.push('2');
readStream.push('3');
readStream.push(null);//结束

writeStream._write = function(chunk,encode,cb){
	console.log(chunk.toString());
	cb();
}

readStream.pipe(writeStream);//连