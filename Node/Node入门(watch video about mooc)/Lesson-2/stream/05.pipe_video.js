var fs = require('fs');

fs.createReadStream('1.mp4').pipe(fs.createWriteStream('1-pipe.mp4'));//用pipe可以省很多步骤，如果不想监听读取过程的话
//读取->放buffer里->pipe连接->消费数据