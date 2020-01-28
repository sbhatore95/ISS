function baz(bar) {
	console.log("This is baz");
	console.log("Now we will call argument function");
	bar();
}

function foo() {
	console.log("This is foo function");
}

var x = foo;
baz(x);
// function foobar() {
// 	var x = 5;
// 	if (x > 3) {
// 		let y = 3;
// 		x ++;
// 		console.log(x,y)
// 	}
// 	console.log(x);
// 	console.log(y)
// }
// // console.log(x)
// foobar()