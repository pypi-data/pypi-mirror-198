from __future__ import annotations
import aio_pika
from aio_pika import Message
from aio_pika.abc import AbstractRobustConnection, AbstractRobustChannel,\
    AbstractRobustExchange, AbstractQueue, AbstractIncomingMessage, ExchangeType
from .dto import BrokerConfiguration, ExchangeConfiguration,\
    MessageHandler, ConsumeConfiguration, PublishConfiguration
from typing import List, Dict


class ChannelWrapper:

    def __init__(self, channel: AbstractRobustChannel):
        self.channel = channel
        self.exchanges: Dict[str, AbstractRobustExchange] = {}


class ChannelPool:

    def __init__(
            self,
            connection: AbstractRobustConnection,
            max_channels: int
    ):
        self.max_channels = max_channels
        self.connection = connection
        self.channels: List[ChannelWrapper] = []
        self.index = 0

    async def get_channel(self) -> ChannelWrapper:
        while len(self.channels) < self.max_channels:
            channel = await self.connection.channel()
            self.channels.append(ChannelWrapper(channel))

        channel = self.channels[self.index]
        self.index = (self.index + 1) % self.max_channels

        return channel


class BrokerConnection:

    def __init__(
            self,
            connection: AbstractRobustConnection,
            max_channels: int
    ):
        self.connection: AbstractRobustConnection = connection
        self.channels: ChannelPool = ChannelPool(connection, max_channels)
        self.exchanges: List[AbstractRobustExchange] = []

    @staticmethod
    async def new(config: BrokerConfiguration) -> BrokerConnection:
        """
        Create new message broker connection
        """
        connection = await aio_pika.connect_robust(config.url)
        return BrokerConnection(connection, config.max_connections)

    async def get_queue(
            self,
            exchange_name: str,
            exchange_type: ExchangeType,
            queue_name: str,
            routing_key: str
    ):
        '''
        Get queue, bound to an specified exchange
        '''
        channel: ChannelWrapper = await self.channels.get_channel()
        exchange = await self.get_exchange(exchange_name, exchange_type)
        queue = await channel.channel.declare_queue(queue_name)
        await queue.bind(exchange, routing_key)

        return queue

    async def get_exchange(
            self,
            exchange_name: str,
            exchange_type: ExchangeType
    ) -> AbstractRobustExchange:
        '''
        Get cached exchange or declare new
        '''
        channel = await self.channels.get_channel()
        try:
            return channel.exchanges[exchange_name]
        except KeyError:
            exchange: AbstractRobustExchange = await channel.channel\
                .declare_exchange(
                    exchange_name,
                    exchange_type
                )
            channel.exchanges[exchange_name] = exchange
            return exchange

    async def subscribe(
        self,
        config: ConsumeConfiguration,
        handler: MessageHandler
    ):
        """
        Subscribe for an event
        """
        queue: AbstractQueue = await self.get_queue(
            exchange_name=config.exchange,
            exchange_type=config.exchange_type,
            queue_name=config.queue,
            routing_key=config.routing_key
        )

        async with queue.iterator() as messages:
            async for message in messages:
                await handler(message)

    async def publish(
        self,
        config: PublishConfiguration,
        message: str | bytes
    ):
        """
        Publish an event
        """
        exchange = await self.get_exchange(
            exchange_name=config.exchange,
            exchange_type=config.exchange_type
        )
        await publish(exchange, config.routing_key, message)

    def close(self):
        for channel in self.channels.channels:
            channel.channel.close()

        self.connection.close()


async def publish(
    exchange: AbstractRobustExchange,
    routing_key: str,
    message: str | bytes
):
    """
    Publish an event to existing exchange
    """
    message = Message(message.encode())

    await exchange.publish(
        message=message,
        routing_key=routing_key
    )

__all__ = [publish.__name__, BrokerConnection.__name__]
