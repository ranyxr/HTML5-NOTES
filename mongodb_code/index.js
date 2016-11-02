/*mongodb 创建索引*/
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

  //创建索引
  createIndex(db,function(){
    console.log("create index ok!");
  });
  //删除索引
  dropIndex(db,function(){
    console.log("drop index ok!");
  });

var indexNameGlobal;
//创建索引
var createIndex = function(db,callback){
  db.collection("first").createIndex({"name":1,"age":-1},{"unique":true},function(error,indexName){

    assert.equal(error,null)
    console.log(indexName);
    indexNameGlobal = indexName;
    callback();
  });
};

var dropIndex = function(db,callback){
  db.collection("first").dropIndex(indexNameGlobal,null,function(error,result){
      assert.equal(error,null);
      console.log(result);
      callback();
  });
};
