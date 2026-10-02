"""Thin async wrapper around OpenAI chat + per-channel history."""
from collections import defaultdict, deque
from openai import AsyncOpenAI


class AIClient:
    def __init__(self, api_key: str, model: str, system_prompt: str, max_history: int = 12):
        self.client = AsyncOpenAI(api_key=api_key)
        self.model = model
        self.system_prompt = system_prompt
        self.max_history = max_history
        self._history: dict[int, deque] = defaultdict(lambda: deque(maxlen=max_history))
        self._locks: dict[int, object] = {}
        import asyncio
        self._asyncio = asyncio

    def _lock_for(self, channel_id: int):
        if channel_id not in self._locks:
            self._locks[channel_id] = self._asyncio.Lock()
        return self._locks[channel_id]

    def reset(self, channel_id: int):
        self._history[channel_id].clear()

    async def chat(self, channel_id: int, user: str) -> str:
        lock = self._lock_for(channel_id)
        async with lock:
            self._history[channel_id].append({"role": "user", "content": user})
            messages = [{"role": "system", "content": self.system_prompt}]
            messages += list(self._history[channel_id])
            try:
                resp = await self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    temperature=0.7,
                    max_tokens=800,
                )
                text = resp.choices[0].message.content.strip()
            except Exception as e:
                return f"AI error: {e}"
            self._history[channel_id].append({"role": "assistant", "content": text})
            return text
