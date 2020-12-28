import requests
import datetime
import json

setup(
    name='Jsoneditoronline',
    version='1.0.0',
    url='https://github.com/raul27868/Jsoneditoronline.git',
    author='Raul Reyero',
    author_email='raul.reyero.diez@gmail.com',
    description='Api for https://jsoneditoronline.org',
    packages=find_packages(),    
    install_requires=['requests', 'datetime', 'json' ],
)
 


class Jsoneditoronline:
  def __init__(self ): 
    self.title = None
    self.data = None
    self.id = None
    self.headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Origin': 'https://jsoneditoronline.org',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://jsoneditoronline.org/',
        'Accept-Language': 'es-ES,es;q=0.9,und;q=0.8,en;q=0.7',
    }

  #New document
  ###########################################
  def new(self, title="", data={}):

    js = json.dumps(data).replace('"', '\\"')
    data = '{"name":"Test","schema":{"type":"NONE","url":null,"id":null,"content":null,"leftPanel":false,"rightPanel":false},"updated":"' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]+"Z" + '","data":"'+js+'"}'
    response = requests.post('https://jsoneditoronline.herokuapp.com/v1/docs', headers=self.headers, data=data)

    self.id = data
    if json.loads(response.content)['ok'] == True:
      self.title = title
      self.data = data
      self.id = json.loads(response.content)['id']

    return json.loads(response.content)


  #Update document
  ###########################################
  def update(self, id="", data={}):
    js = json.dumps(data).replace('"', '\\"')
    data = '{"name":"Test","schema":{"type":"NONE","url":null,"id":null,"content":null,"leftPanel":false,"rightPanel":false},"updated":"' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]+"Z" + '","data":"'+js+'"}'
    data = '{"name":"'+self.title + '", "updated":"'+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]+"Z"+'","_id":"'+id+'","data":"'+js+'"}'
    
    response = requests.put('https://jsoneditoronline.herokuapp.com/v1/docs/' +id, headers=self.headers, data=data)
    if json.loads(response.content)['ok'] == True:
      self.data = data
     
    return json.loads(response.content)
