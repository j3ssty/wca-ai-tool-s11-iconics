import os
import json
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("OPENAI_API_KEY")

# Create OpenAI client
client = OpenAI(api_key=api_key)


def analyze_feedback(feedback):
    """Analyze customer feedback using OpenAI."""

    prompt = f"""
Analyze the following customer feedback:

"{feedback}"

Return ONLY valid JSON in this format:

{{
    "sentiment": "positive, negative, or neutral",
    "category": "category of the feedback",
    "summary": "short summary",
    "priority": "low, medium, or high"
}}
"""

    try:
        response = client.responses.create(
            model="gpt-5.5",
            input=prompt
        )

        result = response.output_text.strip()
        analysis = json.loads(result)

        return analysis

    except json.JSONDecodeError:
        print("Error: AI returned invalid JSON.")
        return None

    except Exception as e:
        print(f"API Error: {e}")
        return None


def generate_response(feedback, analysis):
    """Generate a professional response to the customer."""

    prompt = f"""
Customer feedback:

"{feedback}"

Feedback analysis:

{json.dumps(analysis, indent=2)}

Write a polite and professional response to the customer.
"""

    try:
        response = client.responses.create(
            model="gpt-5.5",
            input=prompt
        )

        return response.output_text.strip()

    except Exception as e:
        print(f"API Error: {e}")
        return None