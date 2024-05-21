import json

with open('../bxss-lbs37/data/final-eval.json', 'r') as file:
    evalData = json.load(file)

with open('active-test.json', 'r') as file:
    activeTest = json.load(file)

with open('all-test.json', 'r') as file:
    allTest = json.load(file)

gfr_distribution = evalData.get('gfr_distribution', [])

print("Length of gfr_distribution array:", len(gfr_distribution))

base_urls = {item['baseUrl']: idx for idx, item in enumerate(allTest)}
path_to_test_id = {item['path']: item['test_id'] for item in activeTest}

#for base_url in base_urls:
#    if base_url in path_to_test_id:
#        print(f'Base URL: {base_url} -> Test ID: {path_to_test_id[base_url]}')
#    else:
#        print(f'Base URL: {base_url} -> Test ID: Not found')


for index, element in enumerate(gfr_distribution):
    if element == 1:
	#print(f'GFR Index: {index} | Test ID: {path_to_test_id[base_url]}')
        #print("GFR Index:", index, "TEST ID:", path_to_test_id[allTest[index]['baseUrl']], "Pass")
        baseUrl = allTest[index]['baseUrl']
        if baseUrl in path_to_test_id:
            print("GFR Index:", index, "TEST ID:", path_to_test_id[baseUrl])
        else:
            print("GFR Index:", index, "No ID: ", baseUrl)

