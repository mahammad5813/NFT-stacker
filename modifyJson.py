import json, os, time


mode = int(input('''
Choose a mode:
0 - Update baseURI
1 - Update custom key
>> '''))

if mode == 0:
    metadata_list = os.listdir("db")
    baseURI = input("Enter the baseURI: ")
    start = time.time()

    for x in range(len(metadata_list)):
        json_file = open(f"db/{x}.json", "r")
        json_obj = json.load(json_file)
        json_file.close()

        json_obj["image"] = f"ipfs://{baseURI}/{x}.png"
        json_file = open(f"db/{x}.json", "w")
        json.dump(json_obj, json_file)
    
    print(f"Updated the baseURI for images to >> ipfs://{baseURI}")

if mode == 1:
    key = input("Enter the key name: ").lower()
    key_value = input("Enter the key value: ")
    metadata_list = os.listdir("db")
    start = time.time()

    for x in range(len(metadata_list)):
        json_file = open(f"db/{x}.json", "r")
        json_obj = json.load(json_file)
        json_file.close()

        json_obj[key] = key_value
        json_file = open(f"db/{x}.json", "w")
        json.dump(json_obj, json_file)
    
    print(f"Updated the {key} key for images to >> {key_value}")

end = time.time()
print(f"The runtime: {end-start}")