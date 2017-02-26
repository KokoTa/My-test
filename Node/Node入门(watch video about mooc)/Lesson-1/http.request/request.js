//自动评论功能(慎用)
var http = require('http');
var querystring = require('querystring');

var postData = querystring.stringify({//数据序列化后发送
	'content':'总结：老师的课程让我受益良多！',
	'mid':8837
});

var options = {
	hostname: 'www.imooc.com',
	port:80,
	path:'/course/docomment',
	method:'POST',
	headers:{
		'Accept':'application/json, text/javascript, */*; q=0.01',
		'Accept-Encoding':'gzip, deflate',
		'Accept-Language':'zh-CN,zh;q=0.8',
		'Connection':'keep-alive',
		'Content-Length': postData.length,
		'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'Cookie':'loginstate=1; apsid=ViOTYwMTc2MDdiMjhhYzI3NWYyMGRmNzJkM2I3ZWEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMjE3MDY3NwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA1ODQ4NDc1MTRAcXEuY29tAAAAAAAAAAAAAAAAAAAAAGQyMTRjOWQyZDliMmI4YmYwYTQ0ZmZlMDZlNmIzODkzXXtPWF17T1g%3DYj; last_login_username=584847514%40qq.com; imooc_uuid=c865ed19-c7a9-4ae3-8304-08328910c62e; imooc_isnew_ct=1481782971; PHPSESSID=mm96i3s0npkk1lpp9ig6k87o54; jwplayer.qualityLabel=é«æ¸; jwplayer.volume=100; IMCDNS=0; Hm_lvt_f0cfcccd7b1393990c78efdeebff3968=1482250524,1482548535,1482626825,1482712016; Hm_lpvt_f0cfcccd7b1393990c78efdeebff3968=1482737253; imooc_isnew=2; cvde=5860634328199-29',
		'Host':'www.imooc.com',
		'Origin':'http://www.imooc.com',
		'Referer':'http://www.imooc.com/video/8837/0',
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
		'X-Requested-With':'XMLHttpRequest'
	}
}

var request = http.request(options, function(response){
	console.log('Status: ' + response.statusCode);
	console.log('headers: ' + JSON.stringify(response.headers));

	response.on('data',function(chunk){
		console.log(Buffer.isBuffer(chunk));
		console.log(typeof chunk);
	})

	response.on('end', function(){
		console.log('评论完毕');
	})
})

request.on('error', function(e){
	console.log('Error:' + e.message);
})
request.write(postData);//对请求添加数据
request.end();//结束请求