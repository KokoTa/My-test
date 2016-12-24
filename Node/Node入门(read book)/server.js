

var http = require("http");//取得node的http模块
var url = require("url");//取得node的url模块

function start(route,handle){//建立服务器的模块 // 传递路由

	function onRequest(request, response) {
		var pathname = url.parse(request.url).pathname;//浏览器请求的URL路径
		var postData = "";
		console.log("Request " + pathname + " received.");

		route(handle, pathname, response, request);
	}

	http.createServer(onRequest).listen(8888);
	console.log("Server has started.");
}

exports.start = start;//输出模块

