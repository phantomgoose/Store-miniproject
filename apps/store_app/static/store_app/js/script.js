$(document).ready(function(){
    $('.add-to-cart-btn').submit(function(){
        var button = this;
        $.ajax({
            url: "/store/cart/update",
            method: 'post',
            dataType: 'json',
            data: $(this).serialize(),
            success: function(response){
                if (response.cart_updated === true){
                    $('.add-to-cart-btn').find('input[name=amount]').val("");
                    $(button).siblings('.cart-update').html(response.server_message).fadeTo(1500, 1.0).fadeTo(1500, 0.0);
                    $.ajax({
                        url: "/store/cart/show",
                        success: function(response){
                            $('.cart').html(response);
                        }
                    });
                }
                else {
                    $(button).siblings('.cart-update').html(response.server_message).fadeTo(1500, 1.0).fadeTo(1500, 0.0);
                }
            }
        });
        return false;
    });

    $('#show-cart').click(function(){
        $.ajax({
            url: $(this).attr('href'),
            success: function(response){
                $('.cart').html(response).slideToggle();
            }
        });
        return false;
    });

    $('.store-remove-link').click(function(){
        $.ajax({
            url: $(this).attr('href'),
            success: function(response){
                window.location.reload();
            }
        });
        return false;
    });
});