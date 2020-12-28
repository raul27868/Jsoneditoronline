import json
import datetime
import requests

class Jsoneditoronline:
  def __init__(self, id=None ): 
    self.title = None
    self.data = None
    self.id = id
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
    if self.id:
      response = self._get( self.id)
      self.title = json.loads(response.content)['name']
      self.data = json.loads(response.content)['data']


  #Get all data for id
  ###########################################
  def _get(self, id):
    response = requests.get('https://jsoneditoronline.herokuapp.com/v1/docs/'   +    id, headers=self.headers )
    return response


  #New document
  ###########################################
  #Example:
  # Js = Jsoneditoronline()
  # Js.new(name="COMENTARIOS", [1670758] )
  #Return: id
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
  #Example:
  # Js = Jsoneditoronline()
  # Js.update(data=[999,3, {'pp':1}])
  def update(self, id="", data={}):
    js = json.dumps(data).replace('"', '\\"')
    data = '{"name":"'+self.title + '", "updated":"'+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]+"Z"+'","_id":"'+self.id+'","data":"'+js+'"}'
    
    response = requests.put('https://jsoneditoronline.herokuapp.com/v1/docs/' +self.id, headers=self.headers, data=data)
    if json.loads(response.content)['ok'] == True:
      self.data = data
     
    return json.loads(response.content)


  #Select document
  ###########################################
  #Example:
  # Js = Jsoneditoronline()
  # Js.select(id="b92c59768fa0449781a456f2e26497d3")
  def select(self  ):
    response = self._get( self.id)
    return json.loads(response.content)['data']
