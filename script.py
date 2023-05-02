import requests
import os 

import csv
with open('WP_images - Sheet1.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        os.mkdir(row['Title'])
        print(row['Title'])
        for img in row['Image URL'].splitlines():
            print(img)
            file_name = img.split('/')[-1]
            print("Downloading file: %s"%file_name)
            r = requests.get(img, stream=True)
            with open(row['Title']+ '/' +file_name, 'wb') as f:
                for chunk in r:
                    f.write(chunk)
