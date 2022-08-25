#Akinola Daramola Jr
#Programming Exercise 7.3
#Due Date: 07/31/2022

"""
Rainfall Statistics
Design a program that lets the user enter the total rainfall for each of 12 months into a list.
The program should calculate and display the total rainfall for the year,
the average monthly rainfall, the months with the highest and lowest amounts.
"""



#Declaring main() function
def main():
    #Invoking weatherApp()
    weatherApp()


#Defining weather App
def weatherApp():
    #Declaring list of string (Months of year)elements
    months = ["Jan","Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec" ]
    #Initializing index
    index = months.index("Jan")
    #Inidializing monthly_rainfall list
    monthly_rainfall = []
    #Initializing variables
    total_rainfall = 0
    averge_rainfall = 0
    number_of_months = 0
    lowest_month = 0
    highest_month = 0
    
    
    #Looping through months list
    for month in months:
        #Defining amount of rainfall dynamically
        rainfall = float(input(f"How much rain fell in {month}? "))
        #Appending monthly rainfall to list
        monthly_rainfall.append(rainfall)
        #Calculating total rainfall
        total_rainfall += rainfall
        #Increments 1 unit for every iteration (12) 
        number_of_months +=1
        #Calculate average rainfall
        average_rainfall = total_rainfall / number_of_months
        #Sorting list from least to greatest amount
        monthly_rainfall.sort()

        #Declaring value of highest_amount variable
        highest_amount = monthly_rainfall[-1]
        #Declaring value of lowest_amount variable
        lowest_amount = monthly_rainfall[0]
        #Incrementing 1 unit per iteration

        #if statement setting input value to highest position
        if rainfall == highest_amount:
            #Reassigning highest_month variable to corresponding month
            highest_month = months[index]
                
        #If statement setting input value to lowest position
        if rainfall == lowest_amount:
            #Reassigning lowest_month variable to corresponding
            lowest_month = months[index]
        #
        else:
            pass
                
        index += 1
        
    #Displaying total rainfall
    print(f"Total rainfall: {total_rainfall:,.2f}")
    #Displaying Average rainfall
    print(f"Avg rainfall: {average_rainfall:,.2f}")
    #Display month with lowest amount of rainfall
    print(f"Lowest Month is {lowest_month} with {lowest_amount}.")
    #Display month with highest amount of rainfall
    print(f"Highest Month is {highest_month} with {highest_amount}.")
    
    
        
#Invoking main() function     
main()


