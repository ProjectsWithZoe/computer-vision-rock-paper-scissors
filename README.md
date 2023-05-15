# Computer Vision RPS


## Creating the model using TeachableMachine and Tensorflow
Using https://teachablemachine.withgoogle.com/train/image I took an image using the webcam making a rock, paper and scissors motion with my right hand . Inorder to train the model, many images were needed so i tried to take an image at every angle of the 3 motions.

Collectively there were over 300 images per motion and a final 'nothing' model was trained showing no motion.
These were then trained for several seconds and were available to be exported through Tensorflow producing the keras_model.h5 file and the label.txt.

## Game logic without using the camera

To set up the game i created another file and imported the random module. I then created a list of choices containing 'Rock','Paper' and 'Scissors' to put into the get_computer_choice function. 
```python
choices =['Rock', 'Paper', 'Scissors']
```
The computer then randomly chose one of these and saved it as a variable computer_choice.

Secondly I created the get_user_choice function which simply asks the user what they want to choose between the 3 and saves it as a variable user_choice.

Lastly, I created an if-elif-else loop under the get_winner function which takes in both the computer_choice and user_choice as parameters.
The loop dictates that if the user choice and computer_choice are the same then it prints out 'It's a tie'. 
If the computer chooses rock and user chooses scissors OR computer chooses paper and user chooses rock OR computer chooses scissors and user chooses paper then the computer wins and prints out'You lost!"
However if none of this are met then the user wins and it prints out'You win!'

Finally these 3 functions get_computer_choice, get_user_choice and get_winner were combined into a single function called play which calls them and prints out who the winner is, thus reducing our code from multiple lines to a single function call.

```python 
def play():
    get_computer_choice()
    get_user_choice()
    get_winner() 
    
```

This code will run in sequence by first getting the computers choice, then the users choice, then checking who between the two is a winner and finally printing out 'You won', 'You lost' or 'It is a tie'

## Final code <img width="1040" alt="Screenshot 2023-01-11 at 19 09 54" src="https://user-images.githubusercontent.com/118231395/211896583-7dbca879-093c-4aa2-8183-4f77b5fadd1d.png">

## Game logic with the camera
The required modules and libraries are imported, including random, time, cv2 from OpenCV, load_model from Keras, and numpy.
The pre-trained model is loaded using load_model('keras_model.h5'). 

The code initializes variables such as rounds_played, computer_wins, and user_wins to keep track of the game progress and scores. The choices list contains the options for the Rock-Paper-Scissors game.
The variable countdown_duration is set to 10 seconds, representing the maximum time allowed for the user to make a gesture.
The game loop starts and continues until one of the following conditions is met: rounds_played reaches 5, computer_wins reaches 3, or user_wins reaches 3.
Inside the loop, the code captures a frame from the webcam using cap.read(). The frame is then resized to (224, 224) using OpenCV's cv2.resize() function.
The resized frame is converted to a numpy array and normalized by scaling the pixel values to the range of -1 to 1.
The normalized image data is stored in the data array, which has the shape (1, 224, 224, 3), representing a batch of one image.
The model predicts the gesture in the image by calling model.predict(data). The prediction result is an array, and the index with the highest value is extracted using np.argmax().
The user's choice is determined based on the highest index using the classes list.
The code calculates the remaining time for the user to make a gesture by subtracting the elapsed time from the start time.
If the remaining time is less than or equal to 0, the user's choice is displayed, and the loop is terminated.
The computer makes a random choice from the choices list.
The user's choice and the computer's choice are compared to determine the winner of the round. The results are printed accordingly, and the scores are updated.
The current score is displayed, and the frame is shown using cv2.imshow().

If the 'q' key is pressed, the loop is terminated.
After the loop, the final game result is determined based on the scores, and a corresponding message is printed.

The get_prediction() function combines image processing, prediction using a pre-trained model, game logic, and webcam input to enable playing Rock-Paper-Scissors against the computer in real-time.
