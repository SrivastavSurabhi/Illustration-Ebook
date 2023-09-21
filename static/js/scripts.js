$(function () {
	

/* ==========================================
        scrollTop() >= 300
	Should be equal the the height of the header
	========================================== */

	// $(window).scroll(function () {
	// 	if ($(this).scrollTop() > 50) {
	// 		$('.site-navbar').addClass("is-sticky");
	// 	} else {
	// 		$('.site-navbar').removeClass("is-sticky");
	// 	}
    // });
    
    $('body').on('click', '.card-grid', function () {        
        $(this).parents('.owl-item').siblings().find('.card-grid-active').removeClass("card-grid-active");
    	if($(this).parents('.card-style:not(.character-selection)').length != 0){
        	$(this).parents('.card').next('.card').addClass('show_now');
		}
		if($(this).parents('.card-style.theme-selection').length != 0){
        	$(this).parents('.card-style.theme-selection').find('.card-grid-active').removeClass("card-grid-active");
		}
		$(this).addClass("card-grid-active");
    });

	// $('body').on('click', '.moral-story-button .card-grids', function () {
	// 	$('.moral-story-button .card-grids').removeClass("card-grid-active");
	// 	$(this).addClass("card-grid-active");
    // });


    $('body').on('click', '.voice-grid', function () {
        $(this).addClass("card-grid-active");
        $(this).parents('.rm-voice-grid-active').siblings().find('.card-grid-active').removeClass("card-grid-active");
        
        // $(this).parents('.user-preview-container').next('.user-preview-container').addClass('show_now');
        // alert("Hello");
    });

    $('.char_selction_btn').click(function () {
         $(this).parents('.card').next('.card').addClass('show_now');
    });

    $('.removebtnAttr').click(function () {
        $(this).parents('.card').find('.char_selction_btn').removeAttr('disabled') 
	});
	
	// $('.card-style.character-selection .card-grid,  button.active').click(function () {
	$(".card-style.character-selection .card-grid, .animal_name").on("click input", function() {
		if($(".card-style.character-selection .card-grid.card-grid-active").length != 0 && $(".animal_name").val()){
        	$(this).parents('.card').find('.char_selction_btn').removeAttr('disabled') 
		}
		else{
			$(this).parents('.card').find('.char_selction_btn').attr('disabled', true)
		}
	})


	$(".human_ethnicity, .human_age, .human_name, .human_gender").on("change", function() {
		if($('.human_name').val() && $('.human_gender:checked').val() && $('.human_age').val() && $('.human_ethnicity').val()){
        	$(this).parents('.card').find('.char_selction_btn').removeAttr('disabled') 
		}
		else{
			$(this).parents('.card').find('.char_selction_btn').attr('disabled', true)
		}
	})
	
	$(".age-groups").on("change", function() {
		if($(".age-groups:checked").val()){
			$(this).parents('.card').find('.char_selction_btn').attr('disabled', false)
		}
		else{
			$(this).parents('.card').find('.char_selction_btn').attr('disabled', true)
		}
	})

	$(".voice-grid").on("click", function() {
		$("#generate-story").attr("disabled", false)
	})

	$('#generate-story').click(function () {
		story_saprk = $('#floatingTextarea2').val()
		writing_style = $('.story-carousel .owl-item .card-grid-active').next('.text-dark').text().trim();
		character_id = $('.character-selection-tab .nav-link.active').attr('id')
		// var pattern = /\b(human|person)\b/i;		
		story_location = $('.settings-fields .owl-item .card-grid-active').next('.text-dark').text().trim();
		moral = $('.moral_of_story .card-grid-active .text-dark').text().trim();
		audio = $('.rm-voice-grid-active .card-grid-active .text-dark').text().trim();
		background = $('.removebtnAttr.card-grid-active').css('background-image')
		readers_age_group = $('.age-groups:checked').val().trim()
		param = {"writing_style": writing_style, "location": story_location, "moral": moral, "audio": audio, "story_saprk":story_saprk, "background":background,"readers_age_group":readers_age_group}
		if (character_id == 'nav-human-tab') {
			param['character'] = "human"
			param['human_name'] = $('.human_name').val().trim()
			param['gender'] = $('.human_gender:checked').val().trim()
			param['age'] = $('.human_age').val().trim()
			param['ethnicity'] = $('.human_ethnicity option:selected').text().trim()
		}
		else{
			param['character'] = "animal"
			param['animal_name'] = $('.animal_name').val().trim()
			param['animal_type'] = $('.animal-carousel .owl-item .card-grid-active').next('.text-dark').text().trim();
		}
		get_openai_response('generate_story', param)
		$('.writing_style').text(writing_style)
		$('.writting_moral').text(moral)
	});
	
	$('#edit-settings').click(function () {
		edit_btn_dynamic_data()
		// $(".writing_style_edit").append(writing_style_div())
		$('.user-preview-container').removeClass('d-none').addClass('d-block');
		$('.user-generate-container').removeClass('show_now').addClass('d-none');
	});

	$(".edit_selected_character .card-edit-grid").click(function () {		
		$(".edit_selected_character .card-edit-grid").removeClass("active")
		$(this).addClass("active")
		if ($(this).hasClass("human")) {
			$(".animal_character_edit").closest(".preview-story-section").addClass("d-none")
			$(".human_character_edit").closest(".preview-story-section").removeClass("d-none")
			// $(".character_img").closest(".row").addClass("d-none")
			$(`.human_display`).removeClass("d-none")
			$(`.animal_display`).addClass("d-none")
		}
		else{
			$(".animal_character_edit").closest(".preview-story-section").removeClass("d-none")
			$(".human_character_edit").closest(".preview-story-section").addClass("d-none")
			// $(".character_img").closest(".row").removeClass("d-none")
			$(`.animal_display`).removeClass("d-none")
			$(`.human_display`).addClass("d-none")
		}
	})

	$('#re-generate-story').click(function () {
		$('#edit-settings').hide()
		writing_style = $('.edit_book_cover .writing_style').text().trim();
		// character_id = $('.character-selection-tab .nav-link.active').attr('id')
		story_location_src = $('.setting_img').attr('src').replace("http://127.0.0.1:8000/", "").replace("http://3.22.65.185:8087/", "")
		$.each(EditBackground, function(e, val){
			if (val.BackgroundUrl == story_location_src) {
				story_location = val.BackgroundName
			}
		})
		moral = $('.writting_moral').text().trim();
		audio = $('.edit-voice-text .text-dark').text().trim();
		background = $('.removebtnAttr.card-grid-active').css('background-image')
		readers_age_group = $('.age-groups-edit:checked').val().trim()
		param = {"writing_style": writing_style, "location": story_location, "moral": moral, "audio": audio, "story_saprk":story_saprk, "background":background,"readers_age_group":readers_age_group}

		if ($(".edit_selected_character .active").hasClass("human")) {
			param['character'] = "human"
			param['human_name'] = $('.edit_human_name').val()
			param['gender'] = $('.edit_human_gender:checked').val()
			param['age'] = $('.edit_human_age').val()
			param['ethnicity'] = $('.edit_human_ethnicity option:selected').text()
		}
		else{
			param['character'] = "animal"
			param['animal_name'] = $('.edit_animal_name').val()
			$(`.animal_display`).removeClass("d-none")
			let animal_type =""
			animal_src = $(".character_img").attr('src').replace("http://127.0.0.1:8000/", "").replace("http://3.22.65.185:8087/", "")
			$.each(EditAnimal, function(e, val){
				if (val.AnimalUrl == animal_src) {
					animal_type = val.AnimalName
				}
			})
			// param['animal_name'] = $('.animal_name').val()
			param['animal_type'] = animal_type
		}
		get_openai_response('generate_story', param)
		$('.writing_style').text(writing_style)
		$('.writting_moral').text(moral)
	});
		
	// $('#back-story').click(function () {
	// 	$('.user-preview-container').removeClass('show_now');
	// 	$('.user-inputs-container').removeClass('d-none').addClass('d-block');
	// });
	// $('#generate-story').click(function () {
	// 	$('.user-generate-container').removeClass('d-none').addClass('show_now');
	// 	$('.user-preview-container').removeClass('show_now').addClass('d-block');
	// });
	
	$('#story-owl-carousel').owlCarousel({
		rtl: true,
		loop: true,
		margin: 10,
		autoplay:true,
		nav: true,
		dots: false,
		 navText: [
        	'>',
			'<'
		],
		responsive: {
			0: {
				items: 3
			},
			600: {
				items: 3
			},
			1000: {
				items: 4
			},
			1280: {
				items: 6
			}
		}
	});

	$('#animal-owl-carousel').owlCarousel({
	rtl: true,
	loop: true,
	margin: 10,
	autoplay:true,
	nav: true,
	dots: false,
		navText: [
		'>',
		'<'
	],
	responsive: {
		0: {
			items: 4
		},
		600: {
			items: 4
		},
		1000: {
			items: 5
		}
	}
	});

	$('#settings-owl-carousel').owlCarousel({
		rtl: true,
		loop: true,
		margin: 10,
		autoplay:true,
		nav: true,
		dots: false,
		 navText: [
        	'>',
			'<'
		],
		responsive: {
			0: {
				items: 3
			},
			600: {
				items: 3
			},
			1000: {
				items: 5
			}
		}
	});

	$('#theme-owl-carousel').owlCarousel({
		rtl: true,
		loop: true,
		margin: 10,
		autoplay:true,
		nav: true,
		dots: false,
		 navText: [
        	'>',
			'<'
		],
		responsive: {
			0: {
				items: 2
			},
			600: {
				items: 3
			},
			1000: {
				items: 5
			}
		}
	});

	$(".card-edit-grid").click(function () {
		$(this).siblings().removeClass("active")
		img_src = get_src_from_style($(this))
		var modifiedUrl = img_src.replace("http://127.0.0.1:8000/", "").replace("http://3.22.65.185:8087/", "");
		edit_element = $(this).addClass("active").parents(".preview-story-edit").siblings(".preview-story-section")
		edit_element.find("img").attr("src", img_src)
		if ($(this).parents().hasClass("writing_style_edit")){
			$.each(WritingStyle, function(e, val){
				if (val.ImgUrl == modifiedUrl) {
					edit_element.find(".writing_style").text(val.Auther)
				}
			})
		}
		else if ($(this).parents(".card-writing-story").hasClass("edit_character")){
			edit_element = $(this).addClass("active").parents(".preview-story-edit").closest(".preview-story-section")
			edit_element.find(".character_img").attr("src", img_src)
		}
		else if ($(this).parents().hasClass("moral_edit")){
			$.each(StoryMoral, function(e, val){
				if (val.ImgUrl == modifiedUrl) {
					edit_element.find(".writting_moral").text(val.Moral)
				}
			})
		}
	});


	$('.audio-sample').click(function(){	
		$('.edit-voice-text audio source').attr('src',AudioSource[$(this).attr('id')]['AudioUrl'])
		$('.edit-voice-text .small.text-dark').text(AudioSource[$(this).attr('id')]['AudioName'])
		$('.edit-voice-text audio')[0].load()
	})
	
	$(document).on('click','.background_edit .card-edit-grid',function(){
		story_location_name = $(this).css("background-image").replace(/^url\(["']?/, '').replace(/["']?\)$/, '').replace("http://127.0.0.1:8000/", "").replace("http://3.22.65.185:8087/", "");
		$.each(EditBackground, function(e, val){
			if (val.BackgroundUrl == '/'+story_location_name) {
				$('.setting-edited-img').text(val.BackgroundName)
			}
		})
	})
});


function edit_btn_dynamic_data(){
	add_active_class_edit($('.story-carousel .owl-item .card-grid-active'), $(".selected_book_img"), $(".writing_style_edit"))
	
	add_active_class_edit($('.animal-carousel .owl-item .card-grid-active'), $(".character_img"),$(".animal_character_edit"))
	
	add_active_class_edit($('.settings-carousel .owl-item .card-grid-active'), $(".setting_img"), $(".background_edit"))
	
	// add_active_class_edit($('.settings-carousel .owl-item .card-grid-active'), $(".setting_img"), $(".background_edit"))

	moralImg = $('.moral-story-button.card-grid-active .story-icon img').attr('src')
	$(".moral_img").attr("src", moralImg)
	$(`.edit_moral .edit-icon div[style="background-image: url('${moralImg}')"]`).addClass("active")

	if($('.character-selection-tab .nav-link.active').attr('id')=='nav-human-tab'){
		$('.human').addClass('active')
		$('.animal').removeClass('active')
		$(`.human_display`).removeClass("d-none")
	}
	else{
		$('.human').removeClass('active')
		$('.animal').addClass('active')
		$(`.animal_display`).removeClass("d-none")
	}
	age_gr = $('.age-groups:checked').val()
	$(`.age-groups-edit[value="${age_gr}"]`).attr('checked',true)

	voice_text = $('.rm-voice-grid-active .card-grid-active .text-dark').text().trim()
	selected_voice =  $('.rm-voice-grid-active .card-grid-active audio source').attr('src')
	$('.edit-voice-text .small.text-dark').text(voice_text)
	$('.setting-edited-img.text-dark').text($('.settings-fields .card-grid-active').next().text().trim())
	$('.edit-voice-text audio source').attr('src',selected_voice)
	$('.edit-voice-text audio')[0].load()
	class_name =$('.rm-voice-grid-active .card-grid-active audio').attr('class')
	$('#'+class_name).addClass('active') 

	if($(".character_img").hasClass('human_img')){
		$('.human_img').attr("src", "/static/assets/img/human.png")
		$('.edit_human_name').val($('.human_name').val())
		$('.edit_human_gender[value="'+$('.human_gender:checked').val()+'"]').prop("checked", true)
		$('.edit_human_age').val($('.human_age').val())
		 $('.edit_human_ethnicity').val($('.human_ethnicity').val())
	}
	if($(".character_img").hasClass('anima_img')){
		$('.edit_animal_name').val($('.animal_name').val())
	}
}

function add_active_class_edit(eleDiv, displayDiv, editDiv){
	ImageUrl = get_src_from_style(eleDiv)
	displayDiv.attr("src", ImageUrl)
	editDiv.find(`.card-edit-grid[style="${eleDiv.attr("style")}"]`).addClass("active")
}

function get_src_from_style(eleDiv){
	return eleDiv.css('background-image').replace(/^url\(["']?/, '').replace(/["']?\)$/, '');
}

function get_openai_response(param, obj=""){
	data = ""
	$.ajax({
		type: 'GET',
		url: "openai_api/"+param,
		data:obj,
		beforeSend: function(){
			$('.parent-loader').show();
		},
		complete: function(){
			$('.parent-loader').hide();
		},
		success:function(data){
		if ( param = "generate_story"){
			if(data.error){
				alert("Something went wrong, Please try again")
			}
			if(data.response){
				$('.generate-story .dynamic_story').empty()
				$('#story_audio').attr('src',data.response['output_path'])
				$('.user-generate-container').css('background-image', `${data.response['background']}`);
				$('.user-generate-container').removeClass('d-none').addClass('show_now');
				$('.user-inputs-container, user-generate-containers').addClass('d-none').removeClass('d-block');
				$('.user-preview-container').removeClass('d-block').addClass('d-none');
				storyDiv = ""
				storyDiv += `
					<div class="audio-div offset-lg-4">
					<audio controls>
					<source id="story_audio" src=${data.response['output_path']}
						type="audio/mpeg">
					Your browser does not support the audio element.
					</audio>
					</div>
				`
				$.each(data.response['response_dict'], function(num, res){
				storyDiv += `<div class="p-lg-3 m-2">
					<div class="row">
						<div class="col-12 col-md-4 col-lg-3">
							<img src="${res.image}" class="img-thumbnail" alt="image">
						</div>
						<div class="col-12 col-md-8 col-lg-9">
							<div class="book-description">
								<p class="text-dark fw-normal mb-2">${res.text}</p>
							</div>
						</div>
					</div>
					</div>`
				})
					$('.generate-story .dynamic_story').append(storyDiv)
				}
			}
		else{
			alert(data.error)
		}
		},
		error:function(e){
			alert("Something went wrong, Please try again")
		}
	});
}


