
import openai

openai.api_key = "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"

def test_animal_response(animal: str):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_prompt(animal),
        temperature=0.6,
    )
    return response.choices[0].text



def generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        animal.capitalize()
    )

if __name__ == "__main__":
    print(test_animal_response("bird"))