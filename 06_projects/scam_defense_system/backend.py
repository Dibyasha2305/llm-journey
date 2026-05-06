import ollama
import json

def analyze_message(message):
    prompt = f"""
    You are a cybersecurity AI specialized in scam detection.

    Analyze the following message:

    "{message}"

    Return ONLY valid JSON in the following format:

    {{
        "scam_type": "...",
        "risk_level": "...",
        "explanation": "...",
        "safe_reply": "..."
    }}

    Rules:
    - risk_level must be EXACTLY one of:
      LOW, MEDIUM, HIGH
    - Do not add extra text
    - Do not use markdown
    - Output only JSON
    """

    response = ollama.chat(
        model='mistral',
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    response_text = response['message']['content']

    data = json.loads(response_text)

    return data


if __name__ == "__main__":
    msg = input("Enter message: ")

    result = analyze_message(msg)

    print("\nAI Analysis:\n")

    print("Scam Type:", result["scam_type"])
    print("Risk Level:", result["risk_level"])
    print("Explanation:", result["explanation"])
    print("Safe Reply:", result["safe_reply"])