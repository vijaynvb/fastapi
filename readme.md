Fast API Examples

## commands to run the application 

```bash
$ cd 01_basic
$ pip install -r requirements.txt 
$ uvicorn app:app --reload
```

## Recap:

  microservice 6 principles
  rest principle 

  web solutions -> [web site, web app, web service]
  browser [fea] -> uvicorn/tomcat/ iis server
  client        -> server [port no]
  process       -> process
  make request  -> listen to the request and provide response 


  url where to make request [http://ip:port/pathtoresource/resource]
  
  http protocol [set of rules]
  request message [5 verb, uri, httpversion, req header, body]
  response message [4 status code, http version, headers, body] 
  
  api -> 
    c - api -> function
    http api -> rest api -> endpoint CRUD
    mongodb -> api -> methods db.find(), db.insert(), db.update(), db.delete()


healthRoute
  1. /health {"health": "ok"}
  2. /metrics/mem {"memory": "value"}
  3. /metrics/cpu {"cpu": "value"}
