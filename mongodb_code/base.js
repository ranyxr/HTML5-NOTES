/*mongodb 的基本操作*/
var mongodb = require("mongodb");
//为了提示错误
var assert = require("assert");
//连接某台机器上的stu数据库
var dburl = "mongodb://192.168.1.247:27017/stu";
//连接数据库
mongodb.MongoClient.connect(dburl,function(error,db){
  //error,表示连接失败的错误
  //db，表示连接成功的数据库

  //当error == null时，不会提示错误，否则提示错误，并且程序立即结束
  assert.equal(error,null);
  console.log("db connect ok!");

  //所有与该数据库相关的操作都必须在该函数中添加

  //插入文档
  // insertOne(db,function(){
  //   console.log("insert one doc ok!");
  // });
  // insertMany(db,function(){
  //   console.log("insert many ok!");
  // });

  //删除文档
  // deleteOne(db,function(){
  //   console.log("delete one doc ok!");
  // });
  // deleteMany(db,function(){
  //   console.log("delete many docs ok!");
  // });

  // db.close();//关闭数据库

  //修改文档
  // updateOne(db,function(){
  //   console.log("update one doc ok!");
  // });
  // updateMany(db,function(){
  //   console.log("update many docs ok!");
  // });

  //查看文档
  findOne(db,function(){
    console.log("find one doc ok!");
  });
});

// 插入一条文档
// var insertOne = function(db,callback){
//   db.collection("first").insertOne({"name":"lisi","age":18},null,function(error,result){
//     assert.equal(error,null);
//     // console.log(result);
//     callback();
//   });
// };
// 添加多条文档
// var insertMany = function(db,callback){
//   db.collection("first").insertMany([{"name":"lisi","age":18},{"name":"zhangsan","age":20}],null,function(error,result){
//     assert.equal(error,null);
//     // console.log(result);
//     callback();
//   });
// };

//删除一条文档
// var deleteOne = function(db,callback){
//   db.collection("first").deleteOne({"age":18},null,function(error,result){
//     assert.equal(error,null);
//     callback();
//   });
// };
//删除多条文档
// var deleteMany = function(db,callback){
//   db.collection("first").deleteMany({"name":"zhangsan"},null,function(error,result){
//     assert.equal(error,null);
//     callback();
//   });
// };

//修改一条文档
// var updateOne = function(db,callback){
//   db.collection("first").updateOne({"name":"lisi"},{$set:{"age":30}},null,function(error,result){
//     assert.equal(error,null);
//     callback();
//   });
//修改多条文档
// var updateMany = function(db,callback){
//   db.collection("first").updateMany({"name":"lisi"},{$set:{"age":50}},null,function(error,result){
//     assert.equal(error,null);
//     callback();
//   });
// };

//查看一条文档
var findOne = function(db,callback){
  // var result = db.collection("first").find({"age":50});
  // var result = db.collection("first").find({$or:[{"name":"zhangsan"},{"age":{$lt:40}}]})
  var result = db.collection("first").find().sort({"age":1});
  result.toArray(function(error,docs){
    console.log(docs);
    db.close();
  });
};
