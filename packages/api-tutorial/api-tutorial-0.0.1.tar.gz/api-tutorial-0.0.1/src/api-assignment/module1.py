#!/usr/bin/env python3

# API to access various services via HTTP as a client. 
# For example, downloading data or interacting with a REST-based API

import argparse
import urllib.request
import json
import ssl

# Set the base URL for the API
base_url = "https://example.com/api/"

# Define the endpoints for the API
endpoints = {
    "users": "users/",
    "posts": "posts/",
    "comments": "comments/"
}

# Define a helper function to make API requests
def make_request(url, method="GET", data=None):
    try:
        request = urllib.request.Request(url)
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        with urllib.request.urlopen(request, context=context) as response:
            return response.read()
    except urllib.error.URLError as error:
        print(error)
        return None

# Define functions to handle each HTTP method
def api_get(endpoint, id=None):
    url = base_url + endpoints[endpoint]
    if id:
        url += str(id) + "/"
    return make_request(url)

def api_post(endpoint, data):
    url = base_url + endpoints[endpoint]
    return make_request(url, method="POST", data=data)

def api_put(endpoint, id, data):
    url = base_url + endpoints[endpoint] + str(id) + "/"
    return make_request(url, method="PUT", data=data)

def api_patch(endpoint, id, data):
    url = base_url + endpoints[endpoint] + str(id) + "/"
    return make_request(url, method="PATCH", data=data)

def api_delete(endpoint, id):
    url = base_url + endpoints[endpoint] + str(id) + "/"
    return make_request(url, method="DELETE")


# Define the main function to parse arguments and call API functions
def main():
    parser = argparse.ArgumentParser(description="API command-line client")
    parser.add_argument("method", choices=["get", "post", "put", "patch", "delete"], help="HTTP method to use")
    parser.add_argument("endpoint", choices=endpoints.keys(), help="API endpoint to use")
    parser.add_argument("-i", "--id", type=int, help="ID of resource to retrieve or update")
    parser.add_argument("-d", "--data", type=json.loads, help="JSON data to use in request body")
    args = parser.parse_args()

    # Call the appropriate API function based on the method and endpoint
    if args.method == "get":
        response = api_get(args.endpoint, id=args.id)
    elif args.method == "post":
        response = api_post(args.endpoint, data=args.data)
    elif args.method == "put":
        response = api_put(args.endpoint, id=args.id, data=args.data)
    elif args.method == "patch":
        response = api_patch(args.endpoint, id=args.id, data=args.data)
    elif args.method == "delete":
        response = api_delete(args.endpoint, id=args.id)

    # Print the response
    print(json.dumps(response, indent=4))

if __name__ == "__main__":
    main()