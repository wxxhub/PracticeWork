
$("div").hover(function(){
	var index = $("body").index();
	for (index==0) {
		index+=1;
		$("body")[index].Style().background = "red"
		if(index/2>=1){
			$("div")[index].Style().background = "#FF00FF"
		if(index/2>=1){
		}
		
	}
	
})