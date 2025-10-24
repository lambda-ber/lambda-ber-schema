#!/usr/bin/env python3
"""Download SAXS data from SimpleScattering"""

import requests
import os

# Create data directory
os.makedirs("data/simplescattering", exist_ok=True)

# Dataset URLs with proper base URL
base_url = "https://simplescattering.com"
urls = {
    "A_S_GluRS_1_5.dat": f"{base_url}/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBaDBSIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--183433be86d7de6e664c74c9e3a3e19811fdee08/A_S_GluRS_1_5.dat",
    "GluRS_Results.zip": f"{base_url}/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBaThIIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--22f8ac3518d7c73bcd0e862fed599a7ceb4384bc/GluRS_Results.zip",
    "8vc5.pdb": f"{base_url}/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBaDRSIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--859126383c33e946f0ca03b5e534985b0ad7db99/8vc5.pdb"
}

# Download each file
for filename, url in urls.items():
    filepath = f"data/simplescattering/{filename}"
    print(f"Downloading {filename}...")
    
    response = requests.get(url, allow_redirects=True)
    
    if response.status_code == 200:
        with open(filepath, 'wb') as f:
            f.write(response.content)
        print(f"  Downloaded {len(response.content):,} bytes")
    else:
        print(f"  Failed with status {response.status_code}")

print("\nFiles downloaded:")
for f in os.listdir("data/simplescattering"):
    size = os.path.getsize(f"data/simplescattering/{f}")
    print(f"  {f}: {size:,} bytes")