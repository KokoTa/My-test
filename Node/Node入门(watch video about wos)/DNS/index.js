// 域名解析
// 1 resolve()/lookup() 决定 域名转IP或dns的记录
// 2 reverse() 颠倒 IP转域名 

var dns = require('dns')

// 解析百度， 参数'A'表示指向IP（见阿里云的解析设置 or Node文档）
dns.resolve('baidu.com', 'A', function (err, res) { // 分析后四个IP对应四个运营商
	if (err) throw err
	console.log(res)
})

// 解析出来的是离我最近的一个IP, 参数4对应IP类型
dns.lookup('baidu.com', '4', function (err, res) {
	if (err) throw err
	console.log(res)
})

// 通过IP找域名, 一般都找不到= =
dns.reverse('111.13.101.208', function (res) { //  它没有错误参数，直接就是返回值
	console.log(res)
})