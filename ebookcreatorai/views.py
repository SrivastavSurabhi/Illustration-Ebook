from django.shortcuts import render
from django.http import JsonResponse
import openai
import os
import requests
from django.conf import settings
import base64
import random
from datetime import datetime
from .constants import VOICES ,LATESTVOICES, FORM_FIELDS, BOOK_TYPE, STORY_FORMAT
from .prompts import *
import json
from django.http import HttpResponse
from story.models import Response, FormData
import uuid
openai.api_key = os.environ.get('OPENAI_API_KEY')
# openai.api_key = os.getenv('CHAT_GPT_KEY')

final_response = ""
final_response_poem = ""
responses = {}
form_response_id=""
last_prompt_text = "in a scene 8k rendered with vibrant colors and renderman,In the style of Pixar artists, CGI, Extremely Detailed."
media_path = settings.MEDIA_ROOT


def home(request):
    return render(request, 'index.html')

def story_preview(request):
    unique_id = uuid.uuid4()
    return render(request, 'type_form_response.html', {"unique_id":unique_id})


def show_customized_story(request):
    return render(request, 'show_customized_story.html')


# def show_customized_story(request):
    # global final_response
    # global final_response_poem
    # global form_response_id
    # response = render(request, 'show_customized_story.html')
    # response.set_cookie('generated-poem', final_response_poem)
    # response.set_cookie('generated-story',json.dumps({'final_response':final_response}))
    # print("123",final_response)
    # redirect_to_story = request.GET.get("response","")
    # unique_id = request.GET["data"].split("unique_id=")
    # try:
    #     final_response = Response.objects.filter(unique_id=unique_id[0]).values('story_text')
    #     # final_response = {'response_dict': {1: {'image': 'media/images/A Brave Human 🦸\u200d♂️Jerry2023-09-06-17-56-25.3439071.png', 'text': "In the parched and wind-strewn township of Sandy Ridges, there existed an enigma most peculiar - a petite maiden, fair of face and stout of heart, known by all as young Jerry. Now, 'tis unusual to christen a young girl by such a moniker, but Jerry was a child unlike any other who lived amidst the wild tapestry of tumbleweeds and cacti. Underneath her broad straw hat, atop her sun-kissed, freckled face, shone eyes deep like the old wishing well in the town, harbouring wells of untold tales. Her mirth was like a prairie sunflower, bright and resilient, enchanting the whole town with its innocent delight. "}, 2: {'image': 'media/images/A Brave Human 🦸\u200d♂️Jerry2023-09-06-17-57-04.5556442.png', 'text': "On many an afternoon, on the sun baked streets, under the blazing western sun, Jerry would gallop through the heart of Sandy Ridges on her wooden stallion, steadfast and bold. Her imaginary foe? The mischievous wind spirit, who would playfully tip hats off the heads of unsuspecting folks. Armed with giggles and undying faith, she'd battle the wind, and save her beloved town, time after time. It was her unwavering spirit that transformed this unruly foe, into a dear friend, a result that even old sheriff Samuel couldn't fathom. Ah, such was the miraculous power of friendship, showering even the driest of the wild western towns with a rainbow of unity and merriment - a message to one and all that ‘Friendship's Power Conquers All.'"}}, 'background': 'Dusty Streets of a Wild West Town 🌵🤠'}
    #     render_response = list(final_response)[0]["story_text"]
    #     return render(request, 'show_customized_story.html',{"context":render_response})
    # except:
    #     return render(request, 'show_customized_story.html',{"loader":True})

    # if final_response_poem != "" and redirect_to_story == "":
    #     render_poem = final_response_poem
    #     final_response_poem = ""
    #     return render(request, 'show_customized_poem.html',{"poem":render_poem})
    # if redirect_to_story != "":
    #     render_response = final_response
    #     return render(request, 'show_customized_story.html',{"context":render_response})
    # else:
    #     return render(request, 'show_customized_story.html',{"loader":True})
    

