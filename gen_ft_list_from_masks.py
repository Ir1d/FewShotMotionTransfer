import fire
import cv2
import os
import tqdm, glob
import numpy as np

def process(root):
    with open(os.path.join(root, 'finetune_samples.txt'), 'w') as f:
        li = glob.glob(os.path.join(root, 'segmentation', '*.png'))
        # ww = []
        for cur in tqdm.tqdm(li):
            im = cv2.imread(cur)
            num = (im == 255).sum()
            # ww.append(num)
            if num > 1e4:
                f.write(os.path.basename(cur).replace('.png', '') + '\n')
            # print(num)
        # print(sorted(ww)[:10])
if __name__ == '__main__':
    fire.Fire(process)
