# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe

__version__ = '1.0.0'

def before_install():
	if (frappe.session.user != "Administrator"):
		logger = frappe.logger(__name__, with_more_info=True)
		logger.error('App install from website by {}'.format(frappe.session.user))
		return False
