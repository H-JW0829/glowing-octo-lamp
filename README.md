# Vue+Flask+mysql打造前后端分离的个人博客
基于Vue cli3和flask搭建的个人博客项目，前后端分离，使用axios进行前后端的通信，还运用了vuex、element-ui等，主要实现了登录注册、首页博客展示、添加博客、个人博客、我的收藏、添加评论、删除博客等模块，是一个小型项目

功能：<br/>
①用户管理，登录注册，前端传输时对密码的md5加密<br/>
②首页博客展示，时钟展示<br/>
③添加博客<br/>
④添加博客评论（新增用户头像和图片的懒加载）<br/>
⑤收藏博客<br/>
⑥进入个人中心页面，查看个人发表的博客以及收藏的博客，对这些博客进行编辑删除处理等<br/>

前端代码在src文件夹下<br/>
后端代码在flask文件夹下，使用蓝图进行管理<br/>
数据库是mysql<br/>

部分页面截图：
①首页
![image](https://github.com/H-JW0829/glowing-octo-lamp/blob/master/ImageForReadMe/zzz.png)
②登陆页面
![image](https://github.com/H-JW0829/glowing-octo-lamp/blob/master/ImageForReadMe/blog2.png)
③添加评论
![image](https://github.com/H-JW0829/glowing-octo-lamp/blob/master/ImageForReadMe/blog3.png)
④添加博客
![image](https://github.com/H-JW0829/glowing-octo-lamp/blob/master/ImageForReadMe/blog4.png)
⑤我的博客
![image](https://github.com/H-JW0829/glowing-octo-lamp/blob/master/ImageForReadMe/blog5.png)
⑥我的收藏
![image](https://github.com/H-JW0829/glowing-octo-lamp/blob/master/ImageForReadMe/blog6.png)
