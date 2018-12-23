$(function(){
    function isCJK(c){ // c: character to check
      var unicode = c.charCodeAt(0);
      if ( (unicode>=0x3000 && unicode<=0x303f)   || // Japanese-style punctuation
           (unicode>=0x3040 && unicode<=0x309f)   || // Hiragana
           (unicode>=0x30a0 && unicode<=0x30ff)   || // Katakana
           (unicode>=0x4e00  && unicode<=0x9fcf)  || // CJK integrated kanji
           (unicode>=0x3400  && unicode<=0x4dbf)  || // CJK integrated kanji ext A
           (unicode>=0xff00 && unicode<=0xff9f)   || // Full-width roman characters and half-width katakana
           (unicode>=0x20000 && unicode<=0x2a6df) || // CJK integrated kanji ext B
           (unicode>=0xf900  && unicode<=0xfadf)  || // CJK compatible kanji
           (unicode>=0x2f800 && unicode<=0x2fa1f) || // CJK compatible kanji
           (unicode>=0xffa0 && unicode<=0xffdc) || // Hangul Half
           (unicode>=0x3131 && unicode<=0xd79d)    // Hangul Full
         )
           return true;
  
      return false;
    }
  
    $("textarea").on('input', function(e){
      var text = $("textarea").val();
      var length = text.length;
      count = 0
      for(var i=0; i<length; i++) {
        var character = text.charAt(i)
        if(isCJK(character)){
          count +=2;
        } else {
          count++;
        }
      }
      $('#counter').text("残り" + (80-count) + "文字");
    });

    $('form').submit(function() {
        if (count > 80) {
            alert('文字数オーバーです!!');
            return false;
        } else {
            this.submit();
        }
    });
  });