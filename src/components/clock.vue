<template>
	<div id="clockDiv">
    	<canvas ref="clock" id="myclock" width="500px" height="500px">您的浏览器不支持canvas,请升级您的浏览器。</canvas>
	</div>
</template>

<script type="text/javascript">
	export default{
		data(){
			return{

			}
		},
		mounted(){
			this.drawClock();
		},
		methods:{
			drawClock(){
				var canvas = this.$refs.clock;
	    		var ctx = canvas.getContext("2d");
	    		var that = this;
	    		requestAnimationFrame(function step() {
		            that.drawDial(ctx);  //画钟盘
		            that.drawAllHands(ctx);  //画指针
		            that.drawShaft(ctx);  //画针轴
		            requestAnimationFrame(step);
	        	})
			},
			drawDial(ctx) {
		        ctx.clearRect(0,0,500,500);  //清除画布内的所有元素
		        ctx.save();  //保存当前状态
		        ctx.translate(250,250); //移动坐标原点到画布的中心
		        ctx.lineWidth = 3;
		        ctx.strokeStyle = 'black';
		        ctx.beginPath();
		        ctx.arc(0,0,240,0,2*Math.PI); //画圆
		        ctx.stroke();
		        ctx.closePath();
		        //画刻度
		        for(let i = 0;i < 60;i++){
		            ctx.save();
		            ctx.rotate(-Math.PI / 2 + i * Math.PI / 30);
		            ctx.beginPath();
		            let startX = i % 5 ? 210 : 200;
		            ctx.moveTo(startX,0);
		            ctx.lineTo(230,0);
		            ctx.lineWidth = i % 5 ? 2 : 4;
		            ctx.stroke();
		            ctx.closePath();
		            ctx.restore();
		        }

		        //画数字
		        for(let i = 1;i <= 12;i++){
		            ctx.save();
		            let deg = -Math.PI / 2 + i * Math.PI / 6;
		            ctx.font = '40px Microsoft Yahei';
		            ctx.fillStyle = "black";
		            let x = 170 * Math.cos(deg) - 10;
		            if (i > 9)
		                x -= 12;
		            let y = 170 * Math.sin(deg) + 18;
		            ctx.fillText(i, x, y);
		            ctx.restore();
		        }
		        ctx.restore(); //把原点恢复到右上角
    		},
    		drawAllHands(ctx) {
    			let time = new Date();
        		let hour = time.getHours();
        		let minute = time.getMinutes();
        		let second = time.getSeconds();
		        let secondAngle = second / 60 * 2 * Math.PI;
		        let minuteAngle = minute / 60 * 2 * Math.PI + secondAngle / 60;
		        let hourAngle = hour / 12 * 2 * Math.PI + minuteAngle / 12;
		        this.drawHand(ctx, hourAngle, 100, 10, 8, "black");
		        this.drawHand(ctx, minuteAngle, 150, 10, 6, "black");
		        this.drawHand(ctx, secondAngle, 180, 20, 2, "red");
    		},
    		drawHand(ctx,angle,len,tailLen,width,color) {
			        ctx.save();
			        ctx.translate(250,250);
			        ctx.rotate(-Math.PI / 2 + angle);
			        ctx.lineWidth = width;
			        ctx.strokeStyle = color;
			        ctx.lineCap = "round";
			        ctx.beginPath();
			        ctx.moveTo(-tailLen, 0);
			        ctx.lineTo(len, 0);
			        ctx.stroke();
			        ctx.closePath();
			        ctx.restore();
    		},
    		drawShaft(ctx) {
		        ctx.save();
		        ctx.fillStyle = "rgb(80, 80, 80)";
		        ctx.beginPath();
		        ctx.arc(250, 250, 6, 0, 2 * Math.PI, false);
		        ctx.fill();

		        ctx.fillStyle = "rgb(180, 180, 180)";
		        ctx.beginPath();
		        ctx.arc(250, 250, 4, 0, 2 * Math.PI, false);
		        ctx.fill();

		        ctx.fillStyle = "rgb(0, 0, 0)";
		        ctx.beginPath();
		        ctx.arc(250, 250, 2, 0, 2 * Math.PI, false);
		        ctx.fill();

		        ctx.restore();
    		},
		}
	}
</script>

<style type="text/css">
	#myclock{
		zoom:30%;
	}
</style>