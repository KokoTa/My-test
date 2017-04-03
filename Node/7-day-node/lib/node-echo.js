var cache = {};
var path = require('path');
function xx(source, value){
	cache[path.normalize(source).replace(/\\/g, '/')] = value;
}

xx('foo//baz', 2);
console.log(cache);