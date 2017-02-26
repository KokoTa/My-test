//事件模块
var EventEmitter = require('events').EventEmitter;

var life = new EventEmitter();

life.setMaxListeners(11);//一个事件的监听器不要超过十个,可以设置上限

//Or addEventListner
life.on('event1',function(who){
	console.log('给'+who+'抱抱1');
})
life.on('event1',function(who){
	console.log('给'+who+'抱抱2');
})
life.on('event1',function(who){
	console.log('给'+who+'抱抱3');
})
life.on('event1',function(who){
	console.log('给'+who+'抱抱4');
})
life.on('event1',function(who){
	console.log('给'+who+'抱抱5');
})
life.on('event1',function(who){
	console.log('给'+who+'抱抱6');
})
life.on('event1',function(who){
	console.log('给'+who+'抱抱7');
})
life.on('event1',function(who){
	console.log('给'+who+'抱抱8');
})
life.on('event1',function(who){
	console.log('给'+who+'抱抱9');
})
life.on('event1',function(who){
	console.log('给'+who+'抱抱10');
})
life.on('event1',foo);
function foo(who){
	console.log('给'+who+'抱抱11');
}

life.removeListener('event1',foo);//移除某事件的单个监听器要传具名函数,匿名函数无效
//life.removeAllListeners('event1');//移除某事件的所有监听器

var hasListener1 = life.emit('event1','我');//调用事件并传参，hasListener1为true
var hasListener2 = life.emit('event2','你');//没有对应监听器，hasListener1返回false



//console.log(hasListener1,hasListener2);
//console.log(life.listeners('event1').length);//某事件的监听器数量
//console.log(EventEmitter.listenerCount(life,'event1'));//同上