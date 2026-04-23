import requests
import time

# Aapka local FastAPI server URL
url = "http://127.0.0.1:8000/generate-code"

# Hum alag-alag intents test kar rahe hain
test_prompts = [
    "sort this array of numbers in descending order", # Should detect: Sorting
    "create a red submit button",                     # Should detect: UI_Component
    "find the maximum number in the data",            # Should detect: Math_Operation
    "reverse the characters in this sentence"         # Should detect: String_Manipulation
]

print("🚀 Starting Backend Tests...\n")

for prompt in test_prompts:
    print(f"👉 Testing Prompt: '{prompt}'")
    
    start_time = time.time()
    
    try:
        # Request bhej rahe hain
        response = requests.post(url, json={"prompt": prompt})
        
        if response.status_code == 200:
            data = response.json()
            generation_time = round(time.time() - start_time, 2)
            
            print(f"✅ Intent Detected : {data['detected_intent']}")
            print(f"⏱️ Generation Time: {generation_time} seconds")
            print(f"💻 Generated Code:\n{data['generated_code']}")
        else:
            print(f"❌ Error: {response.status_code} - {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Error: FastAPI server is not running. Please start it with 'uvicorn main:app --reload'")
        break
        
    print("-" * 50)