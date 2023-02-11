import settings, logging
from khl import Bot, Message
from function import chat
from khl.command import Rule, CommandManager


# class MyCommandManager(CommandManager):
#
#     def __call__(self,  *args, **kwargs):
#         prefixes = ('!',),
#         super().__call__(prefixes, *args, **kwargs)
#
#
# Bot.command = MyCommandManager()

bot = Bot(token=settings.token)


@bot.command(name='hello', rules=[Rule.is_bot_mentioned(bot)], prefixes=('/', ))
async def world(msg: Message, mention_str: str):
    await msg.reply(f'world! I am mentioned with {mention_str}')

@bot.command(name='', rules=[Rule.is_bot_mentioned(bot)], regex=r'(.+)')
async def world(msg: Message, mention_str: str):
    await msg.reply(f'world! I am mentioned with {mention_str}')


if __name__ == '__main__':
    logging.basicConfig(level='INFO')
    bot.run()
