$.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    dataType: 'json'
}).done(function(data) {
    $('DIV#hello').text(data.hello);
});
