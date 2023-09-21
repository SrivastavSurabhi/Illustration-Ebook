story_summary_guide = "Act as prompt engineer who specialises in prompting for stable diffusion who converts this scene to a single prompt in less than 6 words. Remember stable diffusion works best with keywords to describe the scene. Don't include any words that are not suitable for image generation."# noqa: E501
coloring_book_story_summary_guide = "Act as prompt engineer who specialises in prompting for stable diffusion who converts this scene to a single prompt in less than 6 words. Remember stable diffusion works best with keywords to describe the scene. Don't include any words that are not suitable for image generation. Note that you will not mention colours in the description."# noqa: E501
character_looks_guide = "Act as prompt engineer who specialises in prompting for stable diffusion and generate physical looks description from the story in less than 6 words. Remember stable diffusion works best with keywords to describe the scene. Don't include any words that are not suitable for image generation."# noqa: E501
coloring_book_character_looks_guide = "Act as prompt engineer who specialises in prompting for stable diffusion and generate physical looks description from the story in less than 6 words. Remember stable diffusion works best with keywords to describe the scene. Don't include any words that are not suitable for image generation. Note that you will not mention colours in the description."# noqa: E501
human_character_looks_prompt = "Give me a character physical looks description from the story  in less than 6 words.For example this could be a boy dressed as a superhero with messy blonde hair or a girl who is a magical fairy with red hair and freckles etc, don't include charachter name in this, Don't include any words that are not suitable for image generation:\n"  # noqa: E501
coloring_book_human_character_looks_prompt = "Give me a character physical looks description from the story  in less than 6 words.For example this could be a boy dressed as a superhero with messy blonde hair or a girl who is a magical fairy with red hair and freckles etc, don't include charachter name in this, Don't include any words that are not suitable for image generation, Note that you will not mention colours in the description.:\n"  # noqa: E501
# last_prompt_text = "in a scene 8k rendered with vibrant colors and renderman,In the style of Pixar artists, CGI, Extremely Detailed."# noqa: E501


human_story_generation_prompt_new ="""
        Craft a story in the style of {}, set in the genre of {}, tailored for the age group of {}. The narrative, unfolding in the vibrant realm of {}, should comprise 2 paragraphs, each about 100 words.

        Introduce the protagonist: a {} named {}, aged {}, of {} descent. The tale should conclude with the moral: '{}'.

        Emulate {}'s hallmark descriptions, storytelling, and character depth.

        Guidelines based on {}:

        - **3-5 years**: 
        - Use simple language and short sentences.
        - Maintain a straightforward narrative with repetition.
        - **6-8 years**: 
        - Slightly more intricate structure.
        - Introduce humour and relatable themes.
        - **9-12 years**: 
        - Complex narratives and deeper themes.
        - Employ abstract concepts; show diverse viewpoints.
        - **13-15 years**: 
        - Mature themes are acceptable.
        - Delve into nuance and challenge conventional perspectives.
        - **16+ years**: 
        - Adult-level narrative complexity is permissible.
        - Ensure content remains youth-appropriate.

        """

animal_story_generation_prompt_new ="""
        Craft a story in the style of {}, set in the genre of {}, tailored for the age group of {}. The narrative, unfolding in the vibrant realm of {}, should comprise 10 paragraphs, each about 100 words.

        The story centers on {}, a {}. The narrative should embed the moral: '{}'.

        Emulate {}'s hallmark descriptions, storytelling, and character depth.

        Guidelines based on {}:

        - **3-5 years**: 
        - Use simple language and short sentences.
        - Maintain a straightforward narrative with repetition.
        - **6-8 years**: 
        - Slightly more intricate structure.
        - Introduce humour and relatable themes.
        - **9-12 years**: 
        - Complex narratives and deeper themes.
        - Employ abstract concepts; show diverse viewpoints.
        - **13-15 years**: 
        - Mature themes are acceptable.
        - Delve into nuance and challenge conventional perspectives.
        - **16+ years**: 
        - Adult-level narrative complexity is permissible.
        - Ensure content remains youth-appropriate.
        """


image_generation_prompt ="""{input_fields}, {charachter_description}, ({scene_description}),(beautiful eyes:2),(Masterpiece,8k,rendered with vibrant colors,award-winning 3d CGI,UHD,best quality),Disney-style."""
# animal_image_generation_prompt ="""{animal_input_fields}, ({scene_description}),(beautiful eyes:2),(Masterpiece,8k,rendered with vibrant colors,award-winning 3d CGI,UHD,best quality),Disney-style."""

coloring_book_image_generation_prompt = """{input_fields}, {charachter_description}, {scene_description}, colorless, b&w, coloring page, coloring book, Line Art Only, Coloring Book Style, simple illustration."""
# coloring_book_images_animal_prompt = """{animal_type}, set in a {location}, {scene_description}, colorless, b&w, coloring page, coloring book, Line Art Only, Coloring Book Style, simple illustration."""


