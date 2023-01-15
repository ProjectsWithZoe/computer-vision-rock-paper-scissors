
def get_prediction():
    import random
    import time
    import cv2
    from keras.models import load_model
    import numpy as np
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    classes = ['Rock', 'Paper', 'Scissors', 'Nothing']

    rounds_played=0
    computer_wins=0
    user_wins=0
    choices =['Rock', 'Paper', 'Scissors']

    countdown_duration = 10  # in seconds

    start_time = time.time()

    while rounds_played < 5 and computer_wins < 3 and user_wins < 3:
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        highest = np.argmax(prediction[0])
        user_choice = classes[highest]
        current_time = time.time()
        elapsed_time = current_time - start_time
        remaining_time = countdown_duration - elapsed_time
        if remaining_time <= 0:
            print(f"You chose {user_choice}")
            break

        # Computer makes a random choice
        computer_choice = random.choice(choices)
        print(f"Computer chose {computer_choice}")

        # Compare user's choice and computer's choice to determine round winner
        if user_choice == "Rock":
            if computer_choice == "Scissors":
                print("You win!")
                user_wins += 1
            elif computer_choice == "Paper":
                print("Computer wins!")
                computer_wins += 1
            else:
                print("It's a tie!")
        elif user_choice == "Paper":
            if computer_choice == "Rock":
                print("You win!")
                user_wins += 1
            elif computer_choice == "Scissors":
                print("Computer wins!")
                computer_wins += 1
            else:
                print("It's a tie!")
        elif user_choice == "Scissors":
            if computer_choice == "Paper":
                print("You win!")
                user_wins += 1
            elif computer_choice == "Rock":
                print("Computer wins!")
                computer_wins += 1
            else:
                print("It's a tie!")
        rounds_played += 1
        print(f"Score: You {user_wins}, Computer {computer_wins}")
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    if user_wins == 3:
        print("Congratulations, you won the game!")
    elif computer_wins == 3:
        print("Sorry, the computer won the game.")
    else:
        print("The game was a tie.")

get_prediction()