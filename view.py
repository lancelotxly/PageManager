# -*- coding: utf-8 -*-
__author__ = 'xzq'

# 自定定义分页器组件
from blog.page_manager import PageManager
def pages(req):
    per_counts = 9
    total_counts = len(USER_LIST)
    current_info  = req.GET.get('p',None)
    display_pages = 5
    p = PageManager(total_counts,current_info,per_counts,display_pages)
    total_pages = p.total_pages
    current_page = p.current_page
    prev_page = p.prev_page
    next_page = p.next_page
    front_page = p.front_page
    tail_page = p.tail_page
    pages_list = p.pages_list()
    start_item, end_item = p.index()
    context = {'user_list': USER_LIST[start_item:end_item + 1],
               'prev_page': prev_page,
               'next_page': next_page,
               'pages_list': pages_list,
               'current_page': current_page,
               'front_page': front_page,
               'tail_page': tail_page
               }
    return render(req, 'pages.html', context)