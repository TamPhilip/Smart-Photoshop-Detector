# AI4Good-2018
Hackathon project for the AI4SocialGood Hackathon 2018.

## Inspiration
Fake news. Fake information. Fake images.<br />
In this day and age where every picture is edited, CGIed, and using the snapchat dog filter :dog:, it becomes hard to determine whether a picture is real or not. Though it is sometimes entertaining (everyone loves Trump photoshops), it isn't always for the best.
Younger folks can be easily influenced by some of the images seen online, and think that their own bodies do not conform to the 'norm' :sweat:. This leads to a decrease of self-confidence, which hinders personal growth. We decided to create something that would bring awareness to the reality that one sees on the web.

## What it does
Analyzing images from the web, our AI attempts to recognize photoshopped images.

## How we built it
***Step 1: Data Analysis*** Using the [Casia](http://forensics.idealtest.org/casiav2/) dataset, we were able to have reliable images that were both photoshopped and original. We first resized the images to 256x256 pixels in order to have a consistent image size for our model, then labelled each image as 'fake' :thumbsdown: or 'real' :thumbsup:.

***Step 2: Training The Model*** We used machine learning to detect patterns in the images and extrapolate to new images. The code can be found [here](https://drive.google.com/file/d/1IZt6MbhnAaZlx4ufcjFvcsSYnUDagWvG/view?usp=sharing). Ideally, we would like to combine ELA (error level analysis) with a high-pass filter to capture the minor changes in pixels, and analyze the pre-processed pictures with a convolutional neural network.<br /> 
Our model is based on the following papers:<br /> CNN - [Image Manipulation Detection using Convolutional Neural Network](https://pdfs.semanticscholar.org/8d29/16d15ffc5b0f97a542e01780f785421185b8.pdf) by Kim D. and Lee H.
<br /> ELA - [Fake Image Detection Using Machine Learning](https://ijcsits.org/papers/vol7no22017/4vol7no2.pdf) by Villan A.M., Kuruvilla K., Paul J. and Elias E.P.

***Step 3: Chrome Extension*** How to make this accessible? The simplest way to apply this AI to our everyday life is to have an automatic detector in the browser. Our team decided to create this extension to allow ease of use. Now even a 9 year old can use it! :girl: :boy:.<br />
It simply shows a red border around images that our AI labelled as photoshopped.

## What we learned
Analyzing images is hard! Within the alloted time, we were only able to train a simple model, but in the future, we hope to use a convolutional neural network, which would be better for image recognition.
