from PIL import Image
import os, random, json, time

start = time.time()
def save_object(data, number):
    with open(f"db/{number}.json", "w") as f:
        json.dump(data, f)

nfts = []
traits = os.listdir("InputLayers")
traits.sort()
description = "A fellow Slim Sapien"
y = 0
while y<1000:
    properties = {}
    for x in traits:
        layer = os.listdir(f"InputLayers/{x}")
        picked_layer = random.choice(layer)[:-4]
        properties[x[3:]] = picked_layer
##############EXCEPTIONS###########################################################################################################################
    if properties["EyeBalls"] == "Closed":
        properties["Iris"] = "None"
    if properties["Beard"] == "Black" and properties["Acne"] == "Black":
        for trait in traits:
            if trait.endswith("Acne"):
                layer = os.listdir(f"InputLayers/{trait}")
                break
        layer.remove("Black.png")
        picked_layer = random.choice(layer)[:-4]
        properties["Acne"] = picked_layer
    if properties["EyeBalls"] == "BloodEye" and properties["Iris"] == "Red":
        for trait in traits:
            if trait.endswith("Iris"):
                layer = os.listdir(f"InputLayers/{trait}")
                break
        layer.remove("Red.png")
        picked_layer = random.choice(layer)[:-4]
        properties["Iris"] = picked_layer
###################################################################################################################################################
    isValid = True
    for nft in nfts:
        if properties == nft:
            isValid = False
            y -= 1
            break
    if isValid:
        nfts.append(properties)
    y += 1
    
print(len(nfts))
for nft in nfts:
    trait0 = traits[0][3:]
    trait0_value = nft.get(trait0)
    img0 = Image.open(f"InputLayers/{traits[0]}/{trait0_value}.png")
    name = f"The Slim Sapien #{nfts.index(nft)}"
    attributes = [
        {
            "trait_type": trait0,
            "value": trait0_value
        }
    ]
    for trait_number in range(len(nft)):
        if trait_number + 1 != len(nft):
            trait = traits[trait_number+1][3:]
            trait_value = nft.get(trait)
            img1 = Image.open(f"InputLayers/{traits[trait_number+1]}/{trait_value}.png")
            img0 = Image.alpha_composite(img0, img1)
            if trait_value != "None":
                attribute = {
                    "trait_type": trait,
                    "value": trait_value
                }
                attributes.append(attribute)
            
    metadata = {
        "name": name,
        "description": description,
        "image": "Change this",
        "attributes": attributes 
    }
    img0.save(f"output/{nfts.index(nft)}.png")
    save_object(metadata, nfts.index(nft))

end = time.time()
print(f"Runtime: {end - start}")