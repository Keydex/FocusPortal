var express = require('express');
var app = express();

app.use(express.static(__dirname + '/public'));
var port = process.env.PORT || 3000;
console.log("Client running on port " + port);
app.listen(port);
