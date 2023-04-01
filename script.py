import requests

keyword = input("Enter a keyword to search on GitHub: ")
url = f"https://api.github.com/search/repositories?q={keyword}"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    total_count = data["total_count"]
    if total_count == 0:
        print("No repositories found.")
    else:
        print(f"{total_count} repositories found:")
        for item in data["items"]:
            print(f"{item['full_name']}: {item['description']}")
else:
    print("Failed to retrieve repositories.")
