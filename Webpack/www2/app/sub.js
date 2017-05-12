// 使用babel后替换commonjs风格
// function generateText () {
// 	var element = document.createElement('h1')
// 	element.innerHTML = 'Hello World'
// 	return element
// }

// module.exports = generateText

export default function () {
	var element = document.createElement('h1')
	element.innerHTML = 'Hello World'
	return element
}