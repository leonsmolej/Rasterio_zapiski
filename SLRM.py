import rasterio as rio
import numpy as np
import os
from scipy.ndimage import gaussian_filter
from rasterio.plot import show, show_hist


#Dodaj input path do folderja da se vsi tifi štejejo, in isto za output.
#dodaj še vmin, vmax ter radius(sigma) kot input 

dem_path = os.path.normpath(r"/home/leon/Dokumenti/KODA/Python/Rasterio/Pivola.tif")

with rio.open(dem_path) as src:
    dem=src.read(1)
    print(src.height)
    print(src.width)
    vel_celice=src.res[0]
    print(vel_celice)
    meta=src.meta.copy()


izravnan_dem=gaussian_filter(dem,30)


slrm=dem-izravnan_dem

slrm=np.clip(slrm,-1.5, 1.5)

print(slrm.shape[1])
#print(slrm)
show(slrm, cmap="gray")

# with rio.open(r"/home/leon/Dokumenti/KODA/Python/Rasterio/test_outputa/moj_slrm.tif",
#               "w", **meta) as dst:
#     dst.write(slrm, 1)