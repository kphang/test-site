#from anyio import create_task_group, run
import anyio
import time
import logging
import httpx
import pandas as pd

def load_file(filepath:str) -> pd.DataFrame:

    # determine filetype (csv/excel/json) and set read type based on filetype
    
    df = pd.read_csv(filepath)
    
    # determine the url col
    
    return df


async def send_request(client, method, url):
    
    if method == "GET":            
        response = await client.get(url)
    
    return response

async def build_requests(client, n):
    urls = ["http://127.0.0.1:9000/limited"]*n
    async with anyio.create_task_group() as tg:        
            for url in urls:
                
                tg.start_soon(send_request,client,"GET",url)
    
async def main(n):#urls):
    start_time=time.time()
    # TODO: adjust timeouts, retries, exception handling
    async with httpx.AsyncClient(http2=True) as client:
        await build_requests(client,n)
    print("--- %s seconds ---" % (time.time() - start_time))
     
        
def run_sync_requests():
    start_time=time.time()
    urls = ["http://127.0.0.1:9000/limited"]*100
    
    responses = []
    with httpx.Client(http2=True) as client:        
        for url in urls:
            responses.append(client.get(url))            
    print("--- %s seconds ---" % (time.time() - start_time))   

    return responses

# pull response.txt 

#anyio.run(main)        
#run_sync_requests()

# async def main():
#     urls = ["http://127.0.0.1:9000/limited"]*1000
#     responses = await run_requests()#"GET",urls)
#     responses = responses.results
#     return responses


# if __name__=="__main__":
#     start_time=time.time()
#     # TODO: implement test?
#     #urls = ["http://127.0.0.1:9000/limited"]*1000    
#     #anyio.run(main())
#     anyio.run(run_requests())#, urls)
#     #test = run_sync_requests(urls)
#     #print(len(test))
#     print("--- %s seconds ---" % (time.time() - start_time))
    
#asyncio.run(run_requests())#, urls)