var promise = new Promise( (res, rej) => {
	a = "Neel";
	try {
		l = a.length()
		res(l)
	} catch (err) {
		rej(err)
	}

});

promise.then((val)=>{
	console.log("Sucess " + val);
}).catch((err)=>{
	console.log("Got error " + err)
})
