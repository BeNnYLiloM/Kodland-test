$(document).ready(function () {

    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function(e) {
                $('#blah').attr('src', e.target.result);
            }

            reader.readAsDataURL(input.files[0]);

            $('.blog__form-add-file').addClass('_added');
        }
    }

    $("#addImg").change(function() {
        readURL(this);
    });

    $('.blog__form-add-file-delete').click(function () {
        $('.blog__form-add-file').removeClass('_added');
    });

});