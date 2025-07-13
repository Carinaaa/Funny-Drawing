# Titanic-Like-Drawing

Probably you know the scene from the Titanic movie, where Rose requests a drawing.

Today, you can feel like Rose, just add your picture and wait for it to be done.

## How to use this code

1. Add your picture in the project and then, add the name on line 11:

```sh
img = cv.imread("_NKL5841.jpg")
```

2. Set the details from the thresholds 1 and 2 and close the window.

<img src="https://github.com/Carinaaa/Funny-Drawing/blob/main/readme_resources/thresholds.PNG" width="400">

4. Wait for the picture to be rendered and enjoy without sinking!

<img src="https://github.com/Carinaaa/Funny-Drawing/blob/main/readme_resources/results.PNG" width="400">

6. Did you wait too long? You can set less edges from thresholds or less drawing from 10 to 20 or so:

```sh
if i % 10 == 0:
```

## Code walk-through:

