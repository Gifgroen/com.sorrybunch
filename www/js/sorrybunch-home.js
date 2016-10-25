$(function() {
	var pages = {
		"video": "VideoIII.png",
		"songs": "SongsII.png",
		"bio": "Bio.png",
		"newsandgigs": "Newsandgigs.png",
		"booker": "BookersNew.png",
		"contact": "Contact.png",
		"photos": "Photos.png"
	};

	$(".page").mouseover(function(event) {
		if($("#page-pointer").is(":hidden"))
			$("#page-pointer").show();

		var id = $(this).attr("id");
		var img = pages[id];
		$("#page-pointer").attr("src", "/images/" + img);
	});
});
