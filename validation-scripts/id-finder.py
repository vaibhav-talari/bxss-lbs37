import json

with open('active-test.json', 'r') as file:
    activeTest = json.load(file)

with open('all-test.json', 'r') as file:
    allTest = json.load(file)

base_urls = {item['baseUrl']: idx for idx, item in enumerate(allTest)}

path_to_test_id = {item['path']: item['test_id'] for item in activeTest}

result = [None] * len(base_urls)

for base_url, idx in base_urls.items():
    test_id = path_to_test_id.get(base_url)
    result[idx] = test_id

# Print the result array
print(result)