def poem_generation(request,*args,**kwargs):
    unique_id = kwargs['unique_id']
    responses = FormData.objects.filter(unique_id=unique_id).last()
    print("2347",responses)
    # respond_poem = json.loads(request.body.decode())['form_response']['answers'][0]['choice']['label']
    # form_response_id = json.loads(request.body.decode())['form_response']['token']
    if "Human" in responses.charcter_type.split():
        poem_prompt = human_poem_generation_prompt.format(
                    author=responses.writing_style,
                    genre=responses.genre,
                    readers_age_group=responses.readers_age_group,
                    location=responses.location,
                    gender=responses.charcter_gender,
                    human_name=responses.charachter_name,
                    age=responses.charachter_age,
                    ethnicity=responses.charachter_ethinicity,
                    moral=responses.moral
                    )
    else:
        poem_prompt = animal_poem_generation_prompt.format(
                    author=responses.writing_style,
                    genre=responses.genre,
                    readers_age_group=responses.readers_age_group,
                    location=responses.location,
                    animal_type=responses.animal_type,
                    animal_name=responses.charachter_name,
                    moral=responses.moral
                    )
    result_poem = openai_response(poem_prompt)
    # result_poem = """
    # Once upon a frothy sea,
    # In a world of salty silliness,
    # There lived a lad named Gavin, see,
    # Full of pluck and willfulness.
    
    # His hair a mop of sandy blonde,
    # His eyes a playful ocean blue.
    # In mischief and magic, Gavin was fond,
    # Oh, the crazy things he would do!
    
    # He owned a ship of cardboard make,
    # Sailed it on the kitchen table,
    # Faced down a biscuit-crumb quake,
    # Swearing, "I am Captain Able!"
    
    # He commandeered the bathtub deep,
    # It became his mystic ocean.
    # Through waves of foam, he'd bravely leap,
    # A devotion to maritime motion.
    
    # The Goldfish pirates, fierce and mean,
    # Tried to loot his rubber duck.
    # Gavin valiant, sharp and keen,
    # Left them in a state of muck.
    
    # The Squid King, twisted and cruel,
    # By his clever schemes did fascinate.
    # Gavin faced the inky ghoul,
    # "Oh, I won't be your calamari mate!"
    
    # Nights passed with challenges untold,
    # Yet our Gavin never wearied.
    # His courage refine, his spirit bold,
    # His voyage never teared.
    
    # Even when the odds grew large,
    # And the soap slipped under water.
    # Gavin, smiling, took the charge,
    # Like a real seafarer's daughter.
    
    # In the heart of the mystic ocean's swirl,
    # Lies a hidden starry treasure.
    # "To all brave boys and hearty girls,
    # The sky's the limit - no bottom measure!"
    
    # Perseverance, the key Gavin found,
    # In every wave and fearsome weather.
    # Through his twists and turns around,
    # Kept his cardboard ship together.
    
    # So now he sails under the bath time light,
    # Laughing at sea's cruel caper.
    # In the world beneath the frothy white,
    # Gavin always found his paper.
    
    # Under the waves of a mystic ocean blue,
    # This is where our story ends.
    # Remember, Young Explorers, true,
    # Dreams and daring make great friends."""
    final_response_poem = result_poem
    Response.objects.create(
        unique_id=unique_id,
        genated_content=2,
        response_id=form_response_id,
        story_text=result_poem,
    ) 
    return JsonResponse( {"response":final_response_poem})
   


