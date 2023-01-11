# Computer Vision RPS

Using https://teachablemachine.withgoogle.com/train/image I took an image using the webcam making a rock, paper and scissors motion with my right hand . Inorder to train the model, many images were needed so i tried to take an image at every angle of the 3 motions.

Collectively there were over 300 images per motion and a final 'nothing' model was trained showing no motion.
These were then trained for several seconds and were available to be exported through Tensorflow producing the keras_model.h5 file and the label.txt.

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
