$(function(){
    // 编辑器
    var $preview = $('#preview');
    var $editor = $('#editor');
    var $textarea = $('textarea', $editor);

    // marked设置
    marked.setOptions({
        gfm: true,
        tables: true,
        breaks: false,
        pedantic: true,
        sanitize: false,
        smartLists: false,
        highlight: function(code, lang){
            setTimer('prettify', function(){
                $('pre code', $preview).addClass('prettyprint');
                prettyPrint();
            }, 50);
            // 将\n修改为<br>，因为在ie里面pre标签中的\n不会产生换行
            return code.replace(/>/g, '&gt;').replace(/</g, '&lt;').
                        replace(/\n/g, '<br>');
        }
    });

    // 动态改变输入框的大小
    $(window).on('resize', function(){
        setTimer('resize', function(){
            $textarea.height($editor.height() - 32);
        }, 100);
    }).resize();

    $textarea.on('input', function(){
        setTimer('input', function(){
            $preview.html(marked($textarea.val()));
            $preview.css('height','600px');
            $preview.css("overflow","auto");
            $('p:has(img)').add($('embed, iframe').wrap('<p></p>').parent())
            .css('text-align', 'center');
        }, 10);
    }).focus(function(){
        $textarea.trigger('input');
    }).on('keydown', function(e){
        var k = e.which;
        // TAB键
        if(k == 9){
            var start = this.selectionStart;
            var end = this.selectionEnd;
            var self = $(this);
            var val = self.val();
            self.val(val.substring(0, start) + '    ' + val.substring(end));
            this.selectionStart = this.selectionEnd = start + 4;
            return false;
        }
    }).trigger('input').css('overflow', 'auto').focus();
});


/* 设置定时器
 * >>> setTimer('scroll_timer', function(){}, 1000);
 * name: 定时器的名字[名字将绑定在window对象上，请确保每个定时器名字唯一]
 * callback: 回调函数
 * time: 延迟时间[单位毫秒]
 */
function setTimer(name, callback, delay){
    // 加个后缀，避免与其他window上的属性冲突
    var name = name + '_timer_pabo_';
    if(window[name]){
        clearTimeout(window[name]);
    }
    window[name] = setTimeout(callback, delay);
}
