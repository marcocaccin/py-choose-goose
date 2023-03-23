#! /usr/bin/env python3

import os

import openai
from rich.console import Console
from rich.markdown import Markdown


openai.api_key = os.getenv("OPENAI_API_KEY")
SYSTEM_PROMPT_DEFAULT = {"role": "system", "content": "You are a helpful assistant. Answer concisely when possible."}
RESET_QUERY = "!RESET"
QUIT_QUERY = "!QUIT"


if __name__ == "__main__":
    console = Console()
    
    prompt = []
    system_prompt = input(
        "System prompt (e.g., 'You are a helpful assistant. Answer concisely when possible.'):\n"
        ).strip()
    if system_prompt:
        prompt.append({"role": "system", "content": system_prompt.strip()})
    
    while True:
        user_query = input("User:\n").strip()
        if user_query == RESET_QUERY:
            prompt = [dict(prompt[0])] if prompt[0]["role"] == "system" else []
            continue
        if user_query == QUIT_QUERY:
            break

        prompt.append({"role": "user", "content": user_query})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=prompt,
        )
        assistant_message = response.choices[0]["message"]
        prompt.append(assistant_message)
        console.print(Markdown(assistant_message["content"]))
