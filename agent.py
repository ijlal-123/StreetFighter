import retro
import cv2

# Initialize the environment
env = retro.make(game='StreetFighterIISpecialChampionEdition-Genesis')
state = env.reset()

for _ in range(5000):
    # Take random action
    action = env.action_space.sample()
    state, reward, done, info = env.step(action)

    # Resize the frame (state)
    resized_state = cv2.resize(state, (800, 600))  # Width x Height in pixels

    # Display the resized frame in an OpenCV window
    cv2.imshow("Street Fighter - Resized", resized_state)

    # Wait for a key press for 1ms
    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' key to exit
        break

    if done:
        state = env.reset()  # Restart the game if it ends

# After loop ends
cv2.destroyAllWindows()
env.close()
