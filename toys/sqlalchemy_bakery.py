"""
Just for Python 3
"""

import logging
import pprint

import tornado.web
import tornado.httpserver
from tornado.options import define, options, parse_command_line
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext import baked
from sqlalchemy.orm import Session


# models

BAKERY = baked.bakery()


Base = declarative_base()


ENGINE = create_engine('sqlite:///:memory:', echo=False)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
       return "<User(name='%s', fullname='%s', password='%s')>" % (
                            self.name, self.fullname, self.password)


# request

class MainHandler(tornado.web.RequestHandler):
    @property
    def session(self):
        return Session(bind=ENGINE)

    def get(self):
        uid = self.get_argument("uid")
        def fn(session):
            logging.warn("call fn %s", fn)
            return session.query(User).filter(User.id == uid)

        baked_query = BAKERY(fn)

        logging.info("fn %s", fn.__code__)
        logging.warn("baked_query _cache_key: %s", baked_query._cache_key)

        user_list = baked_query(self.session).all()

        self.write("user_list:\n{}\n".format(pprint.pformat(user_list)))


def main():
    Base.metadata.create_all(ENGINE)

    # add test user
    session = Session(bind=ENGINE)
    for uid in range(20):
        user = User(name='ed {}'.format(uid), fullname='Ed Jones {}'.format(uid), password='edspassword')
        session.add(user)
    session.commit()

    # start application
    application = tornado.web.Application([
        (r"/", MainHandler),
    ], )
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()



if __name__ == "__main__":
    define("port", default=8888, help="run on the given port", type=int)
    parse_command_line()
    main()
