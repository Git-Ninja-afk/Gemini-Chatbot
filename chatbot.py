import os
import google.generativeai as genai
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

# Store conversation history
chat_history = []

def chat(user_input):
    chat_history.append({
        "role": "user",
        "parts": [user_input]
    })
    
    response = model.generate_content(chat_history)
    assistant_response = response.text
    
    chat_history.append({
        "role": "model",
        "parts": [assistant_response]
    })
    
    return assistant_response

def save_chat():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"chat_{timestamp}.txt"
    with open(filename, "w") as f:
        for message in chat_history:
            role = "You" if message["role"] == "user" else "Gemini"
            f.write(f"{role}: {message['parts'][0]}\n\n")
    print(f"✅ Chat saved to {filename}")

def main():
    print("🤖 GEMINI AI CHATBOT")
    print("=" * 50)
    print("Powered by Google Gemini 1.5 Flash")
    print("Commands: 'quit' to exit | 'save' to save chat | 'clear' to clear history")
    print("=" * 50)

    while True:
        try:
            user_input = input("\n You: ").strip()

            if not user_input:
                continue

            if user_input.lower() == "quit":
                print("👋 Goodbye!")
                break

            if user_input.lower() == "save":
                save_chat()
                continue

            if user_input.lower() == "clear":
                chat_history.clear()
                print("🗑️ Chat history cleared!")
                continue

            print("\n🤖 Gemini: ", end="", flush=True)
            response = chat(user_input)
            print(response)

        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()
