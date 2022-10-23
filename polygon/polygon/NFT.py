from thirdweb import ThirdwebSDK
from thirdweb.types.nft import NFTMetadataInput
import os
import json 
import requests
import time 
f = open('polygon/config.json')
config_data = json.load(f)

PRIVATE_KEY = config_data['company_privateKey']
PUBLIC_KEY = config_data['company_publicKey']
THIRDWEB = config_data['company_thirdWeb']
projectID = config_data['IPFS_projectID']
secretKey = config_data['IPFS_secretKey']

NETWORK = "mumbai"
Path = './reviews_folder' + '/EXRXFZSZTK.json'

def NFT_mint(jsonFile, ipfs):
    # load_dotenv()
    # PRIVATE_KEY = os.getenv("PRIVATE_KEY")
    sdk = ThirdwebSDK.from_private_key(PRIVATE_KEY, NETWORK)
    contract = sdk.get_nft_collection(THIRDWEB)
    NFT_COLLECTION_ADDRESS = THIRDWEB
    nft_collection = sdk.get_nft_collection(NFT_COLLECTION_ADDRESS)
    companyName = json.load(open(jsonFile))["Organization"]
    nft_collection.mint(NFTMetadataInput.from_json({
        "name": companyName,
        "image": 'ipfs://' + ipfs,
    }))


def NFT_collect(search_name):
    sdk = ThirdwebSDK(NETWORK)
    contract = sdk.get_nft_collection(THIRDWEB)
    nft_lst = contract.get_all()
    ipfs_lst=[]

    for nft_obj in nft_lst:
        if nft_obj.metadata.name == search_name:
            ipfs_lst.append(nft_obj.metadata.image)
    return ipfs_lst


def upload_json(JsonFile):
    f = open(JsonFile)
    json_data = json.load(f)

    files = {
        'file': str(json_data),
    }
    response = requests.post('https://ipfs.infura.io:5001/api/v0/add', files=files, auth=(projectID,secretKey))
    if response.status_code == 200:
        print ('Upload IPFS successful')
        return response.json()["Hash"]
    else:
        return False

# for filename in os.listdir('/Users/luju/Library/Containers/com.tencent.xinWeChat/Data/Library/Application Support/com.tencent.xinWeChat/2.0b4.0.9/a8789faea974cdc3500680286da8c5c7/Message/MessageTemp/978823ce65c0e1871a028b536c878e23/File/reviews_folder'):
#     jsonFile = os.path.join('/Users/luju/Library/Containers/com.tencent.xinWeChat/Data/Library/Application Support/com.tencent.xinWeChat/2.0b4.0.9/a8789faea974cdc3500680286da8c5c7/Message/MessageTemp/978823ce65c0e1871a028b536c878e23/File/reviews_folder', filename)
#     ipfs = upload_json(jsonFile)
#     print (ipfs)
#     NFT_mint(jsonFile, ipfs)
#     print('success')

# # nft_lst = contract.get_all()
# # print(nft_lst)

# ipfs_lst = NFT_collect("Facebook")
# for ele in ipfs_lst:
#     print(ele)