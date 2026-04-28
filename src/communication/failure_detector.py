# very simple failure detector (ping)
import aiohttp, asyncio
from ..utils.config import PEER_NODES

async def ping_node(url, timeout=1):
    try:
        # Gunakan aiohttp.ClientTimeout sesuai aturan terbaru library
        client_timeout = aiohttp.ClientTimeout(total=timeout)
        
        async with aiohttp.ClientSession() as sess:
            # Masukkan client_timeout yang sudah dibungkus
            async with sess.get(url + '/health', timeout=client_timeout) as r:
                return r.status == 200
    except Exception:
        return False

async def check_all():
    results = {}
    for n in PEER_NODES:
        results[n] = await ping_node(n)
    return results