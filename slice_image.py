import image_slicer
import os 
# image_slicer.slice('CarPlateFull/31.jpg', 50)

# to crop all image in the directory into smaller images
subdirs = [x[0] for x in os.walk("CarPlateFull")]                                                                            
for subdir in subdirs:                                                                                            
        files = os.walk(subdir).next()[2]                                                                             
        if (len(files) > 0):                                                                                          
            for file in files:
                print file
                tiles = image_slicer.slice("CarPlateFull/"+file, 50, save=False)
                image_slicer.save_tiles(tiles, directory='CarPlateFull/Tiled', prefix=file)