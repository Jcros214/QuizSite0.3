The db models seem to be incorrectly configured. I'm getting the following error when I try to run the app:
```
127.0.0.1 - - [31/Dec/2022 01:41:06] "POST /login HTTP/1.1" 500 -
Error on request:
Traceback (most recent call last):
  File "/Users/jon/Documents/DEV/pythonanywhere/site/QuizSite/auth/lib/python3.10/site-packages/werkzeug/serving.py", line 335, in run_wsgi
    execute(self.server.app)
  File "/Users/jon/Documents/DEV/pythonanywhere/site/QuizSite/auth/lib/python3.10/site-packages/werkzeug/serving.py", line 322, in execute
    application_iter = app(environ, start_response)
  File "/Users/jon/Documents/DEV/pythonanywhere/site/QuizSite/auth/lib/python3.10/site-packages/flask/app.py", line 2548, in __call__
    return self.wsgi_app(environ, start_response)
  File "/Users/jon/Documents/DEV/pythonanywhere/site/QuizSite/auth/lib/python3.10/site-packages/flask/app.py", line 2528, in wsgi_app
    response = self.handle_exception(e)
  File "/Users/jon/Documents/DEV/pythonanywhere/site/QuizSite/auth/lib/python3.10/site-packages/flask/app.py", line 2525, in wsgi_app
    response = self.full_dispatch_request()
  File "/Users/jon/Documents/DEV/pythonanywhere/site/QuizSite/auth/lib/python3.10/site-packages/flask/app.py", line 1822, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/Users/jon/Documents/DEV/pythonanywhere/site/QuizSite/auth/lib/python3.10/site-packages/flask/app.py", line 1820, in full_dispatch_request
    rv = self.dispatch_request()
  File "/Users/jon/Documents/DEV/pythonanywhere/site/QuizSite/auth/lib/python3.10/site-packages/flask/app.py", line 1796, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)
  File "/Users/jon/Documents/DEV/pythonanywhere/site/QuizSite/project/auth.py", line 141, in login
    user = User.query.filter_by(username=username).first()
  File "/Users/jon/Documents/DEV/pythonanywhere/site/QuizSite/auth/lib/python3.10/site-packages/flask_sqlalchemy/__init__.py", line 550, in __get__
    mapper = orm.class_mapper(type)
  File "/Users/jon/Documents/DEV/pythonanywhere/site/QuizSite/auth/lib/python3.10/site-packages/sqlalchemy/orm/base.py", line 442, in class_mapper
    mapper = _inspect_mapped_class(class_, configure=configure)
  File "/Users/jon/Documents/DEV/pythonanywhere/site/QuizSite/auth/lib/python3.10/site-packages/sqlalchemy/orm/base.py", line 421, in _inspect_mapped_class
    mapper._check_configure()
  File "/Users/jon/Documents/DEV/pythonanywhere/site/QuizSite/auth/lib/python3.10/site-packages/sqlalchemy/orm/mapper.py", line 1924, in _check_configure
    _configure_registries({self.registry}, cascade=True)
  File "/Users/jon/Documents/DEV/pythonanywhere/site/QuizSite/auth/lib/python3.10/site-packages/sqlalchemy/orm/mapper.py", line 3483, in _configure_registries
    _do_configure_registries(registries, cascade)
  File "/Users/jon/Documents/DEV/pythonanywhere/site/QuizSite/auth/lib/python3.10/site-packages/sqlalchemy/orm/mapper.py", line 3522, in _do_configure_registries
    mapper._post_configure_properties()
  File "/Users/jon/Documents/DEV/pythonanywhere/site/QuizSite/auth/lib/python3.10/site-packages/sqlalchemy/orm/mapper.py", line 1941, in _post_configure_properties
    prop.init()
  File "/Users/jon/Documents/DEV/pythonanywhere/site/QuizSite/auth/lib/python3.10/site-packages/sqlalchemy/orm/interfaces.py", line 231, in init
    self.do_init()
  File "/Users/jon/Documents/DEV/pythonanywhere/site/QuizSite/auth/lib/python3.10/site-packages/sqlalchemy/orm/relationships.py", line 2150, in do_init
    self._generate_backref()
  File "/Users/jon/Documents/DEV/pythonanywhere/site/QuizSite/auth/lib/python3.10/site-packages/sqlalchemy/orm/relationships.py", line 2430, in _generate_backref
    raise sa_exc.ArgumentError(
sqlalchemy.exc.ArgumentError: Error creating backref 'season' on relationship 'Season.events': property of that name exists on mapper 'mapped class Event->event'
```