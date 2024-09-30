
# Arrow Detection with OpenCV

This project is a Python-based implementation using OpenCV to detect arrows in a live video feed from a webcam. The code allows for real-time contour detection and tracks the orientation of arrow-like shapes.


## Features

- **Real-time video processing:** The webcam feed is processed live for arrow detection.
- **Contour detection:** Arrows are detected based on their contour shapes.
- **Angle calculation:** The angle of the detected arrow is calculated and displayed on the screen.


## How it Works

- The webcam captures the video feed.
- The frame is converted to HSV color space.
- Lower and upper bounds for HSV are set using trackbars.
- A binary mask is created to filter out colors that do not fall within the HSV range.
- Contours are detected from the mask.
- If a contour resembles an arrow, the angle of the arrow is calculated and displayed.


## Authors

- GitHub: [@Akshath Dubey](https://www.github.com/akshathdubey)
- Instagram: [@akshath_dubey](https://www.instagram.com/akshath_dubey)

## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License.

