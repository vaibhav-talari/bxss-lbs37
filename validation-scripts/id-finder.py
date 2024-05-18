import json

with open('active-test.json', 'r') as file:
    activeTest = json.load(file)

with open('all-test.json', 'r') as file:
    allTest = json.load(file)

# Create the base_urls dictionary
base_urls = {item['baseUrl']: idx for idx, item in enumerate(allTest)}

# Create the path_to_test_id dictionary
path_to_test_id = {item['path']: item['test_id'] for item in activeTest}

# Initialize the result array with None or another placeholder
result = [None] * len(base_urls)

# Populate the result array
for base_url, idx in base_urls.items():
    test_id = path_to_test_id.get(base_url)
    result[idx] = test_id

# Print the result array
print(result)