function check(url, i) {
	var casper = require('casper').create();
	casper.start(url);

	casper.waitFor(function check() {
	    return this.evaluate(function() {
	        return document.querySelectorAll('a.news_lst_tab.zhz').length > 9;
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
		console.log(this.getCurrentUrl());
	});

	casper.run() ;
}

check('http://weixin.sogou.com/gzh?openid=oIWsFt51HfKbQF6u7mC89FBMz0IQ&ext=Uc8g8yaxQpHQZ9O6rEp3ubAAp9WimWJUcI5IuVvkwtPqf8cOSyB-UewERTT_p8I5', 18);