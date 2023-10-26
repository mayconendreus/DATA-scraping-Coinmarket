# DATA-scraping-Coinmarket
The provided code is a Python script that makes use of the requests library to fetch data from the CoinMarketCap API. This script retrieves information about the latest cryptocurrency listings and extracts the top 10 trading coins based on their 24-hour trading volume in USD.

Here's a breakdown of the code:

Import necessary libraries:

import requests: This line imports the requests library, which is commonly used for making HTTP requests in Python.
import json: This line imports the json library for working with JSON data.
Define the API URL and parameters:

url: This variable contains the URL of the CoinMarketCap API for fetching cryptocurrency data.
parameters: This dictionary contains the parameters to be sent with the API request. It specifies the start, limit, currency conversion, and sorting options.
Set headers:

headers: This dictionary contains the headers to be sent with the API request. It includes an 'Accepts' header and an 'X-CMC_PRO_API_KEY' header. You should replace 'YOUR_API' with your actual CoinMarketCap API key.
Make the API request:

The script uses a try block to handle potential exceptions.
It sends an HTTP GET request to the specified URL (url) with the parameters and headers specified.
It stores the response in the response variable.
Parse the response:

The response content is assumed to be in JSON format, so the script uses json.loads() to parse the JSON response into a Python dictionary, and it is stored in the data variable.
Extract the top 10 trading coins:

The script initializes an empty list top_coins to store the top trading coins.
It iterates through the cryptocurrency data in data['data'] and extracts the symbol and 24-hour trading volume for each coin.
It limits the list to the top 10 coins based on trading volume.
The results are stored in the top_coins list.
Print the top 10 coins:

The script iterates through the top_coins list and prints the coin symbol and its 24-hour trading volume in USD.
Exception handling:

The script handles potential exceptions related to the requests library, such as ConnectionError, Timeout, and TooManyRedirects. If any of these exceptions occur, it prints the error message.
Note: To run this code successfully, you should replace 'YOUR_API' in the headers dictionary with your actual CoinMarketCap API key. Also, make sure you have the requests library installed in your Python environment.





