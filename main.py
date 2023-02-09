import requests

requests.packages.urllib3.disable_warnings()


def sysinfo():
    url = "https://api-uat.ggn.nl/talendapi/dossierstatus?dossiers=00020017000,00015656000,B3990033000"
    cert_file_path = "cert/GGN+developer+SSL+client+key.crt"
    key_file_path = "cert/GGN+developer+SSL+client+key.key"

    headers = {"X-Api-Key": "Cvh4gANVtyHa1sKaN351v98ov4MEyaaqhWpTvDZq"}
    # params = {"param_1": "value_1", "param_2": "value_2"}
    cert = (cert_file_path, key_file_path)
    response = requests.get(url, verify=False, headers=headers, cert=cert)

    # print request object
    print(response.content)


print(sysinfo())
