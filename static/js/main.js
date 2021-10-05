$(document).ready(function () {
    $("form").submit(function (e) {
        console.log($('form').serializeArray())
        let x = $('form').serializeArray()
        let y = new Set(x.map(i => i.value))
        if (y.size != 4) {
            $("#error").removeClass("hidden");
            e.preventDefault();
        }
    });
});
