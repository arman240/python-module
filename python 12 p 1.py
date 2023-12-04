import requests

def get_random_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    if response.status_code == 200:
        joke_data = response.json()
        return joke_data.get("value")
    else:
        return None

def main():
    chuck_norris_joke = get_random_chuck_norris_joke()

    if chuck_norris_joke:
        print("Random Chuck Norris Joke:")
        print(chuck_norris_joke)
    else:
        print("Failed to fetch Chuck Norris joke.")

if __name__ == "__main__":
    main()
