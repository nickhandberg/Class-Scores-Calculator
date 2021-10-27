# Nicholas Handberg, Assignment 4, 2/2/2021
# Topics: List, file input/output
# Create a program to read, compute, and save grade data

descript = ["Min =      ","Max =      ","Mean =     ","Median =   "]                            # Stores the string elements into a list called descript for use later on screen and file output

def load_score(filename):                                                                       # Defines the load_score function with parameter 'filename'
    try:                                                                                        # Try/except used in case of a FileNotFoundError
        with open(filename, 'r') as f:                                                          # Opens the file in read mode
            scores_temp = [int(x) for x in next(f).split()]                                     # Splits the data by spaces and stores them as int into the list 'scores_temp'
            scores = sorted(scores_temp)                                                        # Sorts the list numerically from lowest to highest

        print('\nData read successfully')                                                       # Prints Data read successfully
        f.close()                                                                               # Closes the file
        return (scores)                                                                         # Returns the list 'scores'
    
    except ValueError:
        
        print("\nThe file you are trying to load does not exist")                               # If there was a FileNotFoundError, prints a message stating that the file does not exist

def save_score(filename, scores):                                                               # Defines the save_score function with parameters 'filename' and 'scores'
    calc = calculations(scores)                                                                 # Calls the calculations() function with scores as arguments and stores the returned list into 'calc'
    save_data = open(filename, 'w')                                                             # Opens the file in write mode and assigns it to 'save_data'
    
    for x in range (0,4,1):                                                                     # For loop to write elements 0-3 of the lists 'descript' and 'calc' to the file
        save_data.write(descript[x] + calc[x] +"\n")                                            # As it loops, it will store the description and respective calculation to new lines in the file
    save_data.close()                                                                           # Closes the file
    print(f"\nData has been stored in {filename}")                                              # Prints that the data has been store in 'filename'
        
def main():                                                                                     # Defines the main() function
    data_read = False                                                                           # Assigns boolean 'False' to 'data_read'
    user_input = 'temp'                                                                         # Assigns 'temp' to 'user_input' in order to start the while loop
    while user_input != 4:                                                                      # While loop to keep looping until 'user_input' == 4
        
        print("\nChoose an option:")                                                            # Prints the options the user may choose from to the user's display
        print("1.   Load Data")
        print("2.   Display computed statistics")
        print("3.   Save computed statistics")
        print("4.   Exit")
        
        try:                                                                                    # Try/except to account for ValueError i.e. user inputing a string
            user_input = int(input("\n\n>"))                                                    # Gets the user's input, converts it to an integer and stores it in 'user_input'
            
            if user_input == 1:                                                                 # If statement to check if the user input 1
                
                load_file_name = str(input("\nEnter the name of the file:  "))                  # Asks the user to input the filename of the file they want to load
                (scores) = load_score(load_file_name)                                           # Calls the load_score() function with 'load_file_name' as an argument and stores the returned list into 'scores'
                data_read = True                                                                # Sets data_read to 'True' as the data has now been read
                
            elif user_input == 2 and data_read == True:                                         # Elif statement to check if the user input 2 and if the data has been read
                
                calc = calculations(scores)                                                     # Calls the calculations() function with 'scores' as an argument and stores the returned list into 'calc'
                for x in range(0,4,1):                                                          # For loop to print elements 0-3 of the lists 'descript' and 'calc' to the user's screen
                    print(descript[x] + calc[x])                                                # As it loops, it will print the description and respective calculation to new lines on the user's screen
                
            elif user_input == 3 and data_read == True:                                         # Elif statement to check if the user input 3 and if the data has been read
                  
                save_file_name = str(input("Enter the name of the file:  "))                    # Asks the user to input the filename of the save file they will be creating
                save_score(save_file_name, scores)                                              # Calls the save_score() function with 'save_file_name' and 'scores' as arguments
                
            elif user_input == 4:                                                               # Elif statement to check if the user input 4
                
                print("\nGoodbye!")                                                             # Prints "Goodbye!" if the user had input 4
                
            elif data_read == False and user_input in (2,3,1):                                  # Elif to check if the user has input 2 or 3 before reading the data 
                
                print("You need to load data before displaying or saving computed statistics")  # Prints that the user must first load data before displaying or saving computed statistics
            
            else:                                                                               # Else statement in case the user enters an invalid command
                
                print("Please enter a valid command (1,2,3,4)")                                 # Tells the user to input a valid command
                
        except ValueError:                                                                      # Except in case the user enters a letter causing a ValueError above
            
            print("Please enter a valid command (1,2,3,4)")                                     # Tells the user to input a valid command
                   
def calculations(scores):                                                                       # Defines the calculations() functions with 'scores' as a parameter
    length = len(scores)                                                                        # Finds the length of the list 'scores' and stores it in 'length'
    score_min = minimum(scores)                                                                 # Calls the minimum() function with 'scores' as a argument and stores the return in 'score_min'
    score_max = maximum(scores,length)                                                          # Calls the maximum() function with 'scores' and 'length' as arguments and stores the return in 'score_max'
    score_mean = mean(scores,length)                                                            # Calls the mean() function with 'scores' and 'length' as arguments and stores the return in 'score_mean'
    score_median = median(scores,length)                                                        # Calls the median() function with 'scores' and 'length' as arguments and stores the return in 'score_median'
    
    return (score_min, score_max, score_mean, score_median)                                     # Returns the min, max, mean, and median as a list

def minimum(scores):                                                                            # Defines the minimum() function with 'scores' as a parameter
    
    score_min = (f"{scores[0]:.0f}")                                                            # Stores the first element in the 'scores' list into 'score_min'
    return score_min                                                                            # Returns 'score_min'

def maximum(scores,length):                                                                     # Defines the maximum() function with 'scores' and 'length' as parameters

    score_max = (f"{scores[length-1]:.0f}")                                                     # Stores the last element in the 'scores' list into 'score_max'
    return score_max                                                                            # Returns 'score_max'

def mean(scores,length):                                                                        # Defines the mean() function with 'scores' and 'length' as parameters
    
    total = sum(scores)                                                                         # Sums the 'scores' list elements and stores the value into 'total'
    score_mean = (f"{(total/length):.1f}")                                                      # Stores the result from 'total' divided by 'length' into 'score_mean'
    return score_mean                                                                           # Returns 'score_mean'

def median(scores,length):                                                                      # Defines the median() function with 'scores' and 'length' as parameters

    if (length % 2) == 0:                                                                       # If statement to check if the length of the list is even
        n = int((length-1) / 2)                                                                 # Calculates the number of the lower middle element's position in the list and stores its value in 'n' 
        x1 = scores[n]                                                                          # Stores the value of the lower middle element in 'x1'
        x2 = scores[n+1]                                                                        # Stores the value of the upper middle element in 'x2'
        score_median = (f"{((x1+x2)/2):.1f}")                                                   # Averages 'x1' and 'x2' and stores the result in 'score_median'
        return score_median                                                                     # Returns 'score_median'
    
    else:                                                                                       # Else statement for if the length of the list is odd
        n = (length // 2)                                                                       # Calculates the middle element's position and stores its value in 'n'
        score_median = (f"{scores[n]:.1f}")                                                     # Stores the value of the middle element into 'score_median'
        return score_median                                                                     # Returns 'score_median'
        
main()                                                                                          # Calls the main() function