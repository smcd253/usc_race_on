import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# main fn
def main():
    #reasd image
    img = Image.open("../black_bar.jpg")
    img.convert('RGB')
    img.show()

    # get height and width
    width, height = img.size
    
    # black region
    plot_mat = [[0 for x in range(width)] for y in range(height)]
    for x in range(width):
        for y in range(height):
            r,g,b = img.getpixel((x,y))
            bw = r * 299/1000 + g * 587/1000 + b * 114/1000
            if bw < 100:
                plot_mat[y][x] = 1
            else:
                plot_mat[y][x] = 0
    # plot
    final_plot = np.array(plot_mat)

    # set axes
    plt.imshow(final_plot)
    plt.show()
  
# run main
if __name__== "__main__":
  main()
