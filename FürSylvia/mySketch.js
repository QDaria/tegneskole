function setup() {
	simple();
	colorMode(HSB);
	createCanvas(800, 600, WEBGL);
	//noStroke();
	strokeWeight(0.5);
	
	loop();
}

function draw() {
	
	background(0, 0, 100);
	
	rotateY(frameCount);
	
	for (var R = 40; R<=200; R+= 40) {
		
		fill(R*2, 80, 80, 0.4);
		stroke(R*2, 80, 80, 0.8);
	
		beginShape();
		for (var a=0; a<180; a+=2){

			var n = 0.8 + (0.4 * noise(R+a));
			var b = (10*a);

			var x = n * R * sin(a) * cos(b);
			var y = n * R * sin(a) * sin(b);
			var z = R * cos(a);
			curveVertex(x, y, z);
		}
		endShape(CLOSE);
	
	}
}