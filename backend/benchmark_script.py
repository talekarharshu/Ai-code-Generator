import requests
import time
import csv

# local FastAPI server
URL = "http://127.0.0.1:8000/generate-code"

# The Test Dataset: A mix of different tasks to test the NLP router
test_dataset = [
    
    # -- JS: Math Operations --
    {"prompt": "Write a JavaScript function to add two numbers.", "expected_intent": "Math_Operation"},
    {"prompt": "Write a JavaScript function to subtract two numbers.", "expected_intent": "Math_Operation"},
    {"prompt": "Write a JavaScript function to multiply two numbers.", "expected_intent": "Math_Operation"},
    {"prompt": "Write a JavaScript function to divide two numbers.", "expected_intent": "Math_Operation"},
    {"prompt": "Write a JS function to calculate the square of a number.", "expected_intent": "Math_Operation"},
    {"prompt": "Create a JavaScript function to find the cube of a number.", "expected_intent": "Math_Operation"},
    {"prompt": "Write a JavaScript function to find the remainder of two numbers.", "expected_intent": "Math_Operation"},
    {"prompt": "Create a JS function that returns true if a number is even.", "expected_intent": "Math_Operation"},
    {"prompt": "Create a JS function that returns true if a number is odd.", "expected_intent": "Math_Operation"},
    {"prompt": "Write a JavaScript function to calculate the area of a rectangle.", "expected_intent": "Math_Operation"},
    {"prompt": "Write a JavaScript function to calculate the perimeter of a square.", "expected_intent": "Math_Operation"},
    {"prompt": "Write a JS function to convert Celsius to Fahrenheit.", "expected_intent": "Math_Operation"},
    {"prompt": "Write a JS function to convert Fahrenheit to Celsius.", "expected_intent": "Math_Operation"},
    {"prompt": "Create a JS function to calculate simple interest.", "expected_intent": "Math_Operation"},
    {"prompt": "Write a JavaScript function to find the maximum of two numbers.", "expected_intent": "Math_Operation"},
    {"prompt": "Write a JavaScript function to find the minimum of two numbers.", "expected_intent": "Math_Operation"},
    {"prompt": "Create a JS function to generate a random number between 1 and 10.", "expected_intent": "Math_Operation"},
    {"prompt": "Write a JavaScript function to calculate the factorial of 5.", "expected_intent": "Math_Operation"},

    # -- JS: String Manipulation --
    {"prompt": "Write a JavaScript function to reverse a string.", "expected_intent": "String_Manipulation"},
    {"prompt": "Create a JS function to convert a string to uppercase.", "expected_intent": "String_Manipulation"},
    {"prompt": "Create a JS function to convert a string to lowercase.", "expected_intent": "String_Manipulation"},
    {"prompt": "Write a JavaScript function to find the length of a string.", "expected_intent": "String_Manipulation"},
    {"prompt": "Write a JS function to concatenate two strings.", "expected_intent": "String_Manipulation"},
    {"prompt": "Create a JavaScript function to check if a string is a palindrome.", "expected_intent": "String_Manipulation"},
    {"prompt": "Write a JS function to count the number of vowels in a word.", "expected_intent": "String_Manipulation"},
    {"prompt": "Write a JS function to get the first character of a string.", "expected_intent": "String_Manipulation"},
    {"prompt": "Write a JS function to get the last character of a string.", "expected_intent": "String_Manipulation"},
    {"prompt": "Create a JavaScript function to remove spaces from a string.", "expected_intent": "String_Manipulation"},
    {"prompt": "Write a JS function to repeat a string 3 times.", "expected_intent": "String_Manipulation"},
    {"prompt": "Write a JavaScript function to replace a word in a string.", "expected_intent": "String_Manipulation"},
    {"prompt": "Create a JS function that splits a sentence into an array of words.", "expected_intent": "String_Manipulation"},
    {"prompt": "Write a JS function to capitalize the first letter of a string.", "expected_intent": "String_Manipulation"},
    {"prompt": "Write a JS function to check if a string contains a specific word.", "expected_intent": "String_Manipulation"},

    # -- JS: Sorting & Arrays --
    {"prompt": "Write a JavaScript function to sort an array of numbers in ascending order.", "expected_intent": "Sorting"},
    {"prompt": "Write a JS function to sort an array of numbers in descending order.", "expected_intent": "Sorting"},
    {"prompt": "Create a JS function to sort an array of strings alphabetically.", "expected_intent": "Sorting"},
    {"prompt": "Write a JavaScript function to reverse an array.", "expected_intent": "Sorting"},
    {"prompt": "Write a JS function to find the largest number in an array.", "expected_intent": "Basic_Logic"},
    {"prompt": "Write a JS function to find the smallest number in an array.", "expected_intent": "Basic_Logic"},
    {"prompt": "Create a JavaScript function to return the first element of an array.", "expected_intent": "Basic_Logic"},
    {"prompt": "Create a JS function to return the last element of an array.", "expected_intent": "Basic_Logic"},
    {"prompt": "Write a JS function to remove the first element of an array.", "expected_intent": "Basic_Logic"},
    {"prompt": "Write a JS function to add an element to the end of an array.", "expected_intent": "Basic_Logic"},
    {"prompt": "Create a JS function to sum all numbers in an array.", "expected_intent": "Math_Operation"},

    # -- JS: UI Components --
    {"prompt": "Write JS code to create an HTML button with text 'Click Me'.", "expected_intent": "UI_Component"},
    {"prompt": "Write JavaScript to change the background color of a webpage to red.", "expected_intent": "UI_Component"},
    {"prompt": "Create a JS function to show a browser alert with 'Hello'.", "expected_intent": "UI_Component"},
    {"prompt": "Write JavaScript to hide an HTML element by ID.", "expected_intent": "UI_Component"},
    {"prompt": "Create JS code to generate an HTML text input field.", "expected_intent": "UI_Component"},
    {"prompt": "Write JavaScript to change the text inside a div.", "expected_intent": "UI_Component"},

    
    # -- javascript: Math Operations --
    {"prompt": "Write a javascript function to add two numbers together.", "expected_intent": "Math_Operation"},
    {"prompt": "Create a javascript program to calculate the square root of a number.", "expected_intent": "Math_Operation"},
    {"prompt": "Write a javascript script to find if a number is prime.", "expected_intent": "Math_Operation"},
    {"prompt": "Create a javascript function to multiply three numbers.", "expected_intent": "Math_Operation"},
    {"prompt": "Write a javascript function to calculate the area of a circle.", "expected_intent": "Math_Operation"},
    {"prompt": "Create a javascript program to check if a number is positive or negative.", "expected_intent": "Math_Operation"},
    {"prompt": "Write a javascript script to convert km to miles.", "expected_intent": "Math_Operation"},
    {"prompt": "Create a javascript function that returns the absolute value of a number.", "expected_intent": "Math_Operation"},
    {"prompt": "Write a javascript function to find the average of a list of numbers.", "expected_intent": "Math_Operation"},
    {"prompt": "Create a javascript program to calculate 10 percent of a value.", "expected_intent": "Math_Operation"},

    # -- javascript: String Manipulation --
    {"prompt": "Write a javascript function to reverse a string.", "expected_intent": "String_Manipulation"},
    {"prompt": "Create a javascript script to convert a string to uppercase.", "expected_intent": "String_Manipulation"},
    {"prompt": "Write a javascript program to count how many times 'a' appears in a word.", "expected_intent": "String_Manipulation"},
    {"prompt": "Create a javascript function to concatenate a first name and last name.", "expected_intent": "String_Manipulation"},
    {"prompt": "Write a javascript script to check if a word is a palindrome.", "expected_intent": "String_Manipulation"},
    {"prompt": "Create a javascript function to strip white spaces from a string.", "expected_intent": "String_Manipulation"},
    {"prompt": "Write a javascript program to replace commas with spaces in a text.", "expected_intent": "String_Manipulation"},

    # -- javascriptscript: Sorting & Data --
    {"prompt": "Write a javascript function to sort a list of integers.", "expected_intent": "Sorting"},
    {"prompt": "Create a javascript script to sort a dictionary by keys.", "expected_intent": "Sorting"},
    {"prompt": "Write a javascript program to reverse a list.", "expected_intent": "Sorting"},
    {"prompt": "Create a javascript function to return the maximum value in a list.", "expected_intent": "Basic_Logic"},
    {"prompt": "Write a javascript script to remove duplicates from a list.", "expected_intent": "Basic_Logic"},


    # -- javascript: Math & Logic --
    {"prompt": "Write a javascript method to add two integers.", "expected_intent": "Math_Operation"},
    {"prompt": "Create a javascript program to find the factorial of 5 using a loop.", "expected_intent": "Math_Operation"},
    {"prompt": "Write a javascript method to check if a number is even or odd.", "expected_intent": "Math_Operation"},
    {"prompt": "Create a javascript class that multiplies two floating-point numbers.", "expected_intent": "Math_Operation"},
    {"prompt": "Write a javascript method to return the greater of two numbers.", "expected_intent": "Math_Operation"},
    {"prompt": "Create a javascript program to print the Fibonacci series up to 10.", "expected_intent": "Math_Operation"},
    {"prompt": "Write a javascript method to calculate the volume of a sphere.", "expected_intent": "Math_Operation"},
    {"prompt": "Create a javascript program to determine if a year is a leap year.", "expected_intent": "Math_Operation"},
    
    # -- javascript: String Manipulation --
    {"prompt": "Write a javascript method to reverse a String object.", "expected_intent": "String_Manipulation"},
    {"prompt": "Create a javascript program to find the length of a String.", "expected_intent": "String_Manipulation"},
    {"prompt": "Write a javascript method to convert a String to lower case.", "expected_intent": "String_Manipulation"},
    {"prompt": "Create a javascript program to check if two strings are equal.", "expected_intent": "String_Manipulation"},
    {"prompt": "Write a javascript method to extract a substring from a given string.", "expected_intent": "String_Manipulation"},
    {"prompt": "Create a javascript program to count the number of words in a sentence.", "expected_intent": "String_Manipulation"},
    {"prompt": "Write a javascript method to replace all vowels in a string with 'x'.", "expected_intent": "String_Manipulation"},

    # -- javascript: Arrays & Sorting --
    {"prompt": "Write a javascript method to sort an array of integers using Arrays.sort.", "expected_intent": "Sorting"},
    {"prompt": "Create a javascript program to implement bubble sort on an array.", "expected_intent": "Sorting"},
    {"prompt": "Write a javascript method to find the sum of all elements in an array.", "expected_intent": "Math_Operation"},
    {"prompt": "Create a javascript program to find the largest element in an integer array.", "expected_intent": "Basic_Logic"},
    {"prompt": "Write a JavaScript method to copy elements from one array to another.", "expected_intent": "Basic_Logic"},
    
    
    # MIXED & EDGE CASES (Target: NLP Router Stress Test)
  
    {"prompt": "Write a C++ function to add numbers.", "expected_intent": "Math_Operation"},
    {"prompt": "Create a Ruby script to reverse text.", "expected_intent": "String_Manipulation"},
    {"prompt": "Write a PHP function to sort an array.", "expected_intent": "Sorting"},
    {"prompt": "Create a Go function to find the square root.", "expected_intent": "Math_Operation"},
    {"prompt": "Write a Swift method to capitalize a string.", "expected_intent": "String_Manipulation"}
]

