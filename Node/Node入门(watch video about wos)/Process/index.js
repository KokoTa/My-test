// 进程

// 进程结束时
// process.on('exit', function () {
// 	setTimeout(function () { // 不执行
// 		console.log('OK1')
// 	}, 100)

// 	console.log('OK2') // 执行
// })

// 捕获错误, 但不关闭服务器
// process.on('uncaughtException', function (err) {
// 	console.log(err)
// })
// console.log('running') // 执行
// setTimeout(() => { // 执行
//   console.log('This will still run.');
// }, 500);
// ffff() // 报错
// console.log('No run') // 不执行

// 再来个例子
// var http = require('http')
// var server = http.createServer(function (req, res) {
// 	res.writeHead(200, {})
// 	res.end('Hello')
// 	xxx() // 想要忽略的错误
// 	console.log('No run')
// }).listen(8080)

// process.on('uncaughtException', function (err) {
// 	console.log(err)
// })
