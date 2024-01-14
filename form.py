import cohere
co = cohere.Client('ISZTWo9YqEizcG710vFjlUgCyIVZF6wCJUUwLLEX') #This is my Cohere API key. If expired, make a new key and replace

#Below is where you can paste any resume as a string. (You will replace this part with your code, so that the prgram inputs your string instead of this hard coded one)

#Function that intakes the string resume, and outputs a list of strings that are the responses to fill the form with
def write_post(resume):
    # Define your prompts - keeping as long answers for now, we will fix later
    prompts = [
        f'Pretend you are me. Based on my resume, what are your strengths  \"{resume}\"',
        f'Pretend you are me. Based on my resume, What are some of your experiences?   \"{resume}\"',
        f'Pretend you are me. Based on my resume, Why do you want to work at Cohere? \"{resume}\"',
        f'Pretend you are me.  Based on my resume, What is an example of a challenge you face? \"{resume}\"',
        f'Pretend you are me. Based on my resume, What is your tech stack? \"{resume}\"'
    ]

    responses = []
    for prompt in prompts:
        try:
            # Generate response from the model
            response = co.generate(
                model='command',
                prompt=prompt,
                max_tokens=100,
                temperature=0.9,
                k=0,
                p=0.75,
                frequency_penalty=0,
                presence_penalty=0,
                stop_sequences=[],
                return_likelihoods='NONE'
            )
            # Append the generated text to the responses list
            # for g in response.generations:
            #      print("For loop")
            #      print(g)
            responses.append(response.generations[0].text.strip())

        except Exception as e:
            # Handle any exceptions (e.g., API errors)
            responses.append(f"Error generating response for prompt: {prompt}. Error: {str(e)}")

    answers = [response.replace('\n', ' ') for response in responses]
    return answers

def form_filler(answers):

  #following code is used for filling out the form :
  
  formlink = input("Enter the form link: ")
  
  formlink = formlink + "?usp=pp_url" #if they get the ending already fix
  for i in range(len(answers)):
    tempList = answers[i].split(" ")
    answers[i] = "+".join(tempList)
  
  questions = ["entry.1299976051", "entry.1550187157", "entry.1472121668", "entry.639995429", "entry.2045628772"]
  
  for i in range(len(questions)):
    formlink = formlink + "&" + questions[i] + "=" + answers[i]
  
  print(answers)
  print("New Form Link: " + formlink)
