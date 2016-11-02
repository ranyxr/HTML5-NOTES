/* mongodb 的基本操作*/

//引入mongodb的模块
var mongodb = require("mongodb");

//是为了提示错误
var assert = require("assert");

//表示连接某台机器上的stu数据库
var dburl = "mongodb://127.0.0.1:27017/stu";

//连接数据库操作
mongodb.MongoClient.connect(dburl, function(error, db){
  //error, 表示的连接失败的错误
  //db, 表示连接成功的数据库

  //当error == null时，不会提示错误，否则提示错误，并且程序立即结束
  assert.equal(error, null);
  console.log("db connect ok!");

  //所有与该数据库相关的操作都必须在该函数中添加。
  //插入文档
  /*
  insertDoc(db, function(){
    console.log("insert one doc ok!");
  });

  insertMany(db, function(){
    console.log("insert Many doc ok!");
  });
  */


  //删除文档操作
  /*
  deleteOne(db, function(){
    console.log("delete one ok!");
  });

  deleteMany(db, function(){
    console.log("delete Many ok!");
  });
  */


  //更新操作
  /*
  updateOne(db, function(){
    console.log("update One ok!");
  });

  updateMany(db, function(){
    console.log("update Many ok!");
  });
  */


  //查询操作
  find(db, function(){console.log("find ok!")});


  // db.close();
});




//插入一条文档
var insertDoc = function(db, callback){
   db.collection("firstClass").insertOne({"name": "lisi", "age": 18}, null, function(error,result){
     assert.equal(error, null);
    //  console.log(result);
     callback();
   });
};


//插入多条文档
var insertMany = function(db, callback){
   db.collection("firstClass").insertMany([{"name": "li", "age": 18}, {"name":"zhangsan", "age": 20}],
      null, function(error,result){
     assert.equal(error, null);
     callback();
   });
};


//删除一条文档
var deleteOne = function(db, callback){
  db.collection("firstClass").deleteOne({"age": 18}, null, function(error, result){
     assert.equal(error, null);
     callback();
  });
};

var deleteMany = function(db, callback){
  db.collection("firstClass").deleteMany({"age": 18}, null, function(error, result){
     assert.equal(error, null);
     callback();
  });
};

var updateOne = function(db, callback){
  db.collection("firstClass").updateOne({"name": "zhaoliu"}, { $set: {"age": 30}}, null, function(error, result){
     assert.equal(error, null);
     callback();
  });
};

var updateMany = function(db, callback){
  // db.collection("firstClass").updateMany({"name": "zhaoliu"}, { $set: {"age": 30}}, null, function(error, result){
  db.collection("firstClass").updateMany({"name": "lili"}, {$pushAll:{"class": ["three", "four"]}}, null, function(error, result){
     assert.equal(error, null);
     callback();
  });
};


var find = function(db, callback){
  // var result = db.collection("firstClass").find({"name":"lili", "age": 10});
  //var result = db.collection("firstClass").find({$or:[{"name":"zhaoliu"},{"age" :{$gt: 20}}]});
  var result = db.collection("firstClass").find({$or:[{"name":"zhaoliu"},{"age" :{$gt: 20}}]}).sort({"age": 1});
  result.toArray(function(error, docs){
    console.log(docs);
    db.close();
  });
}
