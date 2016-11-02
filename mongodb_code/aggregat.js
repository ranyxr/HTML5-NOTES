/*mongodb 聚合相关*/
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

  aggregate(db,function(){
    console.log("aggredate ok!");
    db.close();
  });
});

//aggregate 第二个可选参数要么填写内容，要么不写，不可以写null
var aggregate = function(db,callback){
  db.collection("first").aggregate(
    [
      {
        $group:{
          _id:"$name",
          count:{
            // $sum:1
            // $sum:"$age"
            $avg:"$age"
          }
        }
      }
    ],function(error,result){
    assert.equal(error,null);
    console.log(result);
    callback();
  });
};
