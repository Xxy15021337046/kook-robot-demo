import settings, logging, re
from khl import Bot, Message
from function import chat
from khl.command import Rule

bot = Bot(token=settings.token)


@bot.command(rules=[Rule.is_bot_mentioned(bot)], regex=r'(.+)')
async def receive(msg: Message, mention_str: str):
    message = re.sub('\s*\(met\).*?\(met\)\s*', '', msg.content)
    res = ""
    if not message.strip():
        res = await chat.chatgpt("自我介绍")
    elif re.search(f'{settings.wildcard_character}help',message.lower()):
        res = settings.kook_rob_help
    else:
        res = await chat.chatgpt(message)
    await msg.reply(res)


if __name__ == '__main__':
    logging.basicConfig(level='INFO')
    bot.run()
