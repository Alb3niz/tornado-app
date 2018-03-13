"""Main web handlers, from tornado web handler"""

import logging
import psycopg2
# import json
# import jinja2 as jinja

import tornado.web
# from tornado import gen

LOGGER = logging.getLogger(__name__)

class BaseHandler(tornado.web.RequestHandler):
    """
        Class to collect all common handler methods.
        Extend all other handlers from this one
    """

    def initialize(self, **kwargs):
        """Start database"""
        super(BaseHandler, self).initialize(**kwargs)
        # self.db = self.settings['db']
        self.db = psycopg2.connect("dbname=twitter_app_db user=postgres password=mysecretpassword host=localhost port=32768").cursor()
        self.current_user_object = None
        self.template_name = None

        # def render(self, template, context=None):
    #     """Renders template using jinja2"""
    #     if not context:
    #         context = {}
    #     context.update(self.get_template_namespace())
    #     self.write(jinja)
