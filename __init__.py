import canvas

#Here is how your PixelArt is stored (using a "list of lists")
palette=["#FFFFFF","#0000FF","#FF0000"]
pixels = [[0,0,0,0,0,1,1,1,1,1,1,0,0,0,0]]

pixels.append([0,0,0,1,1,1,1,1,1,1,1,1,0,0])
pixels.append([0,0,1,1,0,0,1,1,1,1,0,0,1,0])
pixels.append([0,1,1,0,0,0,0,1,1,0,0,0,0,0])
pixels.append([0,1,1,0,0,2,2,1,1,0,0,2,2,0])
pixels.append([1,1,1,0,0,2,2,1,1,0,0,2,2,1])
pixels.append([1,1,1,1,0,0,1,1,1,1,0,0,1,1])
pixels.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1])
pixels.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1])
pixels.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1])
pixels.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1])
pixels.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1])
pixels.append([1,1,0,1,1,1,0,0,1,1,1,0,1,1])
pixels.append([1,0,0,0,1,1,0,0,1,1,0,0,0,1])

canvas.draw(pixels, palette)
