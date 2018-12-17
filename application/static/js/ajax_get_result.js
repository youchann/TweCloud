$(function() {
    var OT = getParam("oauth_token");
    var OV = getParam("oauth_verifier");
    var oauth_data = JSON.stringify({"oauth_token":OT,"oauth_verifier":OV});

    $.ajax({
        type: "POST",
        url: "analyze",
        contentType:"application/json",
        data: oauth_data,
        success:function(data) {
            var file_name = JSON.parse(data.ResultSet).file_name;
            $("#loading").remove(); //loading画面の削除
            $(".result_image").append('<p>これがあなたのクモです！</p>');
            $(".result_image").append('<img src="static/images/' + file_name + '">');
        }
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