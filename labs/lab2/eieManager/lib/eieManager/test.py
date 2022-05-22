#import uvicorn
import json
jsonPath = "../../../sensors_cfg.json"
#jsonObject = none


def main():
    """
    Device Manager application main function.
    """
 #   uvicorn.run("eieManager.ServerAPI.main:app")
    open_json(jsonPath)

def open_json(path):

    with open(path) as jsonFile:
        jsonObject = json.load(jsonFile)
    
    """
    Open json file to manage the devices info
 
    :param path: Json location.
    """

def create_device():
    json_data = {
        "product":"Python book",
        "overall":"4.0",
        "text":"Nice book"
    }
    with open('writed_json.json', 'w') as jsonFile:
    json.dump(json_data, jsonFile)
    jsonFile.close()


    
def close_json(path):
    """
    Close json file
 
    :param path: Json location.
    """
    jsonFile.close()


if __name__ == "__main__":
    main()



#product = jsonObject['product']
#overall = jsonObject['overall']
#text = jsonObject['text']

