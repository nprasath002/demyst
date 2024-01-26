### Setup instructions
- Checkout this repo from github
- To run cli `python3 main.py`
- To run tests `python3 test.py`

### System extensibility & Scalability
- The API allows to [filter results](https://jsonplaceholder.typicode.com/guide/) by id
- Since the required data is first 20 even numbers the most performant way is to make a single call with ids as filter
- If we want to scale this to get first 2 million even numbers we need to 
  - Only get n number of entries at a time (Depends on server environment)
  - Send multiple API requests simultanously
  - Combine the results and print output