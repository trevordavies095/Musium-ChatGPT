import csv
import openai

def main():
    r = open_csv()
    albums = ""
    for k in r:
        albums += r[k] + "\n"

    chat_gpt(albums)


def chat_gpt(data):
    openai.api_key = ''

    prompt = """
        I want you to act as a music connoisseur. I will provide you a list of albums that I have listened to. Each album will have a score out of 100 that I have given to it. I want you to recommend me a handful of albums you think I would enjoy based on the albums I have listened to and the scores I have given them. Below is the list of albums.

        List of Albums:
        """ + data + """
        """

    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )

    generated_text = response.choices[0].text.strip()
    print(generated_text)



def open_csv():
    data = {}
    with open('musium.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line = 0
        for row in csv_reader:
            if line == 0:
                line+=1
                continue
            else:
                data[row["MusicBrainz ID"]] = "- \"" + row["Album"] + "\" by " + row["Artist"] + ", Score: " + row["Album Rating"]

    return data

if __name__ == "__main__":
    main()