//爬取html
//由于慕课网页面结构会改动，所以爬的结果不一定完整，写作日期:2016/12/26
var http = require('http');
var url = 'http://www.imooc.com/video/7965';
var html = '';
var cheerio = require('cheerio');//相当于JS中的JQ,文档：https://cnodejs.org/topic/5203a71844e76d216a727d2e

function filterHtml(html){
	var $ = cheerio.load(html);
	var chapters = $('.sec-title');

	// [{
	// 	chapterTitle:'',
	// 	videos:[
	// 		title:'',
	// 		id:''
	// 	]
	// }]
	var courseData = [];
	chapters.each(function(){
		var chapter = $(this);
		var chapterTitle = chapter.find('span').text();//每一大章的标题
		var videosTitle = chapter.parent().find('a');//用于获得每一大章下所有小章标题
		var videos = chapter.parent().find('a');//用于获得每一大章下所有小章链接（PS：虽然videoTitle和video一样，但用途不一样）
		var chapterData = {
			chapterTitle:chapterTitle,
			videos:[]
		}
		
		videosTitle.each(function(){
			var video = $(this);
			var title = video.text();
			chapterData.videos.push({
				title:title
			})
		})

		var arr = [];
		videos.each(function(){
			var video = $(this).attr('href');
			var id = video.split('/')[2];
			arr.push(id);
		})
		arr.forEach(function(item,index){
			chapterData.videos[index].id = item;
		})

		courseData.push(chapterData);
	});


	return courseData;
}

function printCourseInfo(courseData){
	courseData.forEach(function(item,index){
		var chapterTitle = item.chapterTitle;
		console.log(chapterTitle + '\n');

		item.videos.forEach(function(item,index){
			var title = item.title;
			var id = item.id;
			console.log('  【' + id + '】  ' + title + '\n');
		})
	})
}

http.get(url, function(response){
	response.on('data', function(data){//触发data事件执行回调
		html += data;
	})
	response.on('end', function(){
		var courseData = filterHtml(html);//格式化数据
		printCourseInfo(courseData);//打印数据
	})
}).on('error', function(){
	console.log('获得数据出错');
})