# form_data = [{'type': 'text', 'text': 'Arya', 'field': {'id': 'Ed043z5IVGGS', 'type': 'short_text', 'ref': 'de647bfc-03e4-42e3-b339-bf22da6b71cb'}}, {'type': 'choice', 'choice': {'id': 'rsecBfQ9HChM', 'label': 'By coloring your own tale 🎨📖', 'ref': 'd8c104fd-6be3-4b65-b716-ad1b77b4e280'}, 'field': {'id': 'ljByUSwH5t0Z', 'type': 'multiple_choice', 'ref': '308470bb-fc07-49a5-8849-fe92d7dc5d91'}}, {'type': 'choice', 'choice': {'id': 'PONTCiaZ9pDb', 'label': 'Words & Illustrations Ready for Your Palette 🖼️', 'ref': 'dfb2eea9-0363-4d25-9073-f5c67dd0414e'}, 'field': {'id': '5Eli3dD71rDx', 'type': 'multiple_choice', 'ref': '15ebb848-9c6d-401b-b3a1-fe73f83a1315'}}, {'type': 'choice', 'choice': {'id': 'DgZk18bKq1Q6', 'label': 'Time-traveling Historical Fiction ⏳🏺', 'ref': 'f2f51bb6-e8bf-440b-a593-284ea1a9b318'}, 'field': {'id': 'f6OpQ53wjmRx', 'type': 'multiple_choice', 'ref': '7dd5dd25-a297-42a6-84c9-7e0c127d5527'}}, {'type': 'choice', 'choice': {'id': 'YelUgMt7ZKvt', 'label': 'Timeless Tales by Charles Dickens 🕰️', 'ref': '6c289db1-0901-4281-91c7-13a10234e307'}, 'field': {'id': '2xJrXwm5zqcS', 'type': 'multiple_choice', 'ref': '36c9db73-26a6-4c25-a486-045ba759ed51'}}, {'type': 'choice', 'choice': {'id': 'win4RLdaXr9K', 'label': 'A Brave Human 🦸\u200d♂️', 'ref': '58100ec2-ff21-4e43-9287-a214ff7789c1'}, 'field': {'id': 'QMxifu1yHFRB', 'type': 'multiple_choice', 'ref': 'cd4cfda2-95fd-450f-a6c5-c08b57e16da1'}}, {'type': 'text', 'text': 'Jerry', 'field': {'id': 'PhMzejBGuxbi', 'type': 'short_text', 'ref': 'bea560d0-4720-49de-918b-2deb405cdd6c'}}, {'type': 'number', 'number': 7, 'field': {'id': 'E9A3rcQq3VkM', 'type': 'number', 'ref': '1fea585b-eb9b-48bf-a655-7cb220b075c8'}}, {'type': 'choice', 'choice': {'id': '5Tsx0rjmVwo3', 'label': 'Girl 🚶\u200d♀️', 'ref': 'ac88576a-d106-43de-abc3-d248b1962de7'}, 'field': {'id': 'iuJXr8aeG0lI', 'type': 'multiple_choice', 'ref': '00a43f48-d5ac-45e0-bf28-04a21c7637f0'}}, {'type': 'choice', 'choice': {'id': '6DN1q4jOQNb7', 'label': 'Hispanic or Latino', 'ref': '6c9720cd-3f4f-463a-9ac8-e1dcc7db8bda'}, 'field': {'id': 'u8EQb4MBXF62', 'type': 'dropdown', 'ref': 'f740ec97-e4fb-4612-98ec-de13ba383f72'}}, {'type': 'choice', 'choice': {'id': '7Ti2ZVX49QbO', 'label': 'Valiant Explorers (Age 9 - 12) 🗺️', 'ref': 'fe918372-005e-4182-ad69-f5a8474a75e3'}, 'field': {'id': 'hjZdugjFEatP', 'type': 'multiple_choice', 'ref': '66c29dda-c750-4f58-8792-83b9e62b40ce'}}, {'type': 'choice', 'choice': {'id': 'KjAq29w3x4Vo', 'label': 'Deep within an Enchanted Forest 🌲🧚', 'ref': 'a8a2e13e-714d-46d0-a1c8-98e07947f47b'}, 'field': {'id': 'ZY2jw7o2t0gp', 'type': 'multiple_choice', 'ref': 'a20bdd92-6121-49eb-9220-d75811d88b43'}}, {'type': 'choice', 'choice': {'id': 'S8gVuGALNZlB', 'label': 'Kindness Echoes in Every Heartbeat 💓🎶', 'ref': 'e2af5234-23ad-4152-b91b-e9d7899ee0b4'}, 'field': {'id': 'NpyVfXQii9i6', 'type': 'multiple_choice', 'ref': '6289af6e-58a4-4cc3-b323-7dc84c7709c3'}}]