print(f"🚀 Starting Benchmark for {len(test_dataset)} prompts...\n")

# Open a CSV file to save our research data
with open('research_results.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the column headers for our Excel sheet
    writer.writerow(["Prompt", "Expected Intent", "Detected Intent", "Intent Match?", "Attempts Needed", "Success Status", "Generation Time (s)"])

    successful_generations = 0
    auto_corrected_count = 0

    for i, test in enumerate(test_dataset):
        print(f"⏳ Testing [{i+1}/{len(test_dataset)}]: '{test['prompt']}'")
        start_time = time.time()
        
        try:
            response = requests.post(URL, json={"prompt": test["prompt"]})
            
            if response.status_code == 200:
                data = response.json()
                generation_time = round(time.time() - start_time, 2)
                
                # Extract data
                detected_intent = data.get('detected_intent', 'Unknown')
                attempts = data.get('attempts_taken', 1)
                success = data.get('success', False)
                
                # Check if our NLP router guessed correctly
                intent_match = "Yes" if detected_intent == test['expected_intent'] else "No"
                
                if success:
                    successful_generations += 1
                if attempts > 1 and success:
                    auto_corrected_count += 1
                
                # Save the row to CSV
                writer.writerow([
                    test["prompt"], 
                    test["expected_intent"], 
                    detected_intent, 
                    intent_match, 
                    attempts, 
                    "Pass" if success else "Fail", 
                    generation_time
                ])
                
            else:
                print(f"❌ Server Error: {response.status_code}")
                writer.writerow([test["prompt"], test["expected_intent"], "Error", "N/A", "N/A", "Error", "N/A"])
                
        except Exception as e:
            print(f"❌ Connection Error: {e}")
            break

print("\n✅ Benchmarking Complete!")
print(f"📊 Results saved to 'research_results.csv'")
print("-" * 30)
print(f"Total Successful Generations: {successful_generations}/{len(test_dataset)}")
print(f"Errors Auto-Corrected by AST: {auto_corrected_count}")