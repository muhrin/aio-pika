import logging

from . import BaseTestCase

log = logging.getLogger(__name__)


class TestCase(BaseTestCase):
    async def test_declare_queue(self):
        connection = await self.create_connection()

        channel = await connection.channel()

        # Declaring queue
        await channel.declare_queue(
            'task_queue',
            exclusive=True,
            arguments={'x-message-ttl': 60000}
        )
