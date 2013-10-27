$('.js-captcha-refresh').click(function(){
    alert($form)
    $form = $(this).parents('form');
    $.getJSON($(this).data('url'), {}, function(json) { });
    return false;
});
