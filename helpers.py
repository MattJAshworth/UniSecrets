import facebook
import os


# Constants
app_id = '377531436400407'
app_key = '50f56416e1297dfd609b3a7b2ef1ef90'
access_token = 'EAAFXXOMofxcBAIcctnErMVmOTZB2riOf1fDy6rrXUPYZBnPeujHHDP5rpK5xz5FG3vEiQcxTZBKNYAiIaafrDsrPBmAYnl4SYVYZAJN7te1ATLpuZBjVXTUkPeFwV2tLQb7juZBGxdMwXxfM6WJeVBIIDZA48ZAkBAHyUyZCyjZAg5CwZDZD'


def fbpost(msg):

  cfg = {
    "page_id"      : os.environ["843586662650752"],  
    "access_token" : os.environ["EAAFLj5ZAN3pcBAJ49pazCZAQS7FPwovXpYE10zoLd7l7V1ncYynq2EbfMstMBwr2geqywSedbQ15KfAvoCeuL480DTRgrXEinejCVR9PEnnqmLoQn3WXIVp2Ane33KGKZCcc0CpKfJZBXZBZBbmSMsZCO0gy4XRNN9hbFistww71dKVVZB6SZAJWiDoraZBUko4O6ZCf68dWd5XacbOZB6y19Y9x"]
    }

  # Post to Facebook
try:
    graph = facebook.GraphAPI(access_token=access_token)
    #graph.put_wall_post(message=random_quote())
    graph.put_object(parent_object='843586662650752', connection_name='feed',
                  message=msg)
except Exception as e:
    print(e)
    pass