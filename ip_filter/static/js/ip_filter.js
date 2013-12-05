/**
 * Created by ahmetdal on 11/26/13.
 */


$(document).ready(function () {
    $.datepicker.setDefaults($.datepicker.regional[lang])
            $('select.vIpField').change(function () {
                redirect($(this))
            });

            $('input.vIpField').keypress(function (e) {
                if (e.which == 13) {
                    redirect($(this))
                }
            });
});

function redirect(element){
    var qs = $.deparam.querystring()
    qs[element.attr('name')] = element.val()
    window.location.href = $.param.querystring('', qs);
}
