--[[ If you haven't gone to the gym in at least a week,

and you have free time today,  or you ate a double cheese burger with fries for lunch,  go to the gym. --]]

print("Hello!")
print("Have you gone to the gym this week? Y/N")

visit = io.read()
if (visit == "Y") then
    print("Great! You have successfully reached your goal this week!")
elseif (visit == "N") then
    print("Did you eat a cheeseburger with fries for lunch? Y/N")
    lunch = io.read()
    print("Do you have free time today? Y/N")
    time = io.read()
    if (lunch == "Y" and time == "N") then
        print("Make some time. You have to stay healthy as possible!")
    elseif (time == "Y") then
        print("Then let's go workout!")
    else
        print("That's too bad. We can check again tomorrow?")
    end
else
    print("Incorrect response. Please try again.")
end
