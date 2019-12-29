# DottedNoiseGenerator

## What is a dotted noise ?
A dotted noise generator is simply a way of generating noise wich I come up with. A dotted noise algorithm simply place points at random positions and calculate for each pixels the distance between these and the pixel. Then, the pixel's brightness is calculated from the distance.

## How to use the generator
Simply specify parameters in the GUI and click 'generate'. Then, save your favorites parameters by clicking File > Save. You can also save the image by clicking Image > Save.

### The 'size' parameter
type : Integer
This parameter simply define the image size (wich is always a square): 512 is recomanded.

### The 'scale' parameter
type : Integer
The scale parameter is simply defining how many random points can spawn in your noise image

### The 'threshold' parameter
type : Integer
This is more technical. The threshold indicate to the algorithm how far from a point the pixel is brightned.

### The 'invert' parameter
type : Boolean
If this parameter is true the brightness from the point is maximum.. Otherwise the brightness is minimal and pixels are brightning up with distance.

### The 'seamless' parameter
type : Boolean
This parameter (if set to true) prevent obvious cut in the image it is repeated: to be used as textures.