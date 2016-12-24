function Ajax(url,fnSucc,fnFaild){
	if(window.XMLHttpRequest){//加了window表示XML...是一个属性，出错时不会报错，给出的是undefind，undefind=false，如果不加window的话会报错
				var ajax = new XMLHttpRequest();
			}else{
				var ajax = new ActiveXObject("Microsoft.XMLHTTP");
			}
			//2.连接服务器
			//open(方法（GET/POST),连接的文件路径，是否异步传输） 异步传输————》可以同时做很多事情  同步传输————》只能一件一件按顺序做
			ajax.open("GET",url+'?t='+new Date().getTime(),true);//这里“?t=当前时间毫秒数”的作用是让a.txt进行刷新，即清除缓存，否则数据无法及时获得更新
			//3.发送请求
			ajax.send();
			//4.接受返回
			ajax.onreadystatechange = function(){
				if(ajax.readyState == 4){//浏览器和服务器匹配进行到哪一步了,4表示完成，但完成不等于成功，因为如果open中的文件不存在也会显示完成，因此还要加以判断
					if(ajax.status == 200){//status用来判断是否成功，200为成功，失败为404
						fnSucc(ajax.responseText);//设置一个函数，这个函数的参数返回路径中的文本
					}else{
						fnFaild(ajax.status);//设置一个函数，这个函数的参数返回错误代码，如：404
					}

				}
			}
}