//运动框架
		function getStyle(obj,name){//获得某对象CSS中某样式的数据的函数，为了防止offset的Bug，必须酱紫做
			if(obj.currentStyle){//判断浏览器是否有这个属性
				return obj.currentStyle[name];//针对IE，获得obj的某属性值
			}else{
				return getComputedStyle(obj,false)[name];//针对其他浏览器
			}
		}
		function move(obj,name,target){//对象名，对象名中的某样式的值，目标值
			clearInterval(obj.timer);//防止Bug要先关闭定时器
			obj.timer = setInterval(function(){
				if(name=='opacity'){//判断要改变的样式是否为透明度(注意)
					var cur = Math.round(parseFloat(getStyle(obj,name)))*100;//透明值一开始是小数所以用parseFloat,但是由于计算机对小数取不到确切值，因此用Math.round取整，用来兼容各个浏览器
				}else{
					var cur = parseInt(getStyle(obj,name));//用一个变量储存获得的样式的数据，取整
				}
				
				var speed = (target-cur)/6;//套用运动框架
				speed=speed>0?Math.ceil(speed):Math.floor(speed);
				if(cur==target){
					clearInterval(obj.timer);
				}else{
					if(name=='opacity'){//判断要改变的样式是否为透明度
						obj.style.filter = 'alpha(opacity:'+(cur+speed)+')';
						obj.style.opacity = (cur +speed)/100;
					}else{
						obj.style[name] = cur +speed +'px';//注意这个[name]
					}
					
				}
			},30)
		}