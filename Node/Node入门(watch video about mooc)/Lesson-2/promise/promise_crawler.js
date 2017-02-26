//爬取html,promise重构
var http = require('http');
var Promise = require('bluebird');//新版node已经集成promise
var baseUrl = 'http://www.imooc.com/learn/';
var cheerio = require('cheerio');//相当于JS中的JQ,文档：https://cnodejs.org/topic/5203a71844e76d216a727d2e
var videoIds = [728,637];

function getPageAsync(url){
	var html = '';	
	return new Promise(function(resolve,reject){
		console.log('正在爬取' + url);

		http.get(url, function(response){
			response.on('data', function(data){//触发data事件执行回调
				html += data;
			})
			response.on('end', function(){
				resolve(html);//回调then中的函数
			})
		}).on('error', function(e){
			reject(e);
		});

	});
}

var fetchCourseArray = [];//Promise对象的数组
videoIds.forEach(function(id){//每个id对应不同课程
	fetchCourseArray.push(getPageAsync(baseUrl + id));
});
Promise
	.all(fetchCourseArray)//类似于foreach,处理Promise对象数组,即then中的回调作用于所有Promise对象
	.then(function(pages){//pages对应一张网页，即一个Promise对象
		var pagesData = [];

		pages.forEach(function(html){
			var page = filterHtml(html);

			pagesData.push(page);

		});
		
		printPagesInfo(pagesData);

	});


function filterHtml(html){
	var $ = cheerio.load(html);
	var chapters = $('.chapter');
	var title = $('.hd h2').text();
	var number =  $('.js-learn-num').text();//ajax数据 爬不到

	// courseData = {
	// 	title: title, 课程标题
	// 	number: number, 学习人数
	// 	videos: [{		该页面下的所有视频信息
	// 		chapterTitle:'',	章节
	// 		videos:[{			章节下的视频信息
	// 			title:'',		标题
	// 			id:''			ID
	// 		}]
	// 	}]
	// };
	
	var courseData = {
		title: title,
		number: number,
		videos: []
	};

	chapters.each(function(index,item){
		var chapter = $(item);
		var chapterTitle = chapter.find('strong').text().replace(/^\s+/g,'').replace(/\s+$/g,'').split(/\s{3,}/)[0];//叫你不弄个元素包起来！
		var videos = chapter.find('ul').find('li');
		var chapterData = {
			chapterTitle:chapterTitle,
			videos:[]
		}

		videos.each(function(){
			var video = $(this);
			var title = video.find('.J-media-item').text().replace(/\s+/g,'');
			var id = video.attr('data-media-id');
			var item = {};
			item.title = title;
			item.id = id;
			chapterData.videos.push(item);
		})

		courseData.videos.push(chapterData);
	});

	return courseData;
}

function printPagesInfo(pagesData){
	pagesData.forEach(function(onepage){
		console.log('###  ' + onepage.number + ' 人学过 ' + onepage.title + '\n');
		onepage.videos.forEach(function(chapter){
			console.log('##  ' + chapter.chapterTitle + '\n');
			chapter.videos.forEach(function(video){
				console.log('【' + video.id +'】' + video.title + '\n');
			})
		});
	});
}
