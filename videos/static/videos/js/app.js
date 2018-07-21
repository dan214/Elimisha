

SLICK_SLIDER = {

    bindSlickSlider: function(){

        var sliderVideoId = $(".watch-videos-slide");
        if(sliderVideoId.length > 0){
            $(document).ready(function(){
                $(".watch-videos-slide").slick({
                    infinite:true,
                    slidesToShow: 3,
                    slidesToScroll: 3
                })
            })
        }

    }
}

SLICK_SLIDER.bindSlickSlider();