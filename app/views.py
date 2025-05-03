from django.shortcuts import render

from project.settings import API_KEY
from .forms import PromptForm
from project.settings import API_KEY

import openai
openai.api_key = ''
client = openai.OpenAI(api_key=API_KEY)


def home(request):
    response_text = None
    response_image = None

    if request.method == 'POST':
        form = PromptForm(request.POST)
        # is_valid
        if form.is_valid():
            prompt = form.cleaned_data['prompt']

        completion = client.chat.completions.create(
            model="gpt-4.1",
            messages=[
                {"role": "developer", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        response_text = completion.choices[0].message.content

        # generate_image
        # model 'dall-e-3'
        image_result = client.images.generate(
            model="dall-e-3",
            prompt='cat in pool'
        )

        response_image = image_result.data[0].url

        # model "gpt-image-1"
        # image_result = client.images.generate(
        #     model="gpt-image-1",
        #     prompt=prompt
        # )
        #
        # image_base64 = image_result.data[0].b64_json
        # response_image = image_base64.b64decode(image_base64)

    else:
        form = PromptForm()

    return render(request, 'home.html', {
        'form': form,
        'response_text': response_text,
        'response_image': response_image,
    })

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # або інша сторінка
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})