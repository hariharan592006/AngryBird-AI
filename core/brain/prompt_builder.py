class PromptBuilder:

    def build(
        self,
        system_prompt,
        context,
        conversation
    ):

        return f"""
{system_prompt}

=========================
KNOWN USER INFORMATION
=========================

{context}

=========================
RECENT CONVERSATION
=========================

{conversation}

=========================
RULES
=========================

- You are Angry Bird.
- Never reveal your AI model.
- Use memories naturally.
- Keep replies concise.
- Learn new user facts.
- Stay in character.

Respond only as Angry Bird.

Angry Bird:
"""