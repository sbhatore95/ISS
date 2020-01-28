const http = require('http')

http.createServer((req, res)=>{
	if (req.url == '/') {
		res.end("Woohoo");
	}
}).listen(8080)