$(document).ready(function() {

    // get_openai_response("story_style")

    $('.character').on('change', function(){
        $('.human_div, .animal_div').addClass('d-none')
        if($('.character:checked').val() == 'human'){
            $('.human_div').removeClass('d-none')
        }
        else{
            $('.animal_div').removeClass('d-none')
        }
    })

    $(document).on('click', '.story_style .list', function(){
        $('.character').removeClass('d-none')
    })

    $(document).on('click', '.location .list', function(){
        $('.theme').removeClass('d-none')
        get_openai_response("theme")
    })

    $(document).on('click', '.theme .list', function(){
        $('.voice').removeClass('d-none')
    })

     $('.character_nxt').on('click', function(){
        $('.location').removeClass('d-none')
         get_openai_response("location")
    })

//     $('.location_nxt').on('click', function(){
//        $('.theme').removeClass('d-none')
//         get_openai_response("theme")
//    })

//    $('.theme_nxt').on('click', function(){
//        $('.voice').removeClass('d-none')
//    })

    $('.voice_nxt').on('click', function(){

        $('.preview').removeClass('d-none')
    })

    var cip = $(".video").hover( hoverVideo, hideVideo );

    function hoverVideo(e) {
        $('video', this).get(0).play();
    }

    function hideVideo(e) {
        $('video', this).get(0).pause();
    }

//     function get_openai_response(param){
//         data = ""
//         $.ajax({
//             type: 'GET',
//             url: "openai_api/"+param,
//             beforesend: function(){
//                 $('#loading').show();
//             },
//             aftersend: function(){
//                 $('#loading').hide();
//             },
//             success:function(data){
//                 response = ''
//                 for (let i = 0; i < data.response.length; i++) {
//                   $('.'+param).append('<a class="list">'+data.response[i]+'<br></a>')
//                 }
// //                $('.'+param).append(data.response)
//             },
//         });
//     }

})