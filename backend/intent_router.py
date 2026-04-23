from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# 1. Hamara Training Dataset (You can add more examples later)
training_data = [
    ("sort this array of numbers", "Sorting"),
    ("arrange the list in ascending order", "Sorting"),
    ("create a button that clicks", "UI_Component"),
    ("make a text input field", "UI_Component"),
    ("find the maximum number in the array", "Math_Operation"),
    ("calculate the average of these values", "Math_Operation"),
    ("reverse this string", "String_Manipulation"),
    ("capitalize the first letter of the word", "String_Manipulation")
]

# Split data into inputs (X) and labels (y)
X_train = [text for text, label in training_data]
y_train = [label for text, label in training_data]

# 2. Build and Train the NLP Pipeline
# TfidfVectorizer words ko numbers me convert karta hai, aur MultinomialNB unhe classify karta hai
intent_classifier = make_pipeline(TfidfVectorizer(), MultinomialNB())
intent_classifier.fit(X_train, y_train)

def get_intent(user_prompt):
    """Predicts the intent of the user's prompt."""
    prediction = intent_classifier.predict([user_prompt])
    return prediction[0]

# 3. Prompt Templates based on Intent
def get_optimized_prompt(user_prompt, intent):
    """
    Advanced Prompt Engineering using Few-Shot and Context Formatting.
    This gives the 350M model a strict pattern to follow.
    """
    
    # 1. FEW-SHOT SORTING TEMPLATE
    # Hum pehle ek example solve karke dikha rahe hain, fir apna task de rahe hain.
    if intent == "Sorting":
        return f"""// Language: JavaScript
// Task: sort numbers in ascending order
function exampleSort(arr) {{
    return arr.sort((a, b) => a - b);
}}

// Task: {user_prompt}
function solution(arr) {{"""

    # 2. FEW-SHOT MATH TEMPLATE
    elif intent == "Math_Operation":
        return f"""// Language: JavaScript
// Task: find the sum of two numbers
function exampleSum(a, b) {{
    return a + b;
}}

// Task: {user_prompt}
function solution(data) {{"""

    # 3. DOMAIN-SPECIFIC UI TEMPLATE
    # Frontend logic ke liye hum DOM manipulation ka pattern set kar rahe hain
    elif intent == "UI_Component":
        return f"""// Language: JavaScript DOM API
// Task: create a simple div element
function createDiv() {{
    const el = document.createElement('div');
    return el;
}}

// Task: {user_prompt}
function createUI() {{"""

    # 4. CHAIN-OF-THOUGHT STRING TEMPLATE
    # Hum model ko step-by-step sochne (comments likhne) ke liye force kar rahe hain
    elif intent == "String_Manipulation":
        return f"""// Language: JavaScript
// Task: {user_prompt}
// Step 1: Process the input string
// Step 2: Return the final result
function processText(str) {{"""

    # Default Fallback (Zero-Shot)
    else:
        return f"// Language: JavaScript\n// Task: {user_prompt}\nfunction executeTask() {{"