// 加密

var crypto = require('crypto')
var md5 = crypto.createHash('md5') // 创建一个哈希对象，可以用来产生哈希算法
var password = 'KokoTa' // 要加密的字段

md5.update(password) // 我要更新这个字段

var d = md5.digest('md5') // 选择加密方式 md5/sha1

console.log(d)


