$(document).ready(function () {
    $('.scrollspy').scrollSpy({
        scrollOffset: 0,
    });

    M.AutoInit(document.body);

    $(document).on('submit', '#writeback_form', function(event) {
        event.preventDefault();

        var name = $('#icon_prefix').val();
        var phone = $('#icon_telephone').val();

        $.ajax({
            url: "writeback",
            type: "post",
            dataType: "json",
            data: JSON.stringify({
                "name": name,
                "phone": phone
            }),

            success: function (data) {
                document.getElementById("icon_prefix").value = "";
                document.getElementById("icon_telephone").value = "";
                M.toast({ html: data.result, classes: 'rounded' });
            }
        });
    });
});