var express = require('express')
var app = express()
var mongo = require('mongodb');

app.use(express.static(__dirname + '/public'));

app.get('/', function (req, res) {
	var div = req.body.code;
	
	console.log(div);
})
app.post('/', function (req,res) {
	response = {
		test: req.body.code
	};
	console.log(response);
	res.end(JSON.stringify(response));
})

app.listen(3000, function () {
  console.log('Example app listening on port 3000!')
})


// Retrieve
var MongoClient = require('mongodb').MongoClient, assert = require('assert');

// Connect to the db

MongoClient.connect("mongodb://localhost:27017/exampleDb", function(err, db) {
  if(!err) {
    console.log("We are connected");
  }
	var collection = db.collection('test2');
  assert.equal(null, err);
  console.log("Connected successfully to server");

  db.close();
});
