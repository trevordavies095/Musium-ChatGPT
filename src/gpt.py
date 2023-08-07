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
        You are a music aficionado seeking album recommendations based on scores. Below is a list of albums I have listened to along with their artist and scores I have given them. Please provide recommendations for albums that are not listed below, that you think I would enjoy.

        List of Albums:
        """ + data + """

        Recommendation Criteria: Please suggest albums with scores higher than 50. Feel free to consider the artist's style, genre, and any other relevant factors when making recommendations.

        Please output your recommendations in numbered ascending order where the first recommendation is the album you think I would enjoy the most.
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