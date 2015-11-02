var casper = require('casper').create();
var urls = ['http://baidu.com/', 'http://www.qq.com/'];
var fs = require('fs');

casper.start().eachThen(urls, function(response) {
  data = response.data;
  this.wait(60000, function() {
      console.log(new Date().toLocaleTimeString())
      console.log('Opened', data);
   });
  // this.thenOpen(response.data, function(response) {
  //   console.log('Opened', response.url);
  // });
  // this.then(function (response) {
  //    var doc = this.evaluate(function() {
  // 			return document.body.innerHTML;
  // 		});
  // 	console.log(response.url);
  // 	//console.log(doc);
  // })

});

a = 'http://mp.weixin.qq.com/s?__biz=MjM5ODUzODk5NQ==&mid=202791673&idx=1&sn=f2c5463473be88f008de68c24e38384e&3rd=MzA3MDU4NTYzMw==&scene=6#rd';
//fs.write('a.txt', "aaaabbbbb", 'w+');
console.log(fs.read('./data/2015-11-1.txt').indexOf(a))
//casper.run();