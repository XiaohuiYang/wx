var names = ['36Kr股权投资', '优投网', '高新园区金融平台', '天使汇', '中关村创业大街',  '真格基金', '无界空间','清华校友tmt协会',  '国银基金', '清创孵化器', '创伙伴', 'IC咖啡']
var _url = "http://weixin.sogou.com/weixin?type=1&query="
var fs = require('fs');

// var host = "http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&"

var old = fs.read('./data/all.txt');
var rels = [];
var casper = require('casper').create();

casper.start().eachThen(names, function(response) {
	data = response.data;
	this.wait(600, function() {
	 	console.log(_url + data);
	 	console.log(new Date().toLocaleTimeString())
 		crawler(_url + data);
 		console.log('cccccccc');	
	});
});

casper.run();

//crawler(_url + 'aia585'); 

function crawler(url) {
	// var link;
	casper.on('step.error', function(err) {
		console.log('aaaaaa');
	    console.log(err);
	});
	casper.open(url);
	casper.then(function() {
		this.evaluate(function () {
		    [].forEach.call(__utils__.findAll('a'), function(link) {
		        link.removeAttribute('target');
		    });
		});
		this.echo(this.getTitle()); // "Google" 
		this.click('div.wx-rb.bg-blue.wx-rb_v1._item');	
	});

	casper.waitFor(function check() {
	    return this.evaluate(function() {
	        return document.querySelectorAll('a.news_lst_tab.zhz').length > 8;
	    });
	});

	casper.then(function() {
		link = this.getCurrentUrl();
	    console.log('clicked ok, new location is ' + link);
	    this.echo(this.getTitle()); // "Google"
	});

	casper.then(function() {
		check(this, this.getCurrentUrl(), 2);
	})
}



function check(casper, url, i) {
	//console.log(casper);
	//console.log(url + "    " + i);
	//var casper = require('casper').create();
	//

	casper.open(url);

	if (i/2 >= 10) {
		handle();
		//casper.exit();
		return;
	}

	casper.waitFor(function check() {
	    return this.evaluate(function() {
	        return document.querySelectorAll('a.news_lst_tab.zhz').length > 8;
	    });
	});

	casper.then(function() {
		this.evaluate(function () {
		    [].forEach.call(__utils__.findAll('a'), function(link) {
		        link.removeAttribute('target');
		    });
		});
		this.click('div.wx-rb.wx-rb3:nth-child(' +i+ ') a' );
	});

	casper.then(function(){
		this.echo(this.getCurrentUrl() + '     ' + i);
		rels.push(this.getCurrentUrl());
	});

	casper.then(function() {
		check(this, url, i+2);
	});
}


function handle() {
	var currentTime = new Date();
	var month = currentTime.getMonth() + 1;
	var day = currentTime.getDate();
	var year = currentTime.getFullYear();
	var myfile = "./data/"+year + "-" + month + "-" + day+".txt";
	console.log(rels);
	tmp = [];
	for (i=0; i<rels.length; i++) {
		if (old.indexOf(rels[i]) == -1) {
			tmp.push(rels[i]);
		}
	}
	fs.write(myfile, tmp, 'w+');
	fs.write('./data/all.txt', tmp, 'w+');
}