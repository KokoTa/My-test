var fs = require('fs');
var source = fs.readFileSync('../buffer/1.png');//同步读取，流专用
 
 fs.writeFileSync('stream_copy_image.png',source);