### Story Form Webhook
def generate_story_webhook(request, *args,**kwargs):
    form_responses = {}
    form_data = json.loads(request.body.decode())['form_response']['answers']
    for fields_response in form_data:
        response_id = fields_response.get('choice', {}).get('label') or fields_response.get('text') or fields_response.get('number')
        form_responses[FORM_FIELDS.get(fields_response['field']['id'])] = response_id
        print(fields_response)

    print(form_responses)
    FormData.objects.create(
        unique_id = json.loads(request.body.decode())['form_response']['hidden']['unique_id'],
        response_id = json.loads(request.body.decode())['form_response']['token'],
        readers_name = form_responses['name'],
        story_format = form_responses['book_type'],
        ebook_format = form_responses.get("ebook_format", None),
        genre = form_responses['genre'],
        writing_style = form_responses['writing_style'],
        charcter_type = form_responses['character_type'],
        charachter_name = form_responses.get("human_name", form_responses.get("animal_name", None)),
        charachter_age = form_responses.get("age", None),
        charcter_gender = form_responses.get("gender", None),
        charachter_ethinicity =form_responses.get("ethnicity", None),
        animal_type = form_responses.get('animal_type', None),
        readers_age_group = form_responses['readers_age_group'],
        location = form_responses['location'],
        moral = form_responses['moral'],
        audio_name = form_responses.get('audio', None)
    )
    return JsonResponse({"success":True})



### Phase2 story_generation_view ###
def generate_story(request, *args, **kwargs):
    result_dict = {}
    unique_id = kwargs['unique_id']
    responses = FormData.objects.filter(unique_id=unique_id).last()
    if "Human" in responses.charcter_type.split():
        name = responses.charachter_name
        ai_prompt = human_story_generation_prompt_new.format(responses.writing_style,responses.genre,responses.readers_age_group , responses.location
        ,responses.charcter_gender, responses.charachter_name, responses.charachter_age, responses.charachter_ethinicity, responses.moral, responses.writing_style,responses.readers_age_group)

        input_fields = "{age}-year-old {gender}, {ethnicity} ethnicity, set in a {location}".format(
            age=responses.charachter_age,
            gender=responses.charcter_gender,
            ethnicity=responses.charachter_ethinicity,
            location=responses.location,
        )
    else:
        name = responses.charachter_name.strip()
        ai_prompt = animal_story_generation_prompt_new.format(responses.writing_style,responses.genre,responses.readers_age_group ,responses.location,
                                    responses.charachter_name, responses.animal_type, responses.moral,responses.writing_style,responses.readers_age_group)  # noqa: E501
        input_fields = "{animal_type}, set in a {location}".format(
            animal_type=responses.animal_type,
            location=responses.location
        )

    text_response = openai_response(ai_prompt)
    # text_response = """
    #     Beneath the kaleidoscopic surface of a crystal clear ocean, in a coral palace wrapped in shimmering seaweeds and pearls, lived a small, quaint creature named Jerry. This dear girl was not like the other sea folk around her, for she was born of humans who had found their destiny under the ocean’s embrace. Alas, being neither fully human nor fully of sea, she often found herself caught between two worlds.

    #     Around Jerry, the ocean world was a mesmerising ballet of colours, where gregarious crabs marched in stride and whimsical dolphins flew through bubble halos. Yet, these wonders couldn't mitigate Jerry's desires to unveil the realm above the waves, the domain her ancestors belonged to, the land of humans.
    #     """

    choiced_book_style = responses.story_format
    if choiced_book_style == BOOK_TYPE['EBOOK']:
        if responses.ebook_format == STORY_FORMAT["TEXT"]:
            result_dict['response_dict'] = text_response.strip()
            result_dict['storyType'] ="eBook Story 📖"
            return JsonResponse({"response": result_dict})
    
    if "Audiobook" in choiced_book_style.split():
        result_dict['output_path'] = voice_narration(text_response,responses.audio_name)
        result_dict['storyType'] = "Audiobook 🎧"
        return JsonResponse({"response": result_dict})
    else:
        if choiced_book_style == BOOK_TYPE["COLORING_BOOK"]:
            char_looks_guide = coloring_book_character_looks_guide
            char_prompt = coloring_book_human_character_looks_prompt if "Human" in responses.charcter_type else ""
            result_dict["storyType"] = "Coloring Book 🎨📖"
        else:
            char_looks_guide = character_looks_guide
            char_prompt = human_character_looks_prompt if "Human" in responses.charcter_type else ""
            result_dict["storyType"] = "eBook Story 🖼️"
        
        story_charachter = prompt_generation(char_looks_guide, char_prompt + text_response).replace(',', '').replace('.',',')

        response_dict = image_generation(story_charachter, input_fields, responses.charcter_type, name, text_response, "coloring_book" if choiced_book_style == BOOK_TYPE["COLORING_BOOK"] else "" )
        print("story_charachter ", story_charachter)
        
        result_dict["response_dict"] = response_dict
        
    # result_dict = {'response_dict': {1: {'image': 'media/images/1.png', 'text': "Tiago the Tiger was known for his wit and charm, but he had a peculiar habit of telling lies. One day, Tiago found himself in a sticky situation when he accidentally knocked over a vase in the village market. Instead of owning up to his mistake, he blamed it on a mischievous monkey. The villagers were kind-hearted and forgave Tiago, but the guilt gnawed at him. Tiago realized that dishonesty only brought temporary relief and decided to change his ways. From that day forward, Tiago became an honest tiger, always owning up to his mistakes and admitting the truth, no matter how difficult it was. Tiago's new found honesty earned him the respect and trust of all the animals in the forest."},2: {'image': 'media/images/A Brave Human 🦸‍♂️Ahana2023-09-05-17-55-55.5647571.png', 'text': "Tiago the Tiger was known for his wit and charm, but he had a peculiar habit of telling lies. One day, Tiago found himself in a sticky situation when he accidentally knocked over a vase in the village market. Instead of owning up to his mistake, he blamed it on a mischievous monkey. The villagers were kind-hearted and forgave Tiago, but the guilt gnawed at him. Tiago realized that dishonesty only brought temporary relief and decided to change his ways. From that day forward, Tiago became an honest tiger, always owning up to his mistakes and admitting the truth, no matter how difficult it was. Tiago's new found honesty earned him the respect and trust of all the animals in the forest."}}, 'storyType': 'Coloring Book 🎨📖','output_path':'/static/result_audios/output.mp3'}
    # print(result_dict)
    final_response = result_dict
    Response.objects.create(
        unique_id=unique_id,
        genated_content=1,
        response_id=form_response_id,
        story_text=final_response,
    )
    return JsonResponse({"response": final_response})


