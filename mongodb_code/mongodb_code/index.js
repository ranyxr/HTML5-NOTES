//引入mongodb的模块
var mongodb = require("mongodb");

//是为了提示错误
var assert = require("assert");

//表示连接某台机器上的stu数据库
var dburl = "mongodb://127.0.0.1:27017/stu";

//连接数据库操作
mongodb.MongoClient.connect(dburl, function(error, db) {
    //error, 表示的连接失败的错误
    //db, 表示连接成功的数据库

    //当error == null时，不会提示错误，否则提示错误，并且程序立即结束
    assert.equal(error, null);
    console.log("db connect ok!");

    createIndex(db, function() {
		console.log("createIndex Ok!")
	});


	
    setTimeout(function() {
        dropIndex(db, function() {
            console.log("dropIndex ok!");
        });
    }, 2000);
	
});


var indexNameGlobal;

var createIndex = function(db, callback) {
    db.collection("firstClass").createIndex({
            "name": 1,
            "age": -1
        }, {
            unique: true //表示name和age至少有一个不同, 如果都一样就会错误
        },
        function(error, indexName) {
            assert.equal(error, null);
            console.log(indexName); //name_1_age_-1, 创建的索引的名字
            indexNameGlobal = indexName;
            callback();

        });
};

var dropIndex = function(db, callback) {
	console.log("indexNameGlobal = ", indexNameGlobal);

    db.collection("firstClass").dropIndex(indexNameGlobal, null, function(error, result) {
        assert.equal(error, null);
        callback();
    });
};
