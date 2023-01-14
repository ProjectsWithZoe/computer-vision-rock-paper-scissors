
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

    rounds=5
    computer_wins=0
    user_wins=0
    choices =['Rock', 'Paper', 'Scissors']

    countdown_duration = 10  # in seconds

    start_time = time.time()

    while computer_wins<3 and user_wins<3: 
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
        computer_choice = random.choice(choices)
        print(f'Computer chose {computer_choice}')

        if (computer_choice == user_choice):
            rounds-=1
            user_wins+=1
            computer_wins+=1
        elif (computer_choice =='Rock' and user_choice=='Scissors') or (computer_choice=='Paper' and user_choice=='Rock') or (computer_choice=='Scissors' and user_choice=='Paper'):
            rounds-=1
            computer_wins+=1
        else:
            rounds-=1
            user_wins+=1
        print(f'Computer : {computer_wins}, User: {user_wins}')
        cv2.imshow('frame', frame)
        # Press q to close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    if user_wins == 3:
        print("You won!")
    else:
        print("You lost!")

        

    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

get_prediction()


   


# %%