human_poem_generation_prompt = """
        Compose a playful and witty poem in the style of {author}, inspired by the genre of {genre}. The poem should resonate with the age group of {readers_age_group} and transport readers to the world of {location}.

        Our star of the poem is a {gender} named {human_name}, aged {age}, of {ethnicity} descent. While crafting, keep in mind the essence of the moral: '{moral}' and infuse it subtly within the verses.

        Channel {author}'s distinctive voice, ensuring the poem's tone and style match the intended audience:

        - 3-5 years:
        - Use catchy rhymes and playful rhythms.
        - Keep verses short and full of vivid imagery.
        - 6-8 years:
        - Integrate humor and imaginative scenarios.
        - Make use of fun wordplay and relatable themes.
        - 9-12 years:
        - Weave in clever twists and unexpected turns.
        - Employ rich vocabulary, but maintain clarity.
        - 13-15 years:
        - Dive into more profound emotions and insights.
        - Use metaphor and simile to add depth.
        - 16+ years:
        - Sophistication in verse is encouraged.
        - However, ensure a touch of playfulness remains
"""

animal_poem_generation_prompt = """
        Compose a playful and witty poem in the style of {author}, inspired by the genre of {genre}. The poem should resonate with the age group of {readers_age_group} and transport readers to the world of {location}.

        Our star of the poem is a {animal_type} named {animal_name}. While crafting, keep in mind the essence of the moral: '{moral}' and infuse it subtly within the verses.

        Channel {author}'s distinctive voice, ensuring the poem's tone and style match the intended audience:

        - 3-5 years:
        - Use catchy rhymes and playful rhythms.
        - Keep verses short and full of vivid imagery.
        - 6-8 years:
        - Integrate humor and imaginative scenarios.
        - Make use of fun wordplay and relatable themes.
        - 9-12 years:
        - Weave in clever twists and unexpected turns.
        - Employ rich vocabulary, but maintain clarity.
        - 13-15 years:
        - Dive into more profound emotions and insights.
        - Use metaphor and simile to add depth.
        - 16+ years:
        - Sophistication in verse is encouraged.
        - However, ensure a touch of playfulness remains
"""





human_story_generation_prompt = """
        Channel the captivating writing style of {} as you craft an enchanting tale for children.This story should cater to children within the age group of {}. Your narrative, set in the vivid world of {}, should span 10 paragraphs, with each paragraph containing approximately 100 words.

        The protagonist of your story is a {} character named {}, who is {} years old and of {} ethnicity. Weave the tale in a way that by the end, readers would glean the moral: '{}'.

        Your words should echo the rich descriptions, imaginative storytelling, and compelling character development that are signature to {} work.
        For the age group {}, please follow these guidelines:
        - **If the age group is 3-5**, focus on simple, concrete language, short sentences, and clear narratives. The story should be straightforward, with lots of repetition and basic vocabulary.
        - **If the age group is 6-8**, the story can be slightly more complex, with a clear structure. Introduce humor and themes exploring their experiences and feelings.
        - **If the age group is 9-12**, introduce more complex narratives and deeper themes. Use more abstract concepts and explore different perspectives.
        - **If the age group is 13-15**, the story can handle mature themes and complex narratives. Explore subtlety and nuance, challenge perspectives, and delve into complex emotions.
        - **If the age group is 16+**, the story can handle adult-level complexity in narratives and themes, but the content should still be appropriate for young adults.
        """# noqa: E501

animal_story_generation_prompt = """
        Channel the captivating writing style of {} as you craft an enchanting tale for children.This story should cater to children within the age group of {}. Your narrative, set in the vivid world of {}, should span 10 paragraphs, with each paragraph containing approximately 100 words.
        
        The protagonist of your story character named {}, who is {}. Weave the tale in a way that by the end, readers would glean the moral: '{}'.
        
        Your words should echo the rich descriptions, imaginative storytelling, and compelling character development that are signature to {} work. 
        For the age group {}, please follow these guidelines:
        - **If the age group is 3-5**, focus on simple, concrete language, short sentences, and clear narratives. The story should be straightforward, with lots of repetition and basic vocabulary.
        - **If the age group is 6-8**, the story can be slightly more complex, with a clear structure. Introduce humor and themes exploring their experiences and feelings.
        - **If the age group is 9-12**, introduce more complex narratives and deeper themes. Use more abstract concepts and explore different perspectives.
        - **If the age group is 13-15**, the story can handle mature themes and complex narratives. Explore subtlety and nuance, challenge perspectives, and delve into complex emotions.
        - **If the age group is 16+**, the story can handle adult-level complexity in narratives and themes, but the content should still be appropriate for young adults.
        """# noqa: E501

