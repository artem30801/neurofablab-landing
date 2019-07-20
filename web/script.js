$(document).ready(function () {
    $('.scrollspy').scrollSpy({
        scrollOffset: 0,
    });

    M.AutoInit(document.body);

    $('#btn').click(function () {

        var name = $('#icon_prefix').val();
        var phone = $('#icon_telephone').val();

        $.ajax({
            url: "action.php",
            type: "post",
            dataType: "json",
            data: {
                "name": name,
                "phone": phone
            },

            success: function (data) {
                document.getElementById("icon_prefix").value = "";
                document.getElementById("icon_telephone").value = "";
                M.toast({ html: data.result, classes: 'rounded' });
            }
        });
    });
});