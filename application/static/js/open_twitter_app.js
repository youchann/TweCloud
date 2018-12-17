// Twitterアプリの起動
$('.open_app').click(function(){
    var start = new Date().getTime();
    console.log('a');
    window.location.href = 'twitter://timeline';
    console.log('b');

    //時間が遅いと、アプリを所持していないと判断
    setTimeout(function() {
        var diff = new Date().getTime() - start;
        console.log('c');

        if (diff < 510) {
            window.location.href = 'https://twitter.com/?lang=ja';
        }
        console.log('d');
    }, 500);
});