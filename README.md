# Random_Number_Generator
My first project. A small curiosity project after encountering random module in Python. Done the help of my dad.
-------------------------------------------------------------------------------------------------x

The state of this random number sequence generator is not ideal. The external source of randomness is microseconds, by importing the datetime module. A polynomial equation with microseconds being added on as a 4 digit constant, is used and the x variable is incremented. That value is reduced to its first 8 bits by using the logical function AND(& FF). So the highest value can be 255. I've attempted to test the randomness of the sequence with a loop but due to the speed of the loop it sabotages external source of randomness which is microsecond (that is my theory). Also the polynomial is not mathematically proven to give 255 unique values. It work great with a few required numbers (to make a list of 10 random numbers), but it occasionally(radically) gives repeating values when more numbers are requeired (150 random numbers) 
Even though it has resulted in a very dodgy and poor performing inefficient algorithm, It was a very fun project to work on. I intend to revisit this project later on. 
