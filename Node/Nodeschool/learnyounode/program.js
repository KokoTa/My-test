var fs = require('fs');
var name = process.argv[2];
var lines = fs.readFileSync(name).toString().split('\n').length-1;
console.log(lines);