from .. import loader
from asyncio import sleep
@loader.tds
class SabiMod(loader.Module):
	strings = {"name": "sabi"}
	@loader.owner
	async def sabicmd(self, message):
		for _ in range(3):
			for dodik in ['я', '️люблю', 'Саби']:
				await message.edit(sabi)
				await sleep(0.7)