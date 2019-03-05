/*
$("#main_bar button").click(function(){
    var text = $(this).text();
	var tab_id = $(this).attr('id');
	var class_name = $(this).attr('class');
	// $("."+tab_id).fadeOut(500);
	
	$(this).toggleClass('active');

	$('div').removeClass('current');
	$('.'+tab_id).addClass('current');
	// $('.'+tab_id).fadeIn(500);
});
*/

// var flag = null;
// var t = 0;


function test(panel){
	panel.style.display = "inherit";
	panel.style.marginLeft = "5%";
}

function sleep(){

}

function changePanel(panel_id){
	// alert("前端贼麻烦");
	for (i = 1; i<= 4; i++){
		var now_panel = "panel"+i;
		var old_panel = document.getElementById(now_panel);
		if  (old_panel.style.display != "none"){
			if (now_panel == panel_id){
				return;
			}
			old_panel.style.marginLeft = "100%";
			old_panel.style.display = "none";
			break;
		}
	}
	
	var panel = document.getElementById(panel_id);
	setTimeout(test, 500, panel);
}