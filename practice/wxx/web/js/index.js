$("#main_bar button").click(function(){
    var text = $(this).text();
    var tab_id = $(this).attr('id');
    $('div').removeClass('current');
    var class_name = $(this).attr('class');
    $('.'+tab_id).addClass('current');
});

/*
	$('ul.tabs li').click(function(){
				var tab_id = $(this).attr('data-tab');

				$('ul.tabs li').removeClass('current');
				$('.tab-content').removeClass('current');
				var old_id = $('.tab-content').attr('id');
				disable_image(old_id);

				$(this).addClass('current');
				$("#"+tab_id).addClass('current');				
				handle_tab(tab_id);
            })
            */