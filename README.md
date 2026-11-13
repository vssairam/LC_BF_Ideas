# 🥗 Healthy Breakfast Ideas Generator

### A LangChain + OpenAI Project

A simple Python application that uses **LangChain's ChatOpenAI** to generate exactly five healthy breakfast ideas.

This project demonstrates prompt engineering, handling LangChain `AIMessage` objects, and understanding how model temperature influences response variability.

## 📌 Project Overview

The application sends a carefully structured prompt to an OpenAI language model and prints five healthy breakfast suggestions.

The program ensures that:

- Exactly five breakfast ideas are requested.
- Ideas are numbered from 1 to 5.
- Each suggestion appears on a separate line.
- No introduction, conclusion, or additional explanation is requested.
- Only the generated response text is printed.
- The OpenAI API key is loaded securely from an environment variable.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| LangChain | LLM integration |
| ChatOpenAI | Interaction with OpenAI |
| GPT-4o-mini | Language model |
| python-dotenv | Environment variable management |

## 📁 Project Structure

```text
LC_BF_Ideas/
│
├── breakfast.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

**Note:** The `.env` file is excluded from Git to protect the OpenAI API key.

## ⚙️ Installation and Setup

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd LC_BF_Ideas
```

Replace `<repository-url>` with the actual GitHub repository URL.

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Configure the OpenAI API Key

Copy `.env.example` to a new file named `.env`.

Update the file with your OpenAI API key:

```dotenv
OPENAI_API_KEY=your_actual_openai_api_key
```

Never commit your actual API key to GitHub.

## 🚀 Running the Application

Execute:

```bash
python breakfast.py
```

The application connects to the OpenAI model and prints five healthy breakfast ideas.

## 💻 How the Application Works

The application is organized into clearly defined sections.

### 1. Import Libraries

Imports the required Python modules, `python-dotenv`, and LangChain's `ChatOpenAI`.

### 2. Load Environment Variables

Loads the OpenAI API key from the `.env` file and checks whether it is configured.

### 3. Initialize the Model

Creates a LangChain `ChatOpenAI` instance using:

```python
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)
```

The temperature setting influences the variation in generated responses.

### 4. Define the Prompt

The prompt requests exactly five healthy breakfast ideas and specifies the required output format.

### 5. Invoke the Model

The application sends the prompt using:

```python
response = llm.invoke(prompt)
```

LangChain returns an `AIMessage` object rather than a plain string.

### 6. Extract and Print the Response

```python
print(response.content)
```

The `.content` attribute extracts the generated text from the message object.

This ensures that the program prints only the model's response, without additional message metadata.

## 🧪 Execution Results

The application was executed twice using the same prompt and model configuration.

### Run 1

```text
1. Greek yogurt with mixed berries and a sprinkle of chia seeds.
2. Overnight oats with almond milk, banana slices, and walnuts.
3. Scrambled eggs with spinach and cherry tomatoes on whole-grain toast.
4. Smoothie with spinach, banana, protein powder, and almond butter.
5. Quinoa bowl with diced avocado, black beans, and lime juice.
```

### Run 2

```text
1. Greek yogurt topped with mixed berries and a sprinkle of chia seeds.
2. Oatmeal cooked with almond milk, sliced bananas, and a dash of cinnamon.
3. Whole grain toast with smashed avocado, cherry tomatoes, and a poached egg.
4. Smoothie with spinach, banana, peanut butter, and almond milk.
5. Cottage cheese with pineapple chunks and a handful of walnuts.
```

## 📊 Comparison of Both Executions

| Idea | Run 1 | Run 2 | Observation |
|---|---|---|---|
| 1 | Greek yogurt, berries, chia seeds | Greek yogurt, berries, chia seeds | Nearly identical |
| 2 | Overnight oats, banana, walnuts | Oatmeal, banana, cinnamon | Similar concept |
| 3 | Scrambled eggs with toast | Avocado toast with poached egg | Different preparation |
| 4 | Smoothie with almond butter | Smoothie with peanut butter | Similar concept |
| 5 | Quinoa bowl with avocado and beans | Cottage cheese with pineapple | Different ideas |

### Key Observations

1. Both executions generated exactly five breakfast suggestions.
2. Both responses followed the required numbered format.
3. The model produced different suggestions despite receiving the same prompt.
4. Some ideas were conceptually similar, while others differed significantly.
5. The temperature setting of `0.7` allows some variation in the generated responses.

## 🌡️ Understanding Temperature

Temperature influences the variability of language model outputs.

| Temperature | Typical Behavior |
|---|---|
| 0.0 | More consistent and predictable |
| 0.5 | Moderate variation |
| 0.7 | Balanced creativity and consistency |
| 1.0 | Greater variation |

**Important:** Temperature influences response variability, but identical outputs are not guaranteed at low temperatures. Differences between two runs cannot be attributed exclusively to temperature.

### Experiment Conclusion

The application demonstrated that a precise prompt can maintain a consistent output format even when the generated content varies.

This is particularly useful when developing AI applications that require structured and predictable responses.

## ✅ Assignment Requirements Checklist

| Requirement | Status |
|---|---|
| Single Python file named `breakfast.py` | ✅ |
| Use LangChain's `ChatOpenAI` | ✅ |
| Generate exactly five breakfast ideas | ✅ |
| Print only the response text | ✅ |
| Number ideas from 1 to 5 | ✅ |
| One idea per line | ✅ |
| No preamble | ✅ |
| Run the application twice | ✅ |
| Compare both executions | ✅ |
| Read the API key from an environment variable | ✅ |

## 🎯 Learning Outcomes

This assignment provided practical experience in:

- Integrating OpenAI models through LangChain.
- Designing precise prompts for structured responses.
- Understanding LangChain's `invoke()` method.
- Extracting text from an `AIMessage` object using `.content`.
- Managing API keys securely through environment variables.
- Observing the variability of LLM-generated responses.
- Understanding the importance of temperature when building AI applications.

## 🏁 Conclusion

Successfully developed and executed a Python-based Healthy Breakfast Ideas Generator using LangChain and OpenAI.

The application generated exactly five numbered breakfast suggestions in both executions while demonstrating variations in the generated content.

The project highlights three important principles of LLM application development:

**Prompt Precision + Correct Response Handling + Understanding Model Variability**

These concepts form a foundation for developing reliable applications using LangChain.