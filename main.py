
import asyncio
import websockets
import platform
import json

async def hello():
	uri = 'ws://localhost:8000/ws/'

	uname = platform.uname()

	system_info = [
		f"System: {uname.system}",
		f"Node Name: {uname.node}",
		f"Release: {uname.release}",
		f"Version: {uname.version}",
		f"Machine: {uname.machine}",
		f"Processor: {uname.processor}"
	]

	async with websockets.connect(uri) as websocket:

		await websocket.send(json.dumps(system_info))
		print('\n' + ("="*50))
		print("System Info")
		for item in system_info:
			print(f"< {item}")

		greeting = await websocket.recv()
		print(f"\nReply\n< {greeting}")


asyncio.get_event_loop().run_until_complete(hello())