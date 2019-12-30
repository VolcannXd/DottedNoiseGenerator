# Dotted Noise & the algorithm/soft to generate it
## python 3.7

---

## ReadMe Summary
• What is a dotted noise ?\
• How to use the generator\
• About

---

## What is a dotted noise ?
A dotted noise generator is simply a way of generating noise wich I come up with. A dotted noise algorithm simply place points at random positions and calculate for each pixels the distance between these and the pixel. Then, the pixel's brightness is calculated from the distance.

---

## How to use the generator
Simply specify parameters in the GUI and click 'generate'. Then, save your favorites parameters by clicking File > Save. You can also save the image by clicking Image > Save.

---

## Parameters description
### The *size* parameter
> type : Integer

`128 < size < 1024`

This parameter simply define the image size (wich is always a square): 512 is recomanded.

### The *scale* parameter
> type : Integer

`1 < scale < 100`

The scale parameter is simply defining how many random points can spawn in your noise image

### The *threshold* parameter
> type : Integer

`1 < threshold < 500`

This is more technical. The threshold indicate to the algorithm how far from a point the pixel is brightned.

### The *contrast* parameter
> type : Double 

`0 <= contrast <= 1`

This parameter is in charge of the contrast. Except that it can invert value when reaching 0.5 or above.

### The *seamless* parameter
> type : Boolean

This parameter (if set to true) prevent obvious cut in the image if it is repeated: to be used as textures.

---

## About
This Algorithm and software were both developped by Arthur Detaille. You can contact me on [twitter](https://twitter.com/arthur_detaille) or by [e-mail](mailto:arthurdetaille.pro@gmail.com).<br/>
I want to thank George Hotz a.k.a. GeoHot wich is my everyday's source of inspiration; probably, with Markus Personn, the programmer I respect the most. Go check his work [here](https://www.youtube.com/channel/UCwgKmJM4ZJQRJ-U5NjvR2dg)