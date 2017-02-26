//爬取html
var http = require('http');
var url = 'http://www.imooc.com/video/7965';
var html = '';

http.get(url, function(response){
	response.on('data', function(data){//触发data事件执行回调
		html += data;
	})
	response.on('end', function(){
		console.log(html);
	})
}).on('error', function(){
	console.log('获得数据出错');
})