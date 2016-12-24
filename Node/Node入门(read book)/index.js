var server = require("./server");//请求服务器模块
var router = require("./router");//请求路由模块
var requestHandlers = require("./requestHandlers");//请求路由处理模块

var handle = {};//处理对象
handle["/"] = requestHandlers.start;
handle["/start"] = requestHandlers.start;
handle["/upload"] = requestHandlers.upload;
handle["/show"] = requestHandlers.show;

server.start(router.route,handle);