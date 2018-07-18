

SLICK_SLIDER = {

    bindSlickSlider: function(){
        $(document).ready(function(){
            $(".watch-videos-slide").slick({
                infinite:true,
                slidesToShow: 3,
                slidesToScroll: 3
            })
        })
    }
}

SLICK_SLIDER.bindSlickSlider();