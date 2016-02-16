$(document).ready(function(){
	$('#myCarousel').carousel({
        interval: 2000
    });
    $('.row.small img.img-polaroid').click(function(){
    	furnitureID = $(this).attr('data-id');
    	$.ajax({
            type: "GET",
            url: "/detail/"+furnitureID+"/",
        }).done(function( msg ) {
           //$(".overlay").show();
           if($("#myModal")){
               $("#myModal").remove();
           }
           $('body').append(msg);
           //$(".overlay").show();
           $('#myModal').modal('show');
        });
    	
    });
    
    $('.overlay .close').click(function(){
    	$('.overlay').hide();
    });
    
    $('.nav.catagory a').click(function(){
    	
    	if($(this).parent().attr('class') != 'active'){
    		$catagory = $('.nav.catagory li.active a').attr('cata');
    		$('div.'+$catagory).hide();
    		$('.nav.catagory li').removeClass('active');
    		$(this).parent().addClass('active');
    		$('div.'+$(this).attr('cata')).show();
    	}else{
    		
    	}
    });
    
});
