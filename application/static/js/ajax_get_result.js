$(function() {
    var oauth_data = JSON.stringify({"oauth_token":getParam("oauth_token"),
                                     "oauth_verifier":getParam("oauth_verifier")});

    $.ajax({
        type: "POST",
        url: "analyze",
        contentType:"application/json",
        data: oauth_data,
    })
    .then(
        // 1つめは通信成功時のコールバック
        function (data) {
            if (data !== 'error'){
                var file_name = JSON.parse(data.ResultSet).file_name;
                $(".change_head").children().remove();
                $(".cloud").children().remove();
                $(".change_head").append('<h2>これがあなたのクモです！</h2>');
                $(".cloud").append('<img id="img_cloud" src="static/clouds/' + file_name + '">');
                $("#share_area").css("display","block");
            } else {
                $(".change_head").children().remove();
                $(".cloud").children().remove();
                $(".change_head").append('<p>エラー</p>');                
                $(".change_head").append('<p><a href="/">トップに戻る</a></p>');                
            }
        },
        // 2つめは通信失敗時のコールバック
        function () {
            $("#loading").remove(); //loading画面の削除
            $(".result_image").append('<p>エラー</p>');                
            $(".result_image").append('<p><a href="/">トップに戻る</a></p>');  
    });
});

//パラメータを取ってくれる関数
function getParam(name, url) {
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}