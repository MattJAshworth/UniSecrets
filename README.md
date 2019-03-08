# Uni Secrets - An Automated Facebook Confession Page Tech Demo

A simple flask based app which helps in posting to FB pages automatically. It can be used to post directly to FB pages without any use of middle man.

### Initial Concept
1. Code & Design the Facebook confession page site
2. Using the Facebook Pages API, Flask web framework and Gunicorn http server to allow automatic posting of images and text to a Facebook page
3. Moderation was hoped to be achived by setting all page posts to be reviewed before published
> Complications with this approach have arisen. Firstly Facebook API tokens are now given on a request review basis. Secondly moderation cannot be achieved as hoped as posts made by the app will be using authenticated tokens from the admin which are published immediately. Only posts from page visitors are succeptable to be moderated. Tl;dr the inital concept will run without post moderation.

### Revised Approach
1. Reuse code and design from inital concept
2. Implement some sort of backend holding database where admins and moderators can approve or deny of posts.
3. Posts that are approved should be posted via the Facebook Pages API straight to the Facebook Page and then deleted
3. Posts that are denied should be immediately deleted

### Deployment
The current iteration is deployed on Heroku - https://unisecrets.herokuapp.com

> For local deployment -
> For deploying on Heroku -

### Working Demo

Uni Secrets posting annonymously : - https://unisecrets.herokuapp.com
Uni Secrets Facebook Page : - 

### Credits
