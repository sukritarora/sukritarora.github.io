# CS194-26 (CS294-26): Project 1 starter Python code

# these are just some suggested libraries
# instead of scikit-image you could use matplotlib and opencv to read, write, and display images

import numpy as np
import skimage as sk
import skimage.io as skio
import skimage.transform as sktr
import matplotlib.pyplot as plt
import glob
import time

# align the images
# functions that might be useful for aligning the images include:
# np.roll, np.sum, sk.transform.rescale (for multiscale)

def ssd(a, b):
    return np.sum(np.square(np.subtract(a.ravel(), b.ravel())))

def crop(im, perc):
    h,w = im.shape
    c1,c2 = tuple([dim//2 for dim in im.shape])
    # h_bounds = slice(int(np.round(c1-(h*perc//2))),int(np.round(c1+int(h*perc//2))))
    # w_bounds = slice(int(np.round(c2-int(w*perc//2))),int(np.round(c2+int(w*perc//2))))
    h_bounds = slice(int((1-perc)*h),-int((1-perc)*h))
    w_bounds = slice(int((1-perc)*w),-int((1-perc)*w))
    return im[h_bounds,w_bounds]

def calc_offset(im, ref, scale=None):
    window = np.arange(-15,15) if scale is None else np.arange(int(-2/scale),int(2/scale))
    scores = np.zeros((window.shape[0], window.shape[0]))
    # print(window[0])
    for x in window:
        for y in window:
            scores[x-window[0],y-window[0]] = ssd(np.roll(im, (x,y), (0,1)), ref)
    # print(scores)
    # print(np.min(scores), np.unravel_index(np.argmin(scores), scores.shape))
    idxs = np.unravel_index(np.argmin(scores), scores.shape)
    return tuple([window[idx] for idx in idxs])

def align(im, ref):
    cropped_im = crop(im, 0.9)
    cropped_ref = crop(ref, 0.9)
    offsets = calc_offset(cropped_im,cropped_ref)
    return (np.roll(im, offsets, (0,1)), offsets)

def multiscale_align(im, ref, s=1/16, offset=(0,0)):
    # print(s)
    if s >= 1:
        return (np.roll(im, offset, (0,1)), offset)
    cropped_im = crop(im, 0.9)
    cropped_ref = crop(ref, 0.9)
    scaled_off = tuple([off*2 for off in offset])
    curr_offset = calc_offset(np.roll(sktr.rescale(cropped_im, s), scaled_off, (0,1)), sktr.rescale(cropped_ref, s),s)
    return multiscale_align(im, ref, s*2, tuple([scale_old_off+new_off for scale_old_off,new_off in zip(scaled_off,curr_offset)]))

data_files = glob.glob("data/*")
for file in data_files:
    # read in the image
    print("Working on {}".format(file))
    im = skio.imread(file)

    # convert to double (might want to do this later on to save memory)    
    im = sk.img_as_float(im)
        
    # compute the height of each part (just 1/3 of total)
    height = np.floor(im.shape[0] / 3.0).astype(np.int)

    # separate color channels
    b = im[:height]
    g = im[height: 2*height]
    r = im[2*height: 3*height]

    t0 = time.time()
    if file[-3:] == "jpg":
        ag, g_offset = align(g, b)
        ar, r_offset = align(r, b)
    else:
        ag, g_offset = multiscale_align(g, b, s=1/np.log(max(*g.shape)))
        ar, r_offset = multiscale_align(r, b, s=1/np.log(max(*r.shape)))

    im_out = np.dstack([ar, ag, b])
    time_elapsed = time.time()-t0
    print("Time Elapsed: {} for {}".format(time_elapsed, file))
    print("Green Offset: {} for {}".format(g_offset, file))
    print("Red Offset: {} for {}".format(r_offset, file))
    # save the image
    fname = "out/"+file[5:-3]+"jpg"
    # print(fname)
    skio.imsave(fname, im_out)
