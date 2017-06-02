#!/usr/bin/python3

from PIL import Image
import numpy as np
import pandas as pd

def get_image(image_path):
    """Get a numpy array of an image so that one can access values[x][y]."""
    image = Image.open(image_path, 'r')
    width, height = image.size
    pixel_values = list(image.getdata())
    if image.mode == 'RGB':
        channels = 3
    elif image.mode == 'L':
        channels = 1
    else:
        print("Unknown mode: %s" % image.mode)
        return None
    pixel_values = np.array(pixel_values).reshape((width, height, channels))
    ## Dataframe
    pan = pd.Panel(pixel_values)
    df = pan.swapaxes(0, 2).to_frame()
    df.index = df.index.droplevel('minor')
    df.index.name = 'ID'
    df.index = df.index+1
    df.columns = list('RGB')
    df.to_csv(image_path.split('.')[0] +'.tsv', sep='\t', encoding='utf-8')
    print(df)
    # return pixel_values
    return df

get_image('b.jpg')
