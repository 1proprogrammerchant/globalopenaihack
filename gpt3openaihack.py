import openai

# Get your OpenAI API key from https://openai.com/account
api_key = "YOUR_API_KEY"

# Create an OpenAI client
client = openai.Client(api_key=api_key)

# Generate a text response to a prompt
response = client.create("text", prompt="What is the meaning of life?")

# Print the response
print(response.choices[0].text)
