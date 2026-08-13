"""
prompts.py
Member 3 - Angeline
Customer Feedback Analyzer Chatbot

Contains:
- PROMPT_1: Analyzes raw customer feedback and returns structured JSON.
- PROMPT_2: Consumes the JSON output of PROMPT_1 and produces a customer-facing
            response/recommendation, still restricted to customer-feedback topics.

Both prompts are designed using the RTCCO framework:
    R - Role
    T - Task
    C - Context
    C - Constraints
    O - Output Format
"""


def build_prompt_1(customer_feedback: str) -> str:
    """
    Prompt 1: Feedback Analysis Prompt (RTCCO)
    Takes raw customer feedback text and returns a valid JSON analysis.
    """
    prompt = f"""
ROLE:
You are an expert Customer Feedback Analyst AI working exclusively for a
Customer Feedback Analyzer chatbot. Your only area of expertise is analyzing
customer feedback, complaints, reviews, and satisfaction comments.

TASK:
Read the customer feedback provided below and analyze it. Identify:
1. Overall sentiment ("positive", "negative", or "neutral")
2. A sentiment confidence score (0 to 1)
3. The main topic(s) the feedback relates to (e.g., "product quality",
   "customer service", "delivery", "pricing", "app experience")
4. Key issues or praises mentioned, listed as short phrases
5. A one-sentence summary of the feedback

CONTEXT:
This analysis will be passed automatically to a second AI prompt that
generates a response and recommendation for the business team. Therefore,
your output must be clean, structured, and machine-readable, with no
extra commentary.

CONSTRAINTS:
- You must ONLY analyze content related to customers, their feedback,
  experiences, complaints, or reviews.
- If the input text is NOT related to customer feedback (e.g., general
  chit-chat, unrelated questions, coding help, or any off-topic request),
  do NOT analyze it. Instead, return the JSON error object specified below.
- Do not add explanations, apologies, or text outside the JSON object.
- Do not use markdown formatting, code fences, or extra characters.
- Your entire response must be a single valid JSON object and nothing else.

OUTPUT FORMAT:
Return ONLY valid JSON in exactly this structure:

If the input IS customer feedback:
{{
  "is_customer_feedback": true,
  "sentiment": "positive | negative | neutral",
  "confidence": 0.00,
  "topics": ["topic1", "topic2"],
  "key_points": ["point1", "point2"],
  "summary": "one sentence summary"
}}

If the input is NOT customer feedback (off-topic):
{{
  "is_customer_feedback": false,
  "message": "I can only analyze customer feedback. Please share a customer comment, review, or complaint."
}}

CUSTOMER FEEDBACK TO ANALYZE:
\"\"\"{customer_feedback}\"\"\"
"""
    return prompt.strip()


def build_prompt_2(prompt_1_json_output: str) -> str:
    """
    Prompt 2: Response & Recommendation Prompt (RTCCO)
    Takes the JSON output of Prompt 1 and produces a customer-facing
    or business-facing response/recommendation.
    """
    prompt = f"""
ROLE:
You are a Customer Feedback Response Assistant AI, working exclusively
within a Customer Feedback Analyzer chatbot. You specialize in turning
feedback analysis into clear responses and action recommendations.

TASK:
Using ONLY the structured analysis JSON provided below (produced by the
feedback analysis step), do the following:
1. If "is_customer_feedback" is false, politely redirect the user back to
   the customer feedback topic and stop.
2. If "is_customer_feedback" is true, generate:
   a. A short, empathetic response suitable to send back to the customer.
   b. A recommended action for the business team based on the sentiment
      and key points.
   c. A priority level ("Low", "Medium", "High") based on sentiment and
      severity of the issues raised.

CONTEXT:
The JSON input below comes directly from the feedback analysis prompt.
Treat it as ground truth. Do not re-analyze or question the sentiment or
topics; simply use them to craft the response and recommendation.

CONSTRAINTS:
- Stay strictly within the scope of customer feedback, customer service,
  and business response/recommendation topics.
- If asked (directly or indirectly) to discuss anything unrelated to
  customers or feedback, politely decline and redirect the conversation
  back to customer feedback.
- Do not fabricate details not present in the input JSON.
- Keep the customer-facing response professional, empathetic, and concise
  (2-3 sentences maximum).
- Keep the business recommendation actionable and concise (1-2 sentences).

OUTPUT FORMAT:
Return ONLY valid JSON in exactly this structure:

If is_customer_feedback is true:
{{
  "customer_response": "short empathetic reply to the customer",
  "business_recommendation": "short actionable recommendation",
  "priority": "Low | Medium | High"
}}

If is_customer_feedback is false:
{{
  "customer_response": "I can only help with customer feedback related topics. Could you please share your feedback about our product or service?"
}}

PROMPT 1 ANALYSIS OUTPUT (INPUT TO THIS PROMPT):
{prompt_1_json_output}
"""
    return prompt.strip()


if __name__ == "__main__":
    # Simple manual test / demo of how Prompt 1 feeds into Prompt 2
    sample_feedback = "The delivery was three days late and no one updated me. Very frustrating experience."

    prompt_1 = build_prompt_1(sample_feedback)
    print("----- PROMPT 1 -----")
    print(prompt_1)

    # In production, prompt_1 would be sent to the LLM and its JSON response
    # captured. Here we simulate that returned JSON output for demonstration.
    simulated_prompt_1_output = """
    {
      "is_customer_feedback": true,
      "sentiment": "negative",
      "confidence": 0.92,
      "topics": ["delivery", "customer service"],
      "key_points": ["late delivery", "no proactive update"],
      "summary": "Customer is frustrated about a delayed delivery with no communication."
    }
    """

    prompt_2 = build_prompt_2(simulated_prompt_1_output)
    print("\n----- PROMPT 2 -----")
    print(prompt_2)