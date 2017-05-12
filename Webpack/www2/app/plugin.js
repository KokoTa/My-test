// 建立一个Jquery插件， 然而直接引入它会报错， 使用imports-lader解决问题
// 也可以使用 webpack.ProvidePlugin 解决问题, 这里我们使用方法一
// 自制颜色插件
(function ($) {
	const shade = '#556b2f'
	$.fn.greenify = function () {
		this.css('color', shade)
		return this
	}
})(jQuery)