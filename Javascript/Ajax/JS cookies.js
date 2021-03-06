﻿<script type="text/javascript">
function getCookie(c_name)
{
	if (document.cookie.length>0) //如果cookie的值长度为零则执行下面的代码
	{
		c_start=document.cookie.indexOf(c_name + "=") //判断cookie的名字是否是指定的名字
		if (c_start!=-1) //如果不等于-1则表示名字为c_name的cookie是存在的
			{ 
				c_start=c_start + c_name.length+1 //获取指定cookie名字的值的起始位置
				c_end=document.cookie.indexOf(";",c_start) //获取指定cookie名字的值的结束位置，从开始位置开始取;号的位置，因为分号是分隔符

				if (c_end==-1) c_end=document.cookie.length //如果结束位置为-1则表示这个cookie是最后一个没有;所以取最长值
				return unescape(document.cookie.substring(c_start,c_end)) //返回解码后的cookie值
			} 
	}
	return "" //否则返回空值
}

function setCookie(c_name,value,expiredays) //设置cookie,指定cookie的名字(c_name),有效期(expiredays)
{
	var exdate=new Date()//设置有效期的初始值当前日期
	exdate.setDate(exdate.getDate()+expiredays) //设置过期的日期当前日期+有效时间长度
	document.cookie=c_name+ "=" +escape(value)+ //设置cookie的名称以及有效时间
	((expiredays==null) ? "" : ";expires="+exdate.toGMTString())
}

function checkCookie() //检查cookie是否存在，如果存在就提示cookie的值
{
	username=getCookie('username') //获取cookie的值
	if (username!=null && username!="") //如果username值不为空并且username不为null提示
		{alert('Welcome again '+username+'!')}
	else 
	{
		username=prompt('Please enter your name:',"") //否则提示重新输入用户名
		if (username!=null && username!="") //如果用户名不为空则不为null
		{
			setCookie('username',username,365) //设置cookie值
		}
	}
}
// 追问：
// 对于上面set cookie中的value，和expireddays具体是什么含义，还请这位大哥解释的再具体一些，谢谢
// 回答：
// set cookie中的value就是要给指定的cookie设置的值呀，expiredday含义是过期的时间单位
</scirpt>