/*
* TODO
* 
* Known bugs:
*  BUG1
*  - If the player pushes two perpendicular directions fast enough they will
*	 start going in the opposition direction which will kill them
*  
* General:
*  G1
*  - Implement a menu
*  
*/


var canvas;
var ctx;
var scr;

window.onload = function() {
	canvas = document.getElementById("snakeCanvas");
	scr = document.getElementById("score");
	ctx = canvas.getContext('2d');
	document.addEventListener("keydown", keypush);
	setInterval(update, 1000/15); // 1000ms, 15fps
	//menu();
}
//global variables
px=py=10; 	// player's current positions
dx=dy=0;  	// change in positions
grid=20;
ax=ay=15; 	// apple's initial position
trail = []; // snake's trail
tail = 3;	// snake length
score = 0;

moveFlag = true;

function update() {
	// Move player
	updatePlayer();
	
	// Draw (happens last)
	drawPlayer();
}

function keypush(evt) {
	// evt : key event, type integer
	if(moveFlag){
		switch (evt.keyCode){
			// top left corner 0,0 bottom right is 100,100
			/* 37: left
			   38: up
			   39: right 
			   40: down */
			case 37:
				if (dx == 1)
					break;
				else {
					dx = -1;
					dy = 0;
					break;
				}
			case 38:
				if (dy == 1)
					break;
				else {
					dx = 0;
					dy = -1;
					break;
				}
			case 39:
				if (dx == -1)
					break;
				else {
					dx = 1;
					dy = 0;
					break;
				}
			case 40:
				if (dy == -1)
					break;
				else {
					dx = 0;
					dy = 1;
					break;
				}
				
		}
	}
}

function updatePlayer()
{
	moveFlag = false;
	px += dx;
	py += dy;
	checkCollision();
	
	if (ax == px && ay == py) {
		tail++;
		score++;
		scr.innerHTML = "Score: " + score;
		spawnApple();
	}
	
	trail.push({x: px, y:py});
	while (trail.length > tail) {
		trail.shift();
	}
	
	moveFlag = true;
}

function drawPlayer() {
	ctx.fillStyle = 'black';
	ctx.fillRect(0, 0, canvas.width, canvas.height);
	
	ctx.fillStyle = 'lime';
	for (var i = 0; i < trail.length; i++) {
		ctx.fillRect(trail[i].x * grid, trail[i].y * grid, grid - 2, grid - 2);
	}
	ctx.fillRect(px * grid, py * grid, grid - 2, grid - 2);
	
	ctx.fillStyle = 'red';
	ctx.fillRect(ax * grid, ay * grid, grid - 2, grid - 2);
}

function spawnApple() {

	ax = Math.floor(Math.random() * grid);
	ay = Math.floor(Math.random() * grid);
	
	// this might not be needed
	if(ax == px && ay == py)
		spawnApple();
	else {
		for(var i = 0; i < trail.length; i++)
		{
			if(ax == trail[i].x && ay == trail[i].y)
				spawnApple();
		}
	}
}

function checkCollision() {
	if(px < 0 || px >= grid || py < 0 || py >= grid) {
		tail = 3;
		px=py=10;
		dx=dy=0;
		score = 0;
		scr.innerHTML = "Score: " + score;
	} else {
		for (var i = 0; i < trail.length; i++) {
			if(px == trail[i].x && py == trail[i].y) {
				tail = 3;
				px=py=10;
				dx=dy=0;
				score = 0;
				scr.innerHTML = "Score: " + score;
			}
		}
	}
}
