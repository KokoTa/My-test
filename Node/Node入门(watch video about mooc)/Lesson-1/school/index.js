var klass = require('./klass');

exports.add = function(klasses){//多个班级
	klasses.forEach(function(item,index){
		var _klass = item;
		var _teacherName = item.teacherName;
		var _students = item.students;
		klass.add(_teacherName,_students);
	})
}


//感觉像链式调用
//student
//			->	klass -> index
//teacher