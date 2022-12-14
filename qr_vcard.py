import pyqrcode
import pandas as pd
import os

import scratch_qr_config

def createStaffQRCodes(csv_in, csv_out, save_to):
    df = pd.read_csv(csv_in)
    df["@QR_Code"] = "C:\\Users\\<user>\\Downloads\\QRcodes\\" + df["Name"].str.replace(" ","_") + ".png"
    for index, values in df.iterrows():
        lastname = values["Name"].split(" ")[1].strip()
        firstname = values["Name"].split(" ")[0].strip()
        title = values["Title"]
        phone = values["Phone"]
        email = values["Email"]
        website = scratch_qr_config.website_url
        org = scratch_qr_config.org
        cell = values["Cell"]
        # street = values["street"]
        # city = values["city"]
        # p_code = values["p_code"]
        # country = values["country"]

        data = f'''BEGIN:VCARD\nVERSION:3.0\nN:{lastname};{firstname}\nFN:{firstname} {lastname}\nORG:{org}\nTITLE:{title}\nTEL;WORK;VOICE:{phone}\nTEL;CELL:{cell}\nEMAIL;WORK;INTERNET:{email}\nURL:{website}\nEND:VCARD'''

        image = pyqrcode.create(data)
        image.svg(os.path.join(save_to, f"{str(values['Email']).split('@')[0]}.svg"), scale=10)
        image.png(os.path.join(save_to, f"{str(values['Email']).split('@')[0]}.png"), scale=10)
    
    df.to_csv(csv_out, index=False)

def createFrontDeskQRCodes(csv_in, csv_out, save_to):
    df = pd.read_csv(csv_in)
    for index, values in df.iterrows():
        lastname = values["Title"]
        title = values["Name"]
        phone = values["Phone"]
        email = values["Email"]
        website = values["Url"]
        org = scratch_qr_config.org

        data = f'''BEGIN:VCARD\nVERSION:3.0\nFN:{lastname}\nORG:{org}\nTITLE:{title}\nTEL;WORK;VOICE:{phone}\nEMAIL;WORK;INTERNET:{email}\nURL:{website}\nEND:VCARD'''

        image = pyqrcode.create(data)
        # image.svg(f"vcard_qrs/{lastname}_{firstname}.svg", scale="5")
        image.png(os.path.join(save_to, f"{str(values['Email']).split('@')[0]}.png"), scale=10)
    
    df["@QR_Code"] = "C:\\Users\\<user>\\Downloads\\QRcodes\\" + f"{str(values['Email']).split('@')[0]}" + ".png"
    df.to_csv(csv_out, index=False)

createStaffQRCodes(csv_in=scratch_qr_config.staff_in, csv_out=scratch_qr_config.staff_out, save_to=scratch_qr_config.staff_save_dir)
createFrontDeskQRCodes(csv_in=scratch_qr_config.loc_in, csv_out=scratch_qr_config.loc_out, save_to=scratch_qr_config.loc_save_dir)

'''
BEGIN:VCARD
VERSION:3.0
N:Lastname;Surname
FN: Displayname
ORG:Example Inc
URL:http://www.example.com/
EMAIL:info@example.com
TEL;TYPE=voice,work,pref:+18008008000
ADR;TYPE=intl,work,postal,parcel:;;1234 Main St;Anytown;;75024;USA
END:VCARD
'''
