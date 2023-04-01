# Github Repo Search
a Python program that takes a keyword as input, searches it on GitHub using the GitHub REST API, and returns all the repositories that contain the keyword

This program first prompts the user to enter a keyword to search on GitHub. It then constructs the URL for the GitHub REST API search endpoint with the keyword as the search query. It sends a GET request to the URL using the requests library and checks the response status code.

If the status code is 200 (OK), the program parses the response JSON data and extracts the total count of repositories found. If the total count is zero, it prints a message saying that no repositories were found. Otherwise, it loops through the items array in the response data and prints the full name and description of each repository.

If the status code is not 200, the program prints a message saying that it failed to retrieve repositories.
