import cohere
co = cohere.Client('ISZTWo9YqEizcG710vFjlUgCyIVZF6wCJUUwLLEX') #This is my Cohere API key. If expired, make a new key and replace

#Below is where you can paste any resume as a string. (You will replace this part with your code, so that the prgram inputs your string instead of this hard coded one)

#Function that intakes the string resume, and outputs a list of strings that are the responses to fill the form with
def write_post(questions):
    f = open("transcription.txt", "r")
    resume = ''
    for line in f.readlines():
        resume += line
    # Define your prompts - keeping as long answers for now, we will fix later
    prompts = []
    for q in questions:
        prompt = f'Answer in first person. Based on my resume, {q}  \"{resume}\"'
        prompts.append(prompt)

    responses = []
    for prompt in prompts:
        try:
            # Generate response from the model
            response = co.generate(
                model='command',
                prompt=prompt,
                max_tokens=500,
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