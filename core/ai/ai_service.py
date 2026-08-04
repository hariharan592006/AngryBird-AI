import requests

from core.personality.system_prompt import SYSTEM_PROMPT

from core.memory.conversation import ConversationMemory
from core.memory.memory_manager import MemoryManager
from core.memory.memory_extractor import MemoryExtractor
from core.memory.memory_search import MemorySearch
from core.memory.memory_response import MemoryResponse

from core.brain.prompt_builder import PromptBuilder
from core.brain.router import AIRouter

from core.context.context_engine import ContextEngine
from core.command_interpreter.command_interpreter import CommandInterpreter


class AIService:

    def __init__(self):

        self.url = "http://localhost:11434/api/generate"
        self.model = "qwen3:1.7b"

        # Conversation Memory
        self.memory = ConversationMemory(max_messages=10)

        # Long-Term Memory
        self.memory_manager = MemoryManager()

        # Memory Components
        self.memory_search = MemorySearch(self.memory_manager)
        self.memory_extractor = MemoryExtractor()
        self.memory_response = MemoryResponse()

        # Brain Components
        self.prompt_builder = PromptBuilder()
        self.context_engine = ContextEngine(self.memory_manager)
        self.router = AIRouter()

        # Command Engine
        self.command_interpreter = CommandInterpreter()

    def ask(self, prompt: str):

        # -----------------------------
        # Save User Message
        # -----------------------------
        self.memory.add_user_message(prompt)

        # -----------------------------
        # Decide Request Type
        # -----------------------------
        route = self.router.route(prompt)

        # =====================================================
        # MEMORY REQUEST
        # =====================================================
        if route == "MEMORY":

            key, value = self.memory_search.search(prompt)

            if key:
                reply = self.memory_response.generate(prompt, key, value)
            else:
                reply = "Sorry, I don't remember that."

            self.memory.add_ai_message(reply)

            return reply

        # =====================================================
        # COMMAND REQUEST
        # =====================================================
        elif route == "COMMAND":

            reply = self.command_interpreter.execute(prompt)

            self.memory.add_ai_message(reply)

            return reply

        # =====================================================
        # TOOL REQUEST
        # =====================================================
        elif route == "TOOL":

            reply = "Tool execution is not implemented yet."

            self.memory.add_ai_message(reply)

            return reply

        # =====================================================
        # NORMAL AI CHAT
        # =====================================================

        # Learn new memories
        facts = self.memory_extractor.extract(prompt)

        for key, value in facts.items():
            self.memory_manager.remember(key, value)

        # Build Context
        context = self.context_engine.build_context()

        # Conversation History
        conversation = self.memory.get_context()

        # Build Prompt
        full_prompt = self.prompt_builder.build(
            SYSTEM_PROMPT,
            context,
            conversation
        )

        payload = {
            "model": self.model,
            "prompt": full_prompt,
            "stream": False,
        }

        try:

            response = requests.post(
                self.url,
                json=payload,
                timeout=300,
            )

            response.raise_for_status()

            reply = response.json()["response"].strip()

            self.memory.add_ai_message(reply)

            return reply

        except Exception as e:

            return f"AI Error: {e}"