Speaker Verification
=======

This web app records and tests audio input against a pre-recorded voice password to verify speaker identity.

###Feature Analysis
#####(analysis_2.py)
Audio features are extracted using signal processing and Mel Frequency Cepstral Coefficient analysis. First, the original password is analyzed, and the extracted features create a unique voiceprint. Then the test audio recorded in the browser is analyzed and features extracted.

###Dynamic Time Warping
#####(dynamic.py)
After the features for the voiceprint and the test audio are extracted, they are compared to each other using Dynamic Time Warping. The output of this step is a number that represents how similar the two sets of features are. The closer the number is to zero, the more similar the features. After multiple tests, a base number is selected which determines whether or not a test audio is a match.

###Web App
#####(app.py, recorder.js, recorder.html)
Currently, the user is able to record his or her voice in the browser. The test audio is then saved temporarily and tested against my password. This portion utilizes Python, Flask, HTML5, Bootstrap, JavaScript, AJAX, and the navigator.getUserMedia() API.

![Alt text](screenshots/waveforms.jpg "Audio Wavs")