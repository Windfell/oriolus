$(document).ready(function () {
    $("#addnew").click(function () {
        location.href = "/blog/add";
    });
    $("#edit").click(function () {
        id = $("#edit_blog_id").val()
//        location.href = "/blog/edit/" + id;
    });
    $(".autotext").focus(function () {
        if (this.value = "标签用英文逗号(,)分隔") {
            this.value = "";
        }
    });
});

function replaceDot(str) {
    var Obj = document.getElementById(str);
    var oldValue = Obj.value;
    while (oldValue.indexOf("，") != -1)//寻找每一个中文逗号，并替换
    {
        Obj.value = oldValue.replace("，", ",");
        oldValue = Obj.value;
    }
}

