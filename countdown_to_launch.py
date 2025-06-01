'''
Countdown to Launch
Write a program to simulate a rocket launch countdown.

The program should display the countdown timer alongside the seconds elapsed at each step.

Write a program that:

Take the starting countdown value (in seconds) as input.
Use a while loop to display the remaining countdown time and elapsed time at each step. The loop should terminate when countdown becomes less than 0.
Print a separator (---) after every update for better readability.
End the program with the message: "Liftoff!".
Hint: You need to update both the countdown and elapsed variables inside the loop.

'''
# Take integer input
countdown = int(input("Enter starting countdown number: "))
i = countdown
elapsed = 0

while (elapsed <= i) and (countdown >= 0):
    print(f"Time left: {countdown} seconds")
    print(f"Elapsed: {elapsed} seconds")
    print("---")
    countdown = countdown - 1
    elapsed = elapsed + 1

# Print the "Liftoff!" message
print("Liftoff!")