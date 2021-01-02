
'''
import asyncio
import websockets
import platform
import json

async def hello():
	uri = 'ws://localhost:8000/ws/hub/'

	uname = platform.uname()

	system_info = [
		f"System: {uname.system}",
		f"Node Name: {uname.node.split('.', 1)[0]}",
		f"Release: {uname.release}",
		f"Version: {uname.version}",
		f"Machine: {uname.machine}",
		f"Processor: {uname.processor}"
	]

	data = {
		'system_info': system_info,
		'token': 'AYYYY its a node'
	}

	async with websockets.connect(uri) as websocket:

		await websocket.send(json.dumps(data))
		print('\n' + ("="*50))
		print("System Info")
		for item in system_info:
			print(f"< {item}")

		greeting = await websocket.recv()
		print(f"\nReply\n< {greeting}")


asyncio.get_event_loop().run_until_complete(hello())
'''

import json
import requests


request = requests.get('http://127.0.0.1:8000/eoh/initnode/', auth=('user', 'pass'))

print(request.json())