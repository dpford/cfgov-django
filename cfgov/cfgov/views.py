from django.shortcuts import render
from django.http import Http404
from elasticsearch import TransportError

from sheerlike.query import get_document


def sheerlike_get_object_or_404(doctype, docid):
    try:
        document = get_document(doctype=doctype, docid=docid)
    except TransportError:
        raise Http404('{} with id {} does not exist'.format(doctype, docid))
    return document


def office(request, office_id):
    context = {}
    office = sheerlike_get_object_or_404('office', office_id)
    if office.related_contact:
        contact = sheerlike_get_object_or_404('contact', office.related_contact)
        context['contact'] = contact
    sub_pages = [sheerlike_get_object_or_404('sub_page', subpage_slug) for subpage_slug in office.related_sub_pages]
    context['office'] = office
    context['sub_pages'] = sub_pages
    return render(request, 'offices/_single.html', context)


def subpage(request, office_id, subpage_id):
    context = {}
    sub_page = sheerlike_get_object_or_404('sub_page', subpage_id)
    office = sheerlike_get_object_or_404('office', office_id)
    # TODO - make this a query instead of a series of gets
    sub_pages = [sheerlike_get_object_or_404('sub_page', subpage_slug) for subpage_slug in office.related_sub_pages]
    if office.related_contact:
        contact = sheerlike_get_object_or_404('contact', office.related_contact)
        context['contact'] = contact
    if subpage_id not in office.related_sub_pages:
        raise Http404('Sub page is not related to office')
    context['sub_page'] = sub_page
    context['office'] = office
    context['sub_pages'] = sub_pages
    return render(request, 'sub-pages/_single.html', context)