def image_generation(story_charachter,input_fields,character_type,name,text_response,book_type):
    count = 0
    response_dict = {}
    seed_number = random.randint(100000, 999999)
    engine_id = "stable-diffusion-xl-1024-v0-9"#"stable-diffusion-xl-beta-v2-2-2"#"stable-diffusion-v1-5"
    
    api_host = os.getenv('API_HOST', 'https://api.stability.ai')

    api_key = os.getenv("STABILITY_API_KEY")
    if api_key is None:
        raise Exception("Missing Stability API key.")

    for story_text in text_response.splitlines():
        if len(story_text) > 50:
            summarize_text = prompt_generation(story_summary_guide, story_text).replace(',', '').replace('.', ',')
            count += 1
            if book_type == "coloring_book":
                image_prompt = coloring_book_image_generation_prompt.format(
                    input_fields=input_fields,
                    charachter_description=story_charachter,
                    scene_description=summarize_text,
                    )
            else:
                image_prompt = image_generation_prompt.format(
                    input_fields=input_fields,
                    charachter_description=story_charachter,
                    scene_description=summarize_text,
                    )
            
            response = requests.post(
            f"{api_host}/v1/generation/{engine_id}/text-to-image",
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Authorization": f"Bearer {api_key}"
            },
            json={
            "text_prompts": [{"text": image_prompt}],
            "prompt_strength":0.7,
            "num_inference_steps":250 if book_type == "coloring_book" else 150,
            "refine":"Expert_ensemble_refiner",
            "scheduler":"DPMSolverMultistep",
            "num_outputs":1,
            "guidance_scale":7.5,
            "high_noise_frac":0.8,
            "seed":seed_number,
            "negative_prompt":"(Out of frame), Missing head, extra feet, poorly drawn feet, mutated feet, deformed feet, missing feet, mutated hands, poorly drawn hands, missing arms, extra hand, deformed hands, extra fingers, fused fingers, too many fingers, deformed fingers, muted fingers, poorly drawn fingers, mutated fingers, deformed eyes, deformed iris, ugly teeth, bad teeth, poorly drawn teeth, lazy eye, ugly eye, squint eye, poorly drawn eye, bad eye, lowres, text, error, cropped, worst quality, low quality, jpeg artefacts, ugly, duplicate, morbid, mutilated, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, extra feet, extra limbs, extra people, extra person, missing leg, missing limb, deformed legs, mutated legs,"
            },
            )
            if response.status_code != 200:
                return {"error": str(response.text)}
            data = response.json()
            current_time=str(datetime.now()).replace(' ','-').replace(':','-')
            for i, image in enumerate(data["artifacts"]):
                with open(media_path+"/images/"+character_type+str(name)+current_time+str(count)+".png", "wb") as f:
                    f.write(base64.b64decode(image["base64"]))
            response_dict[count] = {"image": "media/images/"+character_type+str(name)+current_time+str(count)+".png", "text": story_text}
    return response_dict



def voice_narration(text_response,voice):
    CHUNK_SIZE = 1024
    voice_id = LATESTVOICES[voice]
    url = "https://api.elevenlabs.io/v1/text-to-speech/"+voice_id
    
    headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": os.environ.get('ELEVENLABS_API_KEY')
    }
    
    data = {
    "text": text_response,
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.5
    }
    }
    
    if os.path.exists(r'media\result_audios'):
        pass
    else:
        os.mkdir(r'media\result_audios')
    
    response = requests.post(url, json=data, headers=headers)
    if response.status_code != 200:
        return {"error": str(response.text)}
    file_name = 'output_'+str(datetime.now()).replace(' ','-').replace(':','-')+'.mp3'
    file_path = 'media/result_audios/'+file_name
    with open(file_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)
    return file_path


def openai_response(prompt):
    response = openai.ChatCompletion.create(
      model="gpt-4",
      messages=[
          {"role": "system", "content":" You are the world's greatest ghost writer and you can mimic the writing style of any famous author without plagiarisma or infringing IP and copyright."},
          {"role": "user", "content": prompt},
      ]
    )
    return response.choices[0].message.content


def prompt_generation(guidance,prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature= 1,
        max_tokens= 1050,
        top_p= 1,
        frequency_penalty= 0.75,
        presence_penalty= 0,
        messages=[
                {"role": "system", "content": guidance},
                {"role": "user", "content": prompt},
            ]
        )
    return response.choices[0].message.content


### First Response Generation view

