// listButton.addEventListener("click", listFiles);
$(document).ready(function () {
    $("#submit").click(function () {
        console.log($('form').serializeArray())
        // console.log("{{url_for ('get_imgs')}}")
        // alert("asdf")
        $.getJSON($SCRIPT_ROOT + '/_add_numbers', {
            a: $('input[name="a"]').val(),
            b: $('input[name="b"]').val()
        }, function (data) {
            console.log(data)
        });
    
        console.log("asdf")
    });

    $("#test").click(function () {
        console.log($('form').serializeArray());
        $.getJSON($SCRIPT_ROOT + '/_add_numbers', {
            a: $('input[name="a"]').val(),
            b: $('input[name="b"]').val()
        }, function (data) {
            console.log(data)
        });
        console.log("hit");
        // listFiles()
    });
});
