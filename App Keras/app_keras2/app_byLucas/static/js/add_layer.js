var foodList = [];

$(function(){
$(document).on('click','input[type=submit]',function(){
  $('#foods').append('<div><a href="#" id="1" class="item">X</a> ' + $('#addFood').val() + '</div>');
  var valor = $('#addFood').val();
  $(valor).push(foodList);
    console.log(foodList);

});
$(document).on('click','input[type=submit]',function(){
  $('#foods').append('<div><a href="#" class="item">X</a> ' + $('#addFood2').val() + '</div>');
});
$(document).on('click','input[type=submit]',function(){
  $('#foods').append('<div><a href="#" class="item">X</a> ' + $('#addFood3').val() + '</div>');
});
$(document).on('click','input[type=submit]',function(){
  $('#foods').append('<div><a href="#" class="item">X</a> ' + $('#rangeSuccess').val() + '</div>');
});
$(document).on('click','.item',function(){
  $(this).parent().remove();
    });
});

console.log(foodList);
