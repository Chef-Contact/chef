$(document).ready(function () {
    $('.image-btn').click(function () {
        var imageUrl = $(this).data('image-url');
        $('#modalImage').attr('src', imageUrl);
    });

    const dd = document.querySelectorAll('.asdad')
    for (let i = 0; i < dd.length; i++) {
        dd[i].onclick = (e) => {
            dd[i].style.border = '3px solid #f8c026'
            for (let i = 0; i < dd.length; i++) {
                if (dd[i] !== e.target.parentElement) {
                    dd[i].style.border = 'none'
                }
            }

            if (e.target.classList[0] == 'img-thumbnail') {
                $('#imageIdInput').attr('value', e.target.parentElement.dataset.id);
            } else {
                $('#imageIdInput').attr('value', e.target.dataset.id);
            }
        }
    }

    $('#selectDesignBtn').click((e) => {
        var imageId = $('.image-btn').data('id');

    })
    $('#selectDesignBtn').click(function () {
        $('#imageModal').modal('hide');
    });
});