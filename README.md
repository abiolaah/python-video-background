# Background Replacement with MediaPipe

This project demonstrates background replacement in a video using OpenCV and MediaPipe's Selfie Segmentation. It takes a video file, segments the person from the background, and replaces the background with a custom image

## Features

- Uses MediaPipe's Selfie Segmentation to detect and segment the person in each video frame.
- Replaces the original video background with a static image.
- Displays the processed video in real-time.

## Requirements

- Python 3.7+
- OpenCV (cv2)
- MediaPipe

## Installation

1. Clone the repository:

```bash
git clone git@github.com:abiolaah/python-video-background.git
```

2. Create and activate a virtual environment(optional but recommended):

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Linux/Mac
source venv/bin/activate
```

3. Install the required packages:

```bash
pip install opencv-python mediapipe
# Or
pip install -r requirements.txt
```

## Usage

1. Place your input video as _test.mov_ and your background image as _test_bg.jpeg_ in the project directory.
2. Run the application:

```bash
python app.py
```

3. The output window will display the video with the replaced background. Press `q` to quit

## File Structure

- [app.py](app.py) — Main application script.
- [test.mov](test.mov) — Input video file (not included in version control).
- [test_bg.jpeg](test_bg.jpeg) — Background image file (not included in version control).
- [venv/]() — Virtual environment directory (not included in version control).
- [.gitignore](.gitignore) — Specifies files and directories to be ignored by git.

### Notes

- Make sure your input video and background image are named [test.mov]() and [test_bg.jpeg]() respectively, or modify app.py to use different filenames.
  The segmentation model used is MediaPipe's Selfie Segmentation with [model_selection=1](app.py) for better quality.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
