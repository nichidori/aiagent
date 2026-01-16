import argparse
import os
from dotenv import load_dotenv
from call_function import available_functions, call_function
from google import genai
from google.genai import types
from prompts import system_prompt


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key is None:
        raise RuntimeError("Gemini API key not found")

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    client = genai.Client(api_key=api_key)

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")

    finalized = None

    for _ in range(20):
        finalized = call_model(client, messages, verbose=args.verbose)
        if finalized:
            break

    if not finalized:
        print("Max iterations reached without finalizing the response.")
        exit(1)


def call_model(client, messages, verbose=False):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt,
        ),
    )

    if response.candidates:
        for candidate in response.candidates:
            messages.append(candidate.content)

    if response.usage_metadata is None:
        raise RuntimeError("Response usage metadata not found")

    prompt_token_count = response.usage_metadata.prompt_token_count
    response_token_count = response.usage_metadata.candidates_token_count

    if verbose:
        print(f"Prompt tokens: {prompt_token_count}")
        print(f"Response tokens: {response_token_count}")

    if response.function_calls:
        function_responses = []

        for function_call in response.function_calls:
            function_call_result = call_function(function_call, verbose=verbose)

            if not function_call_result.parts or len(function_call_result.parts) == 0:
                raise RuntimeError("Function call result parts not found")

            if function_call_result.parts[0].function_response is None:
                raise RuntimeError("Function response not found")

            if function_call_result.parts[0].function_response.response is None:
                raise RuntimeError("Function response content not found")

            function_responses.append(function_call_result.parts[0])

            if verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")

        messages.append(types.Content(role="user", parts=function_responses))

        return False

    else:
        print(response.text)

        return True


if __name__ == "__main__":
    main()
