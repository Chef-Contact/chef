import asyncio
import websockets

# Список подключенных клиентов
clients = set()

async def server(websocket, path):
    # Добавляем нового клиента в список
    clients.add(websocket)
    try:
        # Бесконечный цикл получения сообщений от клиента
        async for message in websocket:
            # Рассылаем сообщение всем подключенным клиентам
            for client in clients:
                await client.send(message)
    finally:
        # Удаляем клиента из списка при разрыве соединения
        clients.remove(websocket)

# Запускаем сервер на порту 8765
start_server = websockets.serve(server, "0.0.0.0", 12345)

# Запускаем сервер в бесконечном цикле
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()