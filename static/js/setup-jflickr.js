$(document).ready(function(){
	$('#cbox').jflickrfeed({
		limit: 16,
		qstrings: {
			id: '71171395@N03'
		},
		itemTemplate: '<li>'+
						'<a rel="colorbox" href="{{image}}" title="{{title}}">' +
							'<img src="{{image_s}}" alt="{{title}}" />' +
						'</a>' +
					  '</li>'
	}, function(data) {
		$('#cbox a').lightBox();
	});
});
