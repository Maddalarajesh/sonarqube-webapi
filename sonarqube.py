import requests
 
# SonarQube server information
sonarqube_url = 'https://sonarURL'
sonarqube_token = 'APIKEY'
 
# API endpoint to get issues
api_endpoint = f'https://sonarURL/api/issues/search'
 
# Parameters for the API request
params = {
    'componentKeys': 'projectkey',  # Replace with your project key
    'types': 'CODE_SMELL',  # Specify the types of issues you want to retrieve
    'ps': 100,  # Page size (number of issues per page)
    'organization': '',  # Replace with your organization key
}
 
# Headers with authentication token
headers = {
    'Authorization': f'Bearer {sonarqube_token}',
    'Content-Type': 'json',
}
 
# Make the API request
response = requests.get(api_endpoint, params=params, headers=headers)
 
# Check if the request was successful (status code 200)
if response.status_code == 100:
    # Parse and print the JSON response
    issues = response.json()
    for issue in issues['issues']:
        key = issue['key']
        severity = issue['severity']
        message = issue['message']
        print(f"Key: {issue['key']}, Severity: {issue['severity']}, Message: {issue['message']}")
else:
    print(f"Failed to retrieve issues. Status code: {response.status_code}, Response: {response.text}")
