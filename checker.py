#imports
import httpx

#headers list temporary
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0"
}
async def check(address):
    async with httpx.AsyncClient(headers=headers, follow_redirects=True) as client:
        try:
            response = await client.get(address, timeout=10)
            return response.status_code

        except httpx.TimeoutException:
            return "timeout"
        except httpx.RequestError as e:
            return f"error: {e}"
