# import libraries
import requests
import zipfile
import glob
import io

# MN state administered land
sl_url = 'https://resources.gisdata.mn.gov/pub/gdrs/data/pub/us_mn_state_dnr/bdry_dnr_managed_areas/shp_bdry_dnr_managed_areas.zip'
          
# MN forest inventory
forest_url = "https://resources.gisdata.mn.gov/pub/gdrs/data/pub/us_mn_state_dnr/biota_dnr_forest_inv_species/shp_biota_dnr_forest_inv_species.zip"

# MN land cover classification
mnlcc_url = "https://resources.gisdata.mn.gov/pub/gdrs/data/pub/us_mn_state_dnr/biota_landcover_mlccs/shp_biota_landcover_mlccs.zip"

print('Downloading shapefiles...')

local_path = './raw'
url_list = [sl_url, forest_url, mnlcc_url]

for index, url in enumerate(url_list):
    print(f"Downloading shapefile {index + 1}")
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(path=local_path) # extract to folder

print("Done")

filenames = glob.glob("./raw/*forest_inventory_species.shp")
filenames.extend(glob.glob("./raw/*management_units.shp"))
filenames.extend(glob.glob("./raw/*landcover*.shp"))
print(f"The files of interest are {filenames}.")