from functools import cache
from openai import AzureOpenAI


@cache
def get_client(azure_endpoint, api_key, api_version):
    return AzureOpenAI(
        azure_endpoint=azure_endpoint,
        api_key=api_key,
        api_version=api_version,
    )


@cache
def ask_openai(
    azure_endpoint,
    api_key,
    api_version,
    deployment_name,
    system_prompt,
    prompt,
    temperature=0,
):
    client = get_client(
        azure_endpoint=azure_endpoint,
        api_key=api_key,
        api_version=api_version,
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt},
    ]

    response = client.chat.completions.create(
        model=deployment_name,
        messages=messages,
        temperature=temperature,
    )

    return response.choices[0].message.content
