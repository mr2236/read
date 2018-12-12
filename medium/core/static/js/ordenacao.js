
$("a#ordenacao").on("click",(function(e){    

    
  
    $(this).addClass('active');
    $('a#reset').removeClass('active');
    var $divs = $(".row-artigo");
    
     var ordenadoDiv = $divs.sort(function (a, b) {                
         return $(b).find('.qtd-voto').text() - $(a).find('.qtd-voto').text();
     });
     
     $("#container-artigos").html(ordenadoDiv);       
     $(".row-artigo").wrapAll($('<div class="article-post">'));    
    
}));


$("a#reset").on("click",(function(e){   
    $(this).addClass('active');
    $('a#ordenacao').removeClass('active');
    var $divs = $(".row-artigo");    
      var ordenadoDiv = $divs.sort(function (a, b) {          
          return $(a).find('.artigo').data('artigo') - $(b).find('.artigo').data('artigo');
      });
      $("#container-artigos").html(ordenadoDiv);      
      $(".row-artigo").wrapAll($('<div class="article-post">'));  
}));


