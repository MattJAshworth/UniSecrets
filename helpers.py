import facebook
import os


def fbpost(msg):

  cfg = {
    "page_id"      : os.environ["843586662650752"],  
    "access_token" : os.environ["EAAFLj5ZAN3pcBAJ49pazCZAQS7FPwovXpYE10zoLd7l7V1ncYynq2EbfMstMBwr2geqywSedbQ15KfAvoCeuL480DTRgrXEinejCVR9PEnnqmLoQn3WXIVp2Ane33KGKZCcc0CpKfJZBXZBZBbmSMsZCO0gy4XRNN9hbFistww71dKVVZB6SZAJWiDoraZBUko4O6ZCf68dWd5XacbOZB6y19Y9x"]
    }

  api = get_api(cfg)
  status = api.put_object(parent_object='me', connection_name='feed', message=msg)

def get_api(cfg):
  graph = facebook.GraphAPI(cfg['access_token'])
  # Get page token to post as the page. You can skip 
  # the following if you want to post as yourself. 
  resp = graph.get_object('me/accounts')
  page_access_token = None
  for page in resp['data']:
    if page['id'] == cfg['page_id']:
      page_access_token = page['access_token']
  graph = facebook.GraphAPI(page_access_token)
  return graph
  # You can also skip the above if you get a page token:
  # http://stackoverflow.com/questions/8231877/facebook-access-token-for-pages
  # and make that long-lived token as in Step 3