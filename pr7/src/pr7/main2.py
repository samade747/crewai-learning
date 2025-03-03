from crewai.flow.flow import Flow, start, listen
from litellm import completion

API_KEY = "AIzaSyBwQb-b28zgXxy8C9wMivFCWjlg-tbxabA"

class CityFunFact(Flow):


    @start()
    def generate_random_city(self):
        return = completion(
            model="gemini/gemini-1.5-pro",
            api_key=API_KEY,
            messages=[{                
                "content": "Generate a random city name and return it as a string.",
                "role": "user"
            }]
        )
        print(result['choices'][0]['message']['content'])



def kickoff():
    obj = CityFunFact()
    obj.kickoff()


    48:51