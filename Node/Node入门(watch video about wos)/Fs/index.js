// FS模块

var fs = require('fs')
var exec = require('child_process').exec

// 读取文件
// var data = fs.readFileSync('test.txt', 'utf-8') // 同步读取

// 复制文件
// exec('copy test.txt test2.txt') // Dos命令的写法

// 修改文件名
// fs.renameSync('test.txt', 'test2.txt');

// 删除文件
// fs.unlinkSync('test.txt');

// 修改文件
// 'a' - 以追加模式打开文件。如果文件不存在，则会被创建。
fs.open('test.txt', 'a', function (err, file) {
	if (err) throw err
	var data = 'Yo Man!'
	fs.write(file, data, function (err, written, string) {
		console.log(written) // 写入的字节数
		console.log(string) // 内容
		fs.close(file, function (err) { // 结束修改，防止多人同时修改文件要抛错
			if (err) throw err
			console.log('file closed')
		})
	})
})