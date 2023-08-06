from dataclasses import dataclass
from aio_pika import ExchangeType
from aio_pika.abc import AbstractIncomingMessage
from typing import Callable, Any


MessageHandler = Callable[[AbstractIncomingMessage], Any]


@dataclass
class ConsumeConfiguration:
    exchange: str
    exchange_type: ExchangeType.DIRECT
    queue: str
    routing_key: str


@dataclass
class PublishConfiguration:
    exchange: str
    exchange_type: str
    routing_key: str


@dataclass
class BrokerConfiguration:
    url: str
    max_connections: int


@dataclass
class ExchangeConfiguration:
    name: str
    type: ExchangeType


__all__ = [ExchangeType.__name__]
