import cohere
key = input("Please enter your Cohere API key")
co = cohere.Client(key) #This is the Cohere API key. If expired, make a new key and replace

#Function that intakes the list of string questions, and outputs a list of strings that are the responses to fill the form with based on the transcription file of resume
def write_post(questions):
    f = open("transcription.txt", "r")
    resume = ''
    for line in f.readlines():
        resume += line
    # Define your prompts - keeping as long answers for now
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

            responses.append(response.generations[0].text.strip())

        except Exception as e:
            # Handle any exceptions (e.g., API errors)
            responses.append(f"Error generating response for prompt: {prompt}. Error: {str(e)}")

    answers = [response.replace('\n', ' ') for response in responses]
    return answers
