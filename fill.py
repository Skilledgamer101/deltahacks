import responses
import fill_helper

link = input("Please enter the link to Google Form")
questions = fill_helper.get(link)
answers = responses.write_post(questions)
fill_helper.fill(link, answers)
