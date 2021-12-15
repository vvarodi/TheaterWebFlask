mysql -h mysql -u 22_appweb_31 -D 22_appweb_31b -p"9JoOBTaL"



python
from theater import db, create_app
db.create_all(app=create_app())


database
SHOW TABLES;
DESCRIBE user;
DESCRIBE message;


python
from theater import db, create_app, model
app = create_app()
app.app_context().push()
import datetime
import dateutil
user = model.User(email="mary@example.com", name="Mary", password="pwd")
message = model.Message(user=user, text="First message", timestamp=datetime.datetime.now(dateutil.tz.tzlocal()))
message2 = model.Message(user=user, text="Response message", timestamp=datetime.datetime.now(dateutil.tz.tzlocal()), response_to=message)
message3 = model.Message(user=user, text="Response message 2", timestamp=datetime.datetime.now(dateutil.tz.tzlocal()), response_to=message)
db.session.add(message2)
db.session.add(message3)
db.session.commit()

from theater import db, create_app, model
app = create_app()
app.app_context().push()
messages = model.Message.query.all()
messages[0].text
messages[1].text
messages[1].response_to.text
messages[0].user.email
len(messages[0].responses)
messages[0].responses[0].text



# -- from theater import db, create_app, model
# -- app = create_app()
# -- app.app_context().push()
# -- import datetime
# -- import dateutil
# -- user = model.User(email="mary@example.com", name="Mary", password="Mary")
# -- message = model.Message(user=user, text="First message", timestamp=datetime.datetime.now(dateutil.tz.tzlocal()))
# -- message2 = model.Message(user=user, text="Response message", timestamp=datetime.datetime.now(dateutil.tz.tzlocal()), response_to=message)
# -- message3 = model.Message(user=user, text="Response message 2", timestamp=datetime.datetime.now(dateutil.tz.tzlocal()), response_to=message)
# -- db.session.add(message2)
# -- db.session.add(message3)
# -- db.session.commit()

