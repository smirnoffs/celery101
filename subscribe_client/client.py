from faker import Faker
import time
import asyncio
import aiohttp

fake = Faker(locale="de")


async def subscribe(name, email):
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "http://localhost:8000/subscribe", json={"name": name, "email": email}
        ) as resp:
            print(await resp.text())


async def subscribe_n_clients(n: int):
    start = time.time()
    for i in range(n):
        email = fake.email()
        name = fake.name()
        await subscribe(email, name)
    end = time.time()
    print(f"Average time: {(end - start)/n:.2} seconds per request.")


if __name__ == "__main__":
    asyncio.run(subscribe_n_clients(2))