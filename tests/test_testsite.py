import pytest
#from fastapi.testclient import TestClient
from httpx import AsyncClient

from testsite.app import testsite
#client = TestClient(testsite)

#@pytest.mark.anyio
@pytest.fixture(scope="module")
async def test_root():
    async with AsyncClient(app=testsite, base_url="http://192.168.0.1:9000", http2=True) as client:
        response = await client.get("/")
    assert response.status_code == 400
