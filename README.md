# tensorflow-srgan
Super Resolution GANs in Tensorflow 1.1+

# Training the model

Training with default settings: `python3 srez_main.py --run train`. The script will periodically output an example batch in PNG format onto the `srez/train` folder, and checkpoint data will be stored in the `srez/checkpoint` folder.

After the network has trained you can also produce an animation showing the evolution of the output by running `python3 srez_main.py --run demo`

For dataset you can use this small set of faces data http://vis-www.cs.umass.edu/lfw/lfw-a.zip  (found it here http://vis-www.cs.umass.edu/lfw/)