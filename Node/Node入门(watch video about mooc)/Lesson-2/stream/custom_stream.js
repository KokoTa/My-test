//流的定制(增加自定义方法)
var stream = require('stream');
var util = require('util');
///////////////////////////
function ReadStream(){//继承
	stream.Readable.call(this);
}

util.inherits(ReadStream,stream.Readable);//继承

ReadStream.prototype._read = function(){
	this.push('1');
	this.push('2');
	this.push('3');
	this.push(null);//结束

}
///////////////////////////
function WriteStream(){
	stream.Writable.call(this);
}

util.inherits(WriteStream,stream.Writable);

WriteStream.prototype._write = function(chunk,encode,cb){
	console.log(chunk.toString());
	cb();
}
///////////////////////////
function TransformStream(){
	stream.Transform.call(this);
}

util.inherits(TransformStream,stream.Transform);

TransformStream.prototype._transform = function(chunk,encode,cb){
	this.push(chunk);//传入数据，不保存，直接调用处理
	cb();
}
TransformStream.prototype._flush = function(chunk,encode,cb){
	this.push('Oh Yeah!');//传入后执行内容的添加
}

///////////////////////////
var rs = new ReadStream();
var ws = new WriteStream();
var ts = new TransformStream();

rs.pipe(ts).pipe(ws);//加一个字符串后输出






// ES6的写法

// "use strict"
// let stream=require('stream');


// class ReaderStream extends stream.Readable{
//     constructor(){
//         super();
//         this._cached=new Buffer('');
//     }
//     _read(){
//         this.push('I');
//         this.push('Love');
//         this.push('Mock\n');
//         this.push(null);
//     }
// }

// class WriteStream extends stream.Writable{
//     _write(chuck,encode,cb){
//         console.log(chuck.toString())
//         cb();
//     }
// }

// class Transform extends stream.Transform{
//     _transform(chunk,encode,cb){
//         this.push(chunk);
//         cb();
//     }
//     _flush(cb){
//         this.push('oh Yeah')
//         cb();
//     }
// }

// let read=new ReaderStream();
// let write = new WriteStream();
// let transform = new Transform();

// read.pipe(transform).pipe(write);