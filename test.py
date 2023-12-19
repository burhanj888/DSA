from openai import OpenAI

# Set your OpenAI API key
# openai.api_key = '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'
client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="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",
)
# import openai

# # Set your OpenAI API key
# api_key = 'YOUR_API_KEY'
# openai.api_key = api_key

# Example prompt
prompt = 'Translate the following English text to French: "hello"'

# Make a request to the API
response = client.chat.completions.create(
  model="text-davinci-003",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ],
  max_tokens=50
)

# Extract and print the generated text
generated_text = response['choices'][0]['message']['content']
print(generated_text)