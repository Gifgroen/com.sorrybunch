$(function() {
	$("#jquery_jplayer_1").jPlayer({
		ready: function () {
			$(this).jPlayer("setMedia", {
				m4a: "http://www.jplayer.org/audio/m4a/Miaow-07-Bubble.m4a",
				oga: "http://www.jplayer.org/audio/ogg/Miaow-07-Bubble.ogg"
			});
			// Set the title
			$('#jp_playlist_1 li').text("Bubble");
		},
		swfPath: "/content/flash",
		supplied: "m4a, oga"
	});
});
