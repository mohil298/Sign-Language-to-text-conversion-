Sign Language to Text Conversion
Abstract
This project presents a real-time method using neural networks for fingerspelling-based American Sign Language (ASL) recognition. The system filters hand images and classifies hand gestures, achieving 98.00% accuracy for the 26 letters of the alphabet.

Project Description
ASL is vital for communication among Deaf and Mute (D&M) individuals. This project focuses on recognizing fingerspelling hand gestures to form words. Sign language consists of three major components: handshapes, movements, and facial expressions.

Steps of Building the Project
1. Directory Structure Creation
Create directories for storing training and testing data.

2. Data Collection
Capture frames using a webcam, define a Region of Interest (ROI), and apply a Gaussian blur filter for preprocessing the images.

3. Model Creation
Use a Convolutional Neural Network (CNN) to train the model.

CNN Architecture:
Convolutional Layer: Learnable filters for feature detection.
Pooling Layer: Reduces the size of activation matrices.
Fully Connected Layer: Neurons connected to all inputs.
4. GUI Creation
Develop a Graphical User Interface (GUI) for converting signs to text, allowing users to communicate effectively with D&M individuals.

5. Results
Achieved 95.8% accuracy with the first algorithm layer and 98.0% with a combination of layers.

Libraries Requirements
Ensure Python 3.8 or above is installed.
Latest pip
numpy
os-sys
opencv-python
tensorflow
keras
tk
Pillow
pyenchant
cyhunspell

Running the Project
Run the application using Python to start the GUI for sign language to text conversion.
bash
python /path/to/the/Application.py
