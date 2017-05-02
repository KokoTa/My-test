var net = require('net');
var server = net.createServer(function(connection) {  // 创建服务器
   console.log('client connected');
   connection.on('end', function() { // 断开连接
      console.log('客户端关闭连接');
   });
   connection.write('Hello World!\r\n');
   connection.pipe(connection); // 在Windows系统上，本地域用具名管道实现。 连接客户端
});
server.listen(3000, function() { 
  console.log('server is listening');
});