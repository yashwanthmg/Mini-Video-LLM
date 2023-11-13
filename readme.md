# Mini Video LLM (Language and Object Detection Model) Project

## Overview

This mini project combines speech recognition, object recognition, and text summarization to generate a summary of a given video clip. It uses Google Speech API for speech recognition, YOLOv4 for object recognition, and Sumy for text summarization.

## Tools and Libraries Used

- **Google Speech API:** Utilized for speech recognition in video clips.
- **Numpy:** Used to compute and manipulate array items.
- **MoviePy:** Used for video editing and processing.
- **YOLOv4:** Implemented for object recognition in video frames.
- **Sumy:** Employed for text summarization.

## Project Structure

- **`src/`**: Contains the source code files.
  - `transcribe_audio.py`: Handles speech recognition using Google Speech API and MoviePy.
  - `object_recognition.py`: Implements video analysis using YOLOv4 for object recognition.
  - `video_summarization.py`: Creates a summary of the video using the output from speech recognition and object recognition.
  
- **`videos/`**: Directory to store input and output video clips.

- **`yoloV4/`**: contains model, weight and config files

## How to Use

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/mini-video-llm.git
   ```
   
2. Install dependencies:

	```bash
	pip install -r requirements.txt
	```
	
3. Prepare your video clip:

	Place the video clip you want to summarize in the videos/ directory.

4. Run the scripts:

	Speech Recognition and Object Recognition:

	```bash
	python src/transcribe_audio.py 
	python src/object_recognition.py
	```
	
	Video Summarization:

	```bash
	python src/video_summarization.py -s speech_recognition_output.txt -o object_recognition_output.txt
	```
	Find the summarized text in the output_summary.txt file.

## Future Updates
	1) Integration with more advanced object recognition models.
	2) Support for additional languages in speech recognition.
	3) Improved video summarization techniques.
	4) Feel free to contribute or suggest improvements by creating issues or pull requests.






