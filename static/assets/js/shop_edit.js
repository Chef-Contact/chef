$(document).ready(function() {
    $('.image-btn').click(function() {
        var imageUrl = $(this).data('image-url');
        $('#modalImage').attr('src', imageUrl);
        
    });
    $('#selectDesignBtn').click(()=>{
        var imageId = $('.image-btn').data('id');
        $('#imageIdInput').attr('value', imageId);

    })
    $('#selectDesignBtn').click(function() {
        $('#imageModal').modal('hide');
    });
});