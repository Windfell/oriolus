$(document).ready(function () {
    $("#addnew").click(function () {
        location.href = "/blog/add";
    });
    $("#edit").click(function () {
        id = $("#edit_blog_id").val()
//        location.href = "/blog/edit/" + id;
    });

});

