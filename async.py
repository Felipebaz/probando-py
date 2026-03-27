import asyncio
import time

async def pedir_cafe () :
    print("Pidiendo cafe...")
    await asyncio.sleep(3)
    print("Cafe listo!")
    return "Cafe"


async def main():
    inicio = time.time()
    await asyncio.gather(
        pedir_cafe(),
        pedir_cafe(),
        pedir_cafe()
    ) 
    fin = time.time()
    print(f"Tiempo total: {fin - inicio} segundos")

asyncio.run(main())
