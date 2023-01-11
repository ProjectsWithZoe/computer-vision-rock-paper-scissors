# Computer Vision RPS

Using https://teachablemachine.withgoogle.com/train/image I took an image using the webcam making a rock, paper and scissors motion with my right hand . Inorder to train the model, many images were needed so i tried to take an image at every angle of the 3 motions.
Collectively there were over 300 images per motion and a final 'nothing' model was trained showing no motion.
These were then trained for several seconds and were available to be exported through Tensorflow producing the keras_model.h5 file and the label.txt.
