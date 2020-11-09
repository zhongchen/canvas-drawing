import asyncio
import logging
import sys

from src.server.command import *
from src.server.canvas import Canvas

root = logging.getLogger()
root.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)


async def on_new_client(reader, writer):
    addr = writer.get_extra_info('peername')
    logging.info(f"connection established from {addr}")
    canvas = Canvas()
    # handshake msgs
    writer.write("hello\r\n".encode('utf-8'))
    await writer.drain()

    try:
        while True:
            data = await reader.readline()
            msg = data.decode("utf-8").strip()
            cmd = Cmd.parse_cmd(msg)

            if isinstance(cmd, QuitCmd):
                break

            if isinstance(cmd, StepCmd):
                canvas.step(cmd.n)

            if isinstance(cmd, ChangeDirectionCmd):
                canvas.change_direction(cmd.n)

            if isinstance(cmd, ChangeModeCmd):
                canvas.set_mode(cmd.n)

            if isinstance(cmd, ClearCmd):
                canvas.clear()

            if isinstance(cmd, CoordCmd):
                x, y = canvas.get_cursor()
                writer.write(f"({x},{y})\r\n".encode("utf-8"))
                await writer.drain()

            if isinstance(cmd, RenderCmd):
                lines = canvas.render()
                for line in lines:
                    writer.write((line + "\r\n").encode("utf-8"))
                    await writer.drain()
                writer.write("\r\n".encode('utf-8'))
                await writer.drain()

    except Exception as e:
        logging.error(e)
    finally:
        logging.info(f"close the connection from {addr}")
        writer.close()


async def main():
    port = 8124
    server = await asyncio.start_server(
        on_new_client, "localhost", port)

    logging.info(f"Sever starts. Listening on port {port}")

    async with server:
        await server.serve_forever()


asyncio.run(main())
