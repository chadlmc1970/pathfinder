from anthropic import Anthropic
from typing import List, Dict
from app.core.config import settings

client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)


def generate_career_recommendations(
    user_interest_dna: Dict,
    available_careers: List[Dict],
    top_n: int = 5
) -> List[Dict]:
    """
    Generate personalized career recommendations using Claude 4.6.

    Args:
        user_interest_dna: User's Interest DNA profile
        available_careers: List of career profiles to rank
        top_n: Number of recommendations to return

    Returns:
        List of career recommendations with scores and reasoning
    """

    # Build prompt for Claude
    prompt = f"""You are a career counselor helping 8th grade students in Louisiana discover careers that match their interests.

User's Interest DNA:
{user_interest_dna}

Available Careers (showing {len(available_careers)} options):
{[{
    'title': c['title'],
    'industry': c['industry'],
    'description': c['description'][:200],
    'skills': c.get('skills', {})
} for c in available_careers]}

Task:
1. Analyze the user's Interest DNA to understand their preferences
2. Match each career against their interests
3. Return the top {top_n} career recommendations
4. For each recommendation, provide:
   - career_id: The career ID
   - match_score: 0-100 score indicating fit
   - reasoning: 2-3 sentences explaining why this career matches their interests

Format your response as JSON:
{{
  "recommendations": [
    {{
      "career_id": 1,
      "match_score": 95,
      "reasoning": "This career aligns with..."
    }}
  ]
}}"""

    response = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=2000,
        messages=[{
            "role": "user",
            "content": prompt
        }]
    )

    # Parse Claude's response
    import json
    result = json.loads(response.content[0].text)

    return result["recommendations"]


def update_interest_dna(
    current_dna: Dict,
    engagement_history: List[Dict]
) -> Dict:
    """
    Update user's Interest DNA based on engagement patterns.

    Args:
        current_dna: Current Interest DNA profile
        engagement_history: Recent engagement events (liked, watched, saved, skipped)

    Returns:
        Updated Interest DNA profile
    """

    prompt = f"""You are analyzing a user's career exploration behavior to update their Interest DNA profile.

Current Interest DNA:
{current_dna}

Recent Engagement History (last 20 interactions):
{engagement_history}

Task:
1. Analyze patterns in what they liked vs skipped
2. Identify emerging interests from watched/saved content
3. Update the Interest DNA to reflect their evolving preferences
4. Keep the same JSON structure but adjust values based on behavior

Format your response as JSON with the updated Interest DNA."""

    response = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1500,
        messages=[{
            "role": "user",
            "content": prompt
        }]
    )

    import json
    updated_dna = json.loads(response.content[0].text)

    return updated_dna
