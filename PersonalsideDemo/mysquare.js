var x;
var keepGoing=true;
var D=1;
function setup(){
	createCanvas(600,600);
	 x=25;
	 y=25;
}

function draw(){
	background(0);
	rectMode(CENTER);
	fill(255,255,255);
	rect(50,100,600,50);
//function draw(){
	//background(0);
	rectMode(CENTER);
	rect(400,200,400,50);
	fill(255,255,255);
	rectMode(CENTER);
	rect(50,300,300,50);
	fill(255,255,255);
	rectMode(CENTER);
	rect(400,400,400,50);
	fill(255,255,255);
	rectMode(CENTER);
	fill(255,0,0);
	rect(50,600,100,50);
	ellipse(x,y,50,50);
	if x=x+25;
	y=y+25;
	


	//x += D;
	//if (x>width/2 && keepGoing){
		//myButton=document.createElement("Button");
		//myButton.textContent="Change Direction!";
		//$("body").append(myButton);
		//keepGoing=false;
		//function changeIt(){
		//	D=-1*D
		//}
		//$("Button").click(changeIt)
	//}
}