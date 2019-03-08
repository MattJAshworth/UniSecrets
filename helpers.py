import facebook
import os


# Constants
app_id = '377531436400407'
app_key = '50f56416e1297dfd609b3a7b2ef1ef90'
access_token = 'EAAFXXOMofxcBAIcctnErMVmOTZB2riOf1fDy6rrXUPYZBnPeujHHDP5rpK5xz5FG3vEiQcxTZBKNYAiIaafrDsrPBmAYnl4SYVYZAJN7te1ATLpuZBjVXTUkPeFwV2tLQb7juZBGxdMwXxfM6WJeVBIIDZA48ZAkBAHyUyZCyjZAg5CwZDZD'


def fbpost(msg, img):


  # Post to Facebook
  try:
    graph = facebook.GraphAPI(access_token)
    #graph.put_wall_post(message=random_quote())
    #graph.put_photo(image=open(img, 'rb'),message=msg, profile_id='843586662650752')
    graph.put_object(parent_object='me', connection_name='feed', message=msg)
  except Exception as e:
    print(e)
    pass