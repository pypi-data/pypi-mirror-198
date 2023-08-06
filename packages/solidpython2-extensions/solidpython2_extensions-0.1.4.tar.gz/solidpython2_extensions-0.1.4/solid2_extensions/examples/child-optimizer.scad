



module wrapperModule0() {
union() {
	difference() {
		children(3);
		union() {
			circle(r = 5);
			children(2);
			children(2);
			children(0);
			children(1);
		}
	}
	translate(v = [10, 0, 0]) {
		children(3);
	}
}
}
module wrapperModule1() {
wrapperModule0(){children(0);children(1);children(2);union() {
	children(0);
	children(1);
}
}}
module wrapperModule2() {
wrapperModule1(){children(0);children(1);cube(size = 2);
}}
module wrapperModule3() {
wrapperModule2(){children(0);sphere(r = 2);
}}
module wrapperModule4() {
wrapperModule3(){cube(size = 1);
}}
wrapperModule4(){};
