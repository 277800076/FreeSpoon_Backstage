#!/usr/bin/env python
# coding: utf-8

import django

if django.VERSION >= (1, 10):
    from django.urls import reverse_lazy
else:
    from django.core.urlresolvers import reverse_lazy

from table.columns import Column
from table.columns.calendarcolumn import CalendarColumn
from table.columns.sequencecolumn import SequenceColumn
from table.columns.imagecolumn import ImageColumn
from table.columns.linkcolumn import LinkColumn, Link, ImageLink
from table.columns.checkboxcolumn import CheckboxColumn

from table import Table
from .models import *


class AjaxSourceTable(Table):
#    id = Column(field='id', header=u'#')
#    name = Column(field='name', header=u'NAME')
#
#    class Meta:
#        model = Person
#        ajax = True
#        ajax_source = reverse_lazy('ajax_source_api')

    id = Column(field = 'id')
#,header = u'团购编号')
#    title = Column(field = 'title')
##,header = u'团购昵称')
#    reseller_mob = Column(field = 'reseller_mob')
##,header = u'团主手机号')
#    receive_mode = Column(field = 'receive_mode')
##,header = u'团购类型')
#    start_time = Column(field = 'start_time')
##,header = u'开始时间')
#    dead_time = Column(field = 'dead_time')
##,header = u'结束时间')
#    status = Column(field = 'status')
##,header = u'团购状态')
#    volume = Column(field = 'volume')
##,header = u'销量')
#    details = Column(field = 'details')
#,header = u'详情')
    class Meta:
        model = Bulk
        ajax = True
        ajax_source = reverse_lazy('ajax_source_api')

