//3.当前窗口首先调用init函数-在游戏的时候尽量不用init()的格式;
//window.onload = init;
window.onload= init;
//5.获取鼠标的坐标
window.onmousemove = MouseMove;
//键盘触发事件
window.onkeydown = KeyDownCode;
var context; //画布的画笔
var gamebg; //游戏背景
var board; //游戏挡板
var ball; //小球
//创建一个存放多个砖块的容器-数组
var Breakers = new Array();
var ballX = 300;
var ballY = 550;
var VX = 6;
var VY = -6;
//定义挡板初始化位置
var boardX = 0;
var boardY = 640;
var i = 0;
//当前画布的宽高
var CH = 768;
var CW = 1024;
var p_num;//得分标签
var number = 0;//默认得分
var terval;//计时器
//满分
var num1 = 0;
var mp3;


//1.游戏入口
function init() {
	
	Log("开始进入游戏。。。")
	//01.找到canvas - 档案柜
	var canvasgame = document.getElementById("CanvasGame");
	p_num = document.getElementById("number");
	mp3 = document.getElementById("mp3")
	//进入游戏得分未：0
	p_num.innerText="得分:0"
	//获取显示得分标签
	//02.获取到画笔 - 管理员
	context = canvasgame.getContext("2d");
	//03.创建一个容器用于存放图片-档案袋
	gamebg = AddImg("img/image/bg.png")
	board = AddImg("img/image/board.png");
	ball = AddImg("img/image/ball1.png");
	//创建多个砖块
	CreateBreakers();
	num1 = Breakers.length;
	//测试执行删除
//	Breakers.splice(4,2)

	//	var img = new Image();
	//	img.src = "img/image/bg.png";
	//	//04.画笔将图片对象绘制道画布上
	//	context.drawImage(img,0,0);
	//04.定时器刷新-第一个：要刷新的函数，第二个：刷新的频率
	terval = setInterval(GameTick, 1000 / 60);
}
//10创建多个砖块
function CreateBreakers() {
	for(var j = 0; j < 1; j++) {
		for(var i = 0; i < 9; i++) {
			var breaker = AddImg("img/image/" + 1 + ".png");
			//		breaker.x = 20+(192+6)*i;
			//		breaker.y = 80;
			Breakers.push({
				item: breaker,
				x: 20 + 102 * i,
				y: 90 + 36 * j
			});
		}
	}

}
//4.创建一个游戏界面刷新的函数 - 刷新的定时器
function GameTick() {
	Log("第" + (i++) + "次刷新。。。")
	//清空画布
	context.clearRect(0, 0, CW, CH);
	//绘制背景图片
	context.drawImage(gamebg, 0, 0);
	//绘制挡板
	context.drawImage(board, boardX, boardY)
	//更新砖块
	UpdateBreaker();
	//更新小球位置
	UpdateBall();
	//测试小球跟挡板的碰撞
	testBallAndBoard();
	//测试小球跟砖块的碰撞
	testBreakerAndBall();
}
function KeyDownCode(e){
	//左边 37
	if(e.keyCode == 65){
		boardX+=-100;
		
	}
	if(e.keyCode == 68){
		boardX+=100;
	}
	
}

function testBreakerAndBall(){
	//把每一个砖块提取出来 - 倒序
	for(var i = Breakers.length - 1;i>=0;i--){
		var breaker = Breakers[i];//{item:breaker,x:20+198*i,y:80}
		var hit = TestPoint(breaker.x,breaker.y,102,36,ballX+ball.width/2,ballY);
		if(hit){
			//播放一次
			mp3.play()
			number+=1;
			p_num.innerText = "得分:"+number;
			//得分；
			//删除被碰撞到的砖块
			Breakers.splice(i,1);
			if(number>=num1){
				Gameover();
				
			}
			//发生碰撞
			VY*=-1;
			break;
			
		}
		
	}
	
}
//
function UpdateBreaker() {
	for(var i = 0; i < Breakers.length; i++) {
		var item = Breakers[i]; //{item:breaker,x:20+198*i,y:80} = item
		context.drawImage(item.item, item.x, item.y)

	}
}
//9测试小球跟挡板的碰撞
function testBallAndBoard() {
	//检查碰撞结果 - 做视觉上的优化
	var hit = TestPoint(boardX - ball.width,
		boardY - ball.height,
		board.width + ball.width,
		board.height + ball.height,
		ballX, ballY);
	if(hit) {
		//小球发生碰撞之后的起始Y坐标等于 = 挡板的Y坐标
		ballY = boardY - ball.height;
		//证明发生了碰撞
		VY *= -1
	}

}

//8.函数 - 判断点与物体发生碰撞的满足条件
//障碍物：x1,y1,w1,h1,x2,y2
function TestPoint(x1, y1, w1, h1, x2, y2) {
	if(x2 >= x1 && x2 <= x1 + w1 && y2 >= y1 && y2 <= y1 + h1) {
		return true;
	} else {
		return false;
	}

}

//7.更新小球位置
function UpdateBall() {
	ballX += VX;
	ballY += VY;
	if(ballY <= 80) {
		VY *= -1;
	}
	if(ballY >= CH) {
		//游戏结束
		Gameover();
	}
	if(ballX >= CW - ball.width) {
		VX *= -1
	}
	if(ballX <= 0) {
		VX *= -1

	}
	context.drawImage(ball, ballX, ballY);

}
//6更新挡板的坐标位置 - 只负责更新挡板的坐标值
function MouseMove(e) {
	//鼠标的X坐标赋值挡板 e.screenX
	//减去挡板/2 解决鼠标位于挡板中的问题
	boardX = e.x - board.width / 2;
//	boardY = e.y - board.height/2;
	//不能让挡板超出屏幕
	if(e.x <= board.width / 2) {
		boardX = 0;
	}
	if(e.x >= CW - board.width / 2) {
		boardX = CW - board.width;
	}
}
//3.创建一个生产图片对象的函数

function AddImg(path) {
	var img = new Image();
	img.src = path;
	return img
}
//2.控制台的游戏进度输出 - 只负责再后台输出进度:msg 变量名
function Log(msg) {
	//后台控制台打印
	console.log(msg)
}
//游戏结束
function Gameover(){
	//停止计时器
	clearInterval(terval);
	//设置div显示
	document.getElementById("gameover").style.display = "block"
	var gamestart = document.getElementById("gamestart");
	//给按钮添加点击事件
	gamestart.onclick = function(){
		//重新加载游戏
		window.location.reload();
	}
//	gamestart.addEventListener("click",function(){
//		
//	})
	
}
