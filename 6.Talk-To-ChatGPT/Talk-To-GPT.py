
import openai

openai.api_key = 'your-api-key'


chat=input('what would you like to talk about today?')
chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
 messages=[{"role": "user", "content": f"{chat}"}])