def openai_api(request, prompt, *args, **kwargs):
    seed_number = random.randint(100000, 999999)
    character_prompt = None
    param = request.GET
    story_summary_guide = "Act as prompt engineer who specialises in prompting for stable diffusion who converts this scene to a single prompt in less than 20 words. Remember stable diffusion works best with keywords to describe the scene. Don't include any words that are not suitable for image generation."
    character_looks_guide = "Act as prompt engineer who specialises in prompting for stable diffusion and generate physical looks description from the story in less than 10 words. Remember stable diffusion works best with keywords to describe the scene. Don't include any words that are not suitable for image generation."

    if param["character"] == "human":
        name = param["human_name"]
        ai_prompt = """Channel the captivating writing style of {} as you craft an enchanting tale for children.This story should cater to children within the age group of {}. Your narrative, set in the vivid world of {}, should span 10 paragraphs, with each paragraph containing approximately 100 words.
        The protagonist of your story is a {} character named {}, who is {} years old and of {} ethnicity. Weave the tale in a way that by the end, readers would glean the moral: '{}'.
        Your words should echo the rich descriptions, imaginative storytelling, and compelling character development that are signature to {} work.
        For the age group {}, please follow these guidelines:
        - **If the age group is 3-5**, focus on simple, concrete language, short sentences, and clear narratives. The story should be straightforward, with lots of repetition and basic vocabulary.
        - **If the age group is 6-8**, the story can be slightly more complex, with a clear structure. Introduce humor and themes exploring their experiences and feelings.
        - **If the age group is 9-12**, introduce more complex narratives and deeper themes. Use more abstract concepts and explore different perspectives.
        - **If the age group is 13-15**, the story can handle mature themes and complex narratives. Explore subtlety and nuance, challenge perspectives, and delve into complex emotions.
        - **If the age group is 16+**, the story can handle adult-level complexity in narratives and themes, but the content should still be appropriate for young adults.
        """.format(param["writing_style"],param["readers_age_group"] , param["location"]
        ,param["gender"], param["human_name"], param["age"], param["ethnicity"], param["moral"], param["writing_style"],param["readers_age_group"])

        common_img_prompt = "Children's book style, {}-year-old {} named {} has {} ethnicity, set in a  {},"\
        .format(param["age"],param["gender"].strip(),  param["human_name"].strip(), param["ethnicity"].strip(), param["location"].strip())

        character_prompt = """Give me a character physical looks description from the story  in less than 10 words.For example this could be a boy dressed as a superhero with messy blonde hair or a girl who is a magical fairy with red hair and freckles etc, don't include charachter name in this, Don't include any words that are not suitable for image generation:"""  # noqa: E501
    else:
        name = param["animal_name"].strip()
        ai_prompt = """Channel the captivating writing style of {} as you craft an enchanting tale for children. This story should cater to children within the age group of {}. Your narrative, set in the vivid world of {}, should span 10 paragraphs, with each paragraph containing approximately 100 words.
        The protagonist of your story character named {}, who is {}. Weave the tale in a way that by the end, readers would glean the moral: '{}'.
        Your words should echo the rich descriptions, imaginative storytelling, and compelling character development that are signature to {} work. For the age group {}, please follow these guidelines:
        - **If the age group is 3-5**, focus on simple, concrete language, short sentences, and clear narratives. The story should be straightforward, with lots of repetition and basic vocabulary.
        - **If the age group is 6-8**, the story can be slightly more complex, with a clear structure. Introduce humor and themes exploring their experiences and feelings.
        - **If the age group is 9-12**, introduce more complex narratives and deeper themes. Use more abstract concepts and explore different perspectives.
        - **If the age group is 13-15**, the story can handle mature themes and complex narratives. Explore subtlety and nuance, challenge perspectives, and delve into complex emotions.
        - **If the age group is 16+**, the story can handle adult-level complexity in narratives and themes, but the content should still be appropriate for young adults.
        """.format(param["writing_style"],param["readers_age_group"] ,param["location"],
                                    param["animal_name"].strip(), param["animal_type"].strip(), param["moral"].strip(),param["writing_style"],param["readers_age_group"])

        common_img_prompt = "Children's book style, animal character {} with background {}".format(param["animal_type"].strip(), param["location"] )

        story_charachter = "A {} named {}".format(param["animal_type"].strip(),param["animal_name"].strip())

    text_response = openai_response(ai_prompt)
    # output_path = voice_narration(text_response,param['audio'])
    print(text_response)
    if character_prompt:
        story_charachter = prompt_generation(character_looks_guide,character_prompt+text_response).replace(',','').replace('.',',')
        print("story_charachter ",story_charachter)

    count = 0
    engine_id = "stable-diffusion-xl-1024-v0-9"#"stable-diffusion-xl-beta-v2-2-2"#"stable-diffusion-v1-5"
    response_dict = {}
    result_dict = {}
    api_host = os.getenv('API_HOST', 'https://api.stability.ai')

    api_key = os.getenv("STABILITY_API_KEY")
    if api_key is None:
        raise Exception("Missing Stability API key.")

    for story_text in text_response.splitlines():
        if len(story_text) > 50:
            count += 1
            if count == 1:
                image_prompt = "{} {} {}".format(common_img_prompt,story_charachter ,last_prompt_text)
                response = requests.post(
                f"{api_host}/v1/generation/{engine_id}/text-to-image",
                headers={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "Authorization": f"Bearer {api_key}"
                },
                json={
                "text_prompts": [
                    {
                        "text": image_prompt
                    }
                ],
                "height":1024,
                "width":1024,
                "steps": 75,
                "prompt_strength":7,
                "seed":seed_number,
                },
                )
            else:
                summarize_text = prompt_generation(story_summary_guide,story_text).replace(',','').replace('.',',')
                image_prompt = "{} {} {} {}".format(common_img_prompt,story_charachter, summarize_text ,last_prompt_text)
                response = requests.post(
                f"{api_host}/v1/generation/{engine_id}/text-to-image",
                headers={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "Authorization": f"Bearer {api_key}"
                },
                json={
                    "text_prompts": [
                        {
                            "text": image_prompt
                        }
                    ],
                    "height":1024,
                    "width":1024,
                    "steps": 75,
                    "prompt_strength":7,
                    "seed":seed_number,
                    "negative_prompt":"out of frame, lowres, text, error, cropped, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck, username, watermark, signature, heads wrong way, legs back to front, missing arms, extra hand, deformed hands, deformed fingers, muted fingers, mutated hands, eyes covered, extra feet, extra limbs, glasses, spectacles, face masks, face paint, items on face, body parts in walls, people in walls, hands in walls, extra people, extra person, missing legs, deformed legs, mutated legs,"
                    # "negative_prompt":"bad nose, poorly drawn nose, cropped, out of frame, missing legs, missing limbs, bad mouth, poorly drawn mouth, poorly drawn chin, missing eye, bad eyes, poorly drawn eyes, poorly drawn wings, bad wings, Ugly, Disfigured, Deformed, Text, Watermark, Signature, Disproportionate, Bad proportions, Gross proportions, Bad anatomy, Duplicate, Extra legs, Extra limbs"
                    },
                )
            if response.status_code != 200:
                return JsonResponse({"error": str(response.text)})
            data = response.json()
            current_time=str(datetime.now()).replace(' ','-').replace(':','-')
            for i, image in enumerate(data["artifacts"]):
                with open(media_path+"/images/"+param["character"]+str(name)+current_time+str(count)+".png", "wb") as f:
                    f.write(base64.b64decode(image["base64"]))
            response_dict[count] = {"image": "media/images/"+param["character"]+str(name)+current_time+str(count)+".png", "text": story_text}
            result_dict['response_dict'] = response_dict
            result_dict['background'] = param['background']
            # result_dict['output_path'] = output_path
    # result_dict = {'response_dict': {1: {'image': 'media/images/1.png', 'text': "Tiago the Tiger was known for his wit and charm, but he had a peculiar habit of telling lies. One day, Tiago found himself in a sticky situation when he accidentally knocked over a vase in the village market. Instead of owning up to his mistake, he blamed it on a mischievous monkey. The villagers were kind-hearted and forgave Tiago, but the guilt gnawed at him. Tiago realized that dishonesty only brought temporary relief and decided to change his ways. From that day forward, Tiago became an honest tiger, always owning up to his mistakes and admitting the truth, no matter how difficult it was. Tiago's new found honesty earned him the respect and trust of all the animals in the forest."}}, 'background': 'url("http://127.0.0.1:8000/static/assets/img/setting3.jpg")','output_path':'/static/result_audios/output.mp3'}
    print(result_dict)
    return JsonResponse({"response": result_dict})



