import openai
import settings

openai.api_key = settings.chat_api_key

_model = [
    {"model": "text-davinci-003", "max_tokens": 4000},
    {"model": "text-curie-001", "max_tokens": 2048},
    {"model": "text-babbage-001", "max_tokens": 2048},
    {"model": "text-ada-001", "max_tokens": 2048},
]
model = _model[0]


async def chatgpt(prompt):
    # prompt = input(restart_sequence)
    try:
        response = openai.Completion.create(
            model=model['model'],
            prompt=prompt,
            temperature=0,
            max_tokens=model['max_tokens'] - 200,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        return response["choices"][0]["text"].strip()
    except Exception as exc:
        return exc
