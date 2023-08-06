# Lazy_Video_Reader

## Installation
    pip install Lazy_Video_Reader

use sudo if you want to install it for root

## Objectif

The objectif of this package is to allow operation on frames where the size of the video do not permit to be hold on RAM

## Usage

the package is compose of 5 methods create_video_reader, take, drop, head, tail every function return iterator or generator
```py
    video = create_video_reader("path to your video") #return a generator usable by all function of itertools, toolz...
    take(10, video) #return the first 10 frames as an iterator
    drop(10, video) #return the last 10 frames as an iterator
    head(video) #return the first frames as an iterator
    tail(video) #return all the frames but the first one as an iterator
    for v in video:
        print(v) #loop through all frames
```
