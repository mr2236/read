$('a#ordenacao').click(function () {  
    $(this).addClass('active');
    $('a#reset').removeClass('active');
    var $divs = $(".row-artigo");
    
     var ordenadoDiv = $divs.sort(function (a, b) {
         //console.log($(a).html());
         console.log($(a).find('.qtd-voto').text());
         return $(a).find('.qtd-voto').text() < $(b).find('.qtd-voto').text();
     });
     $("#container-artigos").html(ordenadoDiv);  
     //console.log(ordenadoDiv);   
     $(".row-artigo").wrapAll($('<div class="article-post">'));    
    
});

$('a#reset').click(function () {    
    
    $(this).addClass('active');
    $('a#ordenacao').removeClass('active');
    var $divs = $(".row-artigo");    
      var ordenadoDiv = $divs.sort(function (a, b) {
          //console.log($(a).html());
          console.log($(a).find('.artigo').data('artigo'));
          return $(a).find('.artigo').data('artigo') > $(b).find('.artigo').data('artigo');
      });
      $("#container-artigos").html(ordenadoDiv);      
      $(".row-artigo").wrapAll($('<div class="article-post">'));    
    
});

