from pyramid.view import view_config
from pyramid.response import Response
from sqlalchemy.exc import SQLAlchemyError

from .. import models


@view_config(route_name='home', renderer='shopper:templates/mytemplate.jinja2')
def my_view(request):
    pass

