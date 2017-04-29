var mongoose = require('mongoose')
mongoose.Promise = require('bluebird')
var db = mongoose.createConnection('localhost', 'test')

db.on('error', console.error.bind(console, 'Error Connection'))

//Schema上可以定义公用的实例方法、静态方法、虚拟属性
var PS = new mongoose.Schema({
	name: String
})
PS.methods.speak = function(cb) { //实例方法要注意绑定model
	return this.model('Person').find({type:this.type},cb)
}
PS.statics.findByName = function(name, cb) { //模型方法不用绑定model
	this.find({name: new RegExp(name, 'i')}, cb)
}
PS.virtual('name.full').get(function() { //虚拟属性get
	return this.name.first + this.name.last
})
PS.virtual('name.full').set(function(name) { //虚拟属性set
	var split = name.split(' ')
	this.name.first = split[0]
	this.name.last = split[1]
})

//model上可以调用静态方法、新增数据
var PM = db.model('Person', PS)
// var PMC = {name: "AAA"}
// PM.create(PMC, function() {
// 	console.log('done')
// })
PM.update = function() {
	this.find().update({name: 'AAA'}, {$set:{name:'GGG'}}, {multi:true}, function(err, obj){
		console.log(obj)
	})
}

//entity上可以调用实例方法,还可以定义私用的各种方法，如增删改查
var PE = new PM({})
PE.findById = function(id) {
	this.model('Person').remove({_id: id})
}



// PE.name.full = 'Ko KoTa'

// PE.findById('58e50afe5b861826a4c034ef')

// PE.save()

PM.update()

db.close()