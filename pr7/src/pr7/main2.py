from crewai.flow.flow import Flow, start, listen
from litellm import completion

API_KEY = "sk-1234567890"

class CityFunFact(Flow):


    @start()
    def generate_random_city(self):
        return = completion(
            model="gemini/gemini-1.5-pro",
            api_key=API_KEY,
            messages=[{                
                "content": "Generate a random city name and return it as a string."
            }]
        )
        print(result['choices'][0]['message']['content'])


