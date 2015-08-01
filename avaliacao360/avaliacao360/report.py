# -*- coding: utf-8 -*-
from django import http
from django.template.loader import get_template
from django.template import Context
import ho.pisa as pisa
import cStringIO as StringIO
import cgi, os
 
 
def fetch_resources(uri, rel):
    path = 'static/images'
    return path
 
def write_to_pdf(template_src, context_dict, filename):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result, link_callback=fetch_resources)
    if not pdf.err:
        response = http.HttpResponse(mimetype='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=%s.pdf' % filename
        response.write(result.getvalue())
        return response
    return http.HttpResponse('Problema ao gerar PDF: %s' % cgi.escape(html))