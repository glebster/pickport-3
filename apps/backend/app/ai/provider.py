"""Базовые типы и протокол провайдера LLM.

Держим единый контракт для разных провайдеров (OpenAI, OpenRouter, DeepSeek,
Qwen, Яндекс, Сбер). Бизнес-логика не должна знать о конкретном API.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, AsyncIterator, Optional, Protocol, runtime_checkable


@dataclass
class Message:
    role: str
    content: str


@dataclass
class ToolCall:
    name: str
    arguments: dict[str, Any]


@dataclass
class CompletionRequest:
    messages: list[Message]
    tools: Optional[list[str]] = None
    temperature: float = 0.7
    max_tokens: Optional[int] = None
    top_p: float = 1.0
    stream: bool = False
    model: Optional[str] = None


@dataclass
class Usage:
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int
    estimated: bool = False


@dataclass
class CompletionResponse:
    text: str
    tool_calls: list[ToolCall]
    usage: Usage
    finish_reason: str


@dataclass
class CompletionChunk:
    """Чанк для стриминга."""

    text: str
    tool_calls: list[ToolCall]
    finish_reason: Optional[str]
    usage: Optional[Usage] = None


@dataclass
class Pricing:
    input_per_1k: float
    output_per_1k: float
    currency: str = "usd"


class AIError(Exception):
    """Единый тип ошибок AI слоя."""


@runtime_checkable
class LLMProvider(Protocol):
    """Протокол провайдера. Реализации создаются из конфига/env."""

    name: str

    async def complete(self, request: CompletionRequest) -> CompletionResponse:
        """Нестримоая генерация."""
        ...

    async def stream(self, request: CompletionRequest) -> AsyncIterator[CompletionChunk]:
        """Стримовая генерация. Если провайдер не поддерживает — можно даунгрейдить до complete."""
        ...

    def count_tokens(self, request: CompletionRequest) -> Usage:
        """Подсчёт токенов локально или эвристикой (estimated=True)."""
        ...

    def pricing(self, model: str | None = None) -> Pricing:
        """Статическая цена модели (per 1k токенов)."""
        ...


# Заготовки для будущих реализаций.


class OpenAIProvider:
    name = "openai"

    async def complete(self, request: CompletionRequest) -> CompletionResponse:
        raise NotImplementedError

    async def stream(self, request: CompletionRequest) -> AsyncIterator[CompletionChunk]:
        raise NotImplementedError

    def count_tokens(self, request: CompletionRequest) -> Usage:
        raise NotImplementedError

    def pricing(self, model: str | None = None) -> Pricing:
        raise NotImplementedError


class OpenRouterProvider:
    name = "openrouter"

    async def complete(self, request: CompletionRequest) -> CompletionResponse:
        raise NotImplementedError

    async def stream(self, request: CompletionRequest) -> AsyncIterator[CompletionChunk]:
        raise NotImplementedError

    def count_tokens(self, request: CompletionRequest) -> Usage:
        raise NotImplementedError

    def pricing(self, model: str | None = None) -> Pricing:
        raise NotImplementedError


class DeepSeekProvider:
    name = "deepseek"

    async def complete(self, request: CompletionRequest) -> CompletionResponse:
        raise NotImplementedError

    async def stream(self, request: CompletionRequest) -> AsyncIterator[CompletionChunk]:
        raise NotImplementedError

    def count_tokens(self, request: CompletionRequest) -> Usage:
        raise NotImplementedError

    def pricing(self, model: str | None = None) -> Pricing:
        raise NotImplementedError


class QwenProvider:
    name = "qwen"

    async def complete(self, request: CompletionRequest) -> CompletionResponse:
        raise NotImplementedError

    async def stream(self, request: CompletionRequest) -> AsyncIterator[CompletionChunk]:
        raise NotImplementedError

    def count_tokens(self, request: CompletionRequest) -> Usage:
        raise NotImplementedError

    def pricing(self, model: str | None = None) -> Pricing:
        raise NotImplementedError


class YandexProvider:
    name = "yandex"

    async def complete(self, request: CompletionRequest) -> CompletionResponse:
        raise NotImplementedError

    async def stream(self, request: CompletionRequest) -> AsyncIterator[CompletionChunk]:
        raise NotImplementedError

    def count_tokens(self, request: CompletionRequest) -> Usage:
        raise NotImplementedError

    def pricing(self, model: str | None = None) -> Pricing:
        raise NotImplementedError


class SberProvider:
    name = "sber"

    async def complete(self, request: CompletionRequest) -> CompletionResponse:
        raise NotImplementedError

    async def stream(self, request: CompletionRequest) -> AsyncIterator[CompletionChunk]:
        raise NotImplementedError

    def count_tokens(self, request: CompletionRequest) -> Usage:
        raise NotImplementedError

    def pricing(self, model: str | None = None) -> Pricing:
        raise NotImplementedError

