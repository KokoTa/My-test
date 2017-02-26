function eat(food){
	if(typeof food === 'string'){
		return food + ' tasted really good.';
	}else{
		return 'error';
	}
}
console.log(eat('bananas'));