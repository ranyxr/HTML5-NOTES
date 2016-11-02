var mongodb = require("mongodb");
var assert = require("assert");
var dburl = "mongodb://192.168.1.247:27017/stu";
mongodb.MongoClient.connect(dburl,function(error,db){
  assert.equal(error,null);
  console.log("connect ok!");

  // insertOne(db,function(){
  //   console.log("insert one doc ok!");
  // });

  // insertMany(db,function(){
  //   console.log("insert many docs ok!");
  // });

  // deleteOne(db,function(){
  //   console.log("delete one doc ok!");
  // });

  // deleteMany(db,function(){
  //   console.log("delete mang docs ok!");
  // });

  // updateOne(db,function(){
  //   console.log("update one doc ok!");
  // });

  // updateMany(db,function(){
  //   console.log("update many docs ok!");
  // });

  findOne(db,function(){
    console.log("find ok!");
  });
});

var insertOne = function(db,callback){
  db.collection("first").insertOne(
    {"name":"lisi","age":18},
    null,
    function(error,result){
      assert.equal(error,null);
      callback();
    });
};

var insertMany = function(db,callback){
  db.collection("first").insertMany(
    [{"name":"sdf","age":1},{"name":"qwe","age":3}],
    null,
    function(error,result){
      assert.equal(error,null);
      callback();
    }
  );
};

var deleteOne = function(db,callback){
  db.collection("first").deleteOne({"age":18},null,function(error,result){
    assert.equal(error,null);
    callback();
  });
};

var deleteMany = function(db,callback){
  db.collection("first").deleteMany({"name":"zhangsan"},null,function(error,result){
    assert.equal(error,null);
    callback();
  });
};

var updateOne = function(db,callback){
  db.collection("first").updateOne({"name":"sdf"},{$set:{"age":20}},null,function(error,result){
    assert.equal(error,null);
    callback();
  });
};

var updateMany = function(db,callback){
  db.collection("first").updateMany({"name":"zhangsan"},{$set:{"age":30}},null,function(error,result){
    assert.equal(error,null);
    callback();
  });
};

var findOne = function(db,callback){
  var result = db.collection("first").find().sort({"age":1});
  result.toArray(function(error,docs){
    console.log(docs);
    db.close();
  });
};
