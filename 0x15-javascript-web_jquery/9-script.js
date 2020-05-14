const givenUrl = 'https://fourtonfish.com/hellosalut/?lang=fr';
$.get(givenUrl, function (data) {
  $('DIV#hello').text(data.hello);
});
