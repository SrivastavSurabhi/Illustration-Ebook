$(document).ready(function(){
    var currentUrl = window.location.href;
    var name = currentUrl.split("#")[1].split("name=")[1]
    var unique_id = currentUrl.split("#")[2].split("unique_id=")[1]
    setTimeout(function () {
        generateStory(unique_id)
    }, 4000);
    $('.readers_name').text(name)
    $('.radio-list').click(function(){
        $('.radio-list').removeClass('radio-active');
        $(this).addClass('radio-active');
    })
    $('.submit_btn').click(function(){
        var generate_poem = $('.radio-list.radio-active .radio-option-text').text().trim()
        if(generate_poem == 'Yes'){
            generatePoem(unique_id)
            
        }
        else{
            if ($('.dynamic_story').text() == "" || $('.audio-container').hasClass('d-none')){
                $('.parent-loader').show();
            }
            $('.story_area').removeClass('d-none');
            $('.poem_area').addClass('d-none');
            $('.poem_confirmation').addClass('d-none');
        }
    })
    $('.ready-story a').click(function(){
        $('.story_area').removeClass('d-none')
        $('.poem_area').addClass('d-none')
        $('.poem_confirmation').addClass('d-none')
    })
})

function generateStory(unique_id){
    $.ajax({
            type: 'GET',
            url: "/create_story/"+unique_id,
            // complete: function(){
            //     $('.parent-loader').hide();
            // },
            success:function(response){
                console.log(response)
                if (response.response.response_dict != undefined && response.response.response_dict.error){
                    alert("Something went wrong while story creation. Please fill the form again.")
                }
                else{
                    $('.story_title').text(response.response.storyType)
                    if(response.response.storyType == "eBook Story 🖼️" || response.response.storyType == "Coloring Book 🎨📖"){
                        $.each(response.response.response_dict,function(index,data){
                            console.log(data)
                            storyDiv = ""
                            storyDiv += `
                                    <div class="row my-3 my-lg-5">
                                        <div class="col-12">
                                            <div class="row">
                                                <div class="col-12 col-md-6 col-lg-6 pe-md-0">
                                                    <img src="/${data.image}" class="img-fluid rounded-0" alt="image">
                                                </div>
                                                <div class="col-12 col-md-6 col-lg-6 ps-md-0">
                                                    <div class="book-description">
                                                        <p class=" fw-normal mb-2">${data.text}</p>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>`
                            // $('.generate-story .dynamic_story').append(storyDiv)
                            $('.dynamic_story').append(storyDiv)
                        })
        
                    }
                    else if(response.response.storyType == "eBook Story 📖"){
                        storyDiv = ""
                        storyDiv += `<div class="p-lg-3 m-2">
                                <div class="row">
                                    <div class="col-12 col-md-12 col-lg-8 offset-lg-2">
                                        <div class="text-book">
                                            <p class=" fw-normal mb-2">${response.response.response_dict}</p>
                                        </div>
                                    </div>
                                </div>
                                </div>`
                        // $('.generate-story .dynamic_story').append(storyDiv)
                        $('.dynamic_story').append(storyDiv)
                    }
                    else{
                        $('.audio-container').removeClass('d-none')
                        
                        // $('.story_audio source').attr('src',response.response.output_path)
                        storyDiv = ""
                        storyDiv += `
                            <div class="story_audio">
                            <audio controls>
                            <source id="story_audio" src=/${response.response.output_path}
                                type="audio/mpeg">
                            Your browser does not support the audio element.
                            </audio>
                            </div>
                        `
                        $('.story_audio').append(storyDiv);
                    }
                    $('.ready-story').removeClass('d-none')
                    $('.preparing-story').addClass('d-none')
                    $('.parent-loader').hide();
                }
            },
            error:function(response){
                alert("Something went wrong!! Please try again.")
            }
    })
}


function generatePoem(unique_id){
    $.ajax({
            type: 'GET',
            url: "/create_poem/"+unique_id,
            beforeSend: function(){
                $('.parent-loader').show();
            },
            complete: function(){
                $('.parent-loader').hide();
            },
            success:function(poem_response){
                console.log(poem_response)
                $('.poem_area').removeClass('d-none')
                $('.poem_confirmation').addClass('d-none')
                $('.story_area').addClass('d-none')
                if(poem_response){
                    poemDiv=''
                    poemDiv += `
                        <div class="p-lg-3 m-2">
                            <div class="row">
                                <div class="col-12 col-lg-8 offset-lg-2 col-xl-6 offset-xl-4">
                                    <div class="poem-content">
                                        <p class=" fw-normal mb-2">${poem_response.response}</p>
                                    </div>
                                </div>
                            </div>
                        </div>`
                    $('.dynamic_poem').html(poemDiv)    
            }
            }
    })
}