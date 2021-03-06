from django.shortcuts import render, HttpResponse, redirect
from django.forms.models import model_to_dict
from webqo import models
from fanyi import models as layout
from utils import pagination
import time, json
import requests
import sys
from bs4 import BeautifulSoup
import difflib


# Create your views here.
def auth(func):
    def inner(request, *args, **kwargs):
        login_url = "https://login.sogou-inc.com/?appid=1162&sso_redirect=http://frontqa.web.sjs.ted/&targetUrl="
        try:
            user_id = request.COOKIES.get('uid')
            if not user_id:
                return redirect(login_url)
        except:
            return redirect(login_url)
        v = request.COOKIES.get('username111')
        return func(request, *args, **kwargs)

    return inner


@auth
def qo_req(request):
    # user_id = "zhangjingjun"
    user_id = request.COOKIES.get('uid')
    if request.method == 'GET':
        business_lst = layout.Business.objects.all()
        app_lst = layout.Application.objects.all()
        req_lst = models.ReqInfo_QO.objects.filter(user_fk_id=user_id)
        user_app_lst = layout.UserToApp.objects.filter(user_name_id=user_id)
        app_id_lst = list()
        for appid in user_app_lst:
            app_id_lst.append(appid.app_id_id)
        if 6 in app_id_lst:
            return render(request, 'qo_req.html',
                          {'business_lst': business_lst, 'user_id': user_id, 'user_app_lst': user_app_lst,
                           'req_lst': req_lst,
                           'app_lst': app_lst, 'businame': 'Webqo', 'app_name': "webqo请求调试"})
        else:
            return render(request, 'no_limit.html',
                          {'business_lst': business_lst, 'user_id': user_id, 'user_app_lst': user_app_lst,
                           'app_lst': app_lst, 'businame': 'Webqo', 'app_name': "webqo请求调试"})


def qo_diff(request):
    ret = {
        'status': True,
        'error': None,
        'data': None
    }
    inputHost = request.POST.get('inputHost')
    inputExpId = request.POST.get('inputExpId')
    query_from = request.POST.get('query_from')
    inputHost_diff = request.POST.get('inputHost_diff')
    inputExpId_diff = request.POST.get('inputExpId_diff')
    query_from_diff = request.POST.get('query_from_diff')
    query = request.POST.get('query')

    if inputExpId == '':
        inputExpId = 0
    else:
        inputExpId = inputExpId

    if inputExpId_diff == '':
        inputExpId_diff = 0
    else:
        inputExpId_diff = inputExpId_diff

    if query_from == '':
        query_from = 0
    else:
        query_from = query_from

    if query_from_diff == '':
        query_from_diff = 0
    else:
        query_from_diff = query_from_diff

    query_from = hex(int(query_from)).split('0x')[1] + "^0^0^0^0^0^0^0^0"
    query_from = query_from.encode('utf-16LE')

    query_from_diff = hex(int(query_from_diff)).split('0x')[1] + "^0^0^0^0^0^0^0^0"
    query_from_diff = query_from_diff.encode('utf-16LE')

    exp_id = hex(int(inputExpId)).split('0x')[1] + "^0^0^0^0^0^0^0^0"
    exp_id = exp_id.encode('utf-16LE')

    exp_id_diff = hex(int(inputExpId_diff)).split('0x')[1] + "^0^0^0^0^0^0^0^0"
    exp_id_diff = exp_id_diff.encode('utf-16LE')

    utf16_query = query.encode('utf-16LE', 'ignore')

    params = {
        'queryString': utf16_query,
        'queryFrom': query_from,
        'exp_id': exp_id
    }

    params_diff = {
        'queryString': utf16_query,
        'queryFrom': query_from_diff,
        'exp_id': exp_id_diff
    }

    headers = {"Content-type": "application/x-www-form-urlencoded;charset=UTF-16LE"}

    try:
        resp = requests.post(inputHost, data=params, headers=headers)
        resp_diff = requests.post(inputHost_diff, data=params_diff, headers=headers)
        status = resp.reason
        status_diff = resp_diff.reason
        if status != 'OK' or status_diff != 'OK':
            print(sys.stderr, query, status, status_diff)
            ret['error'] = 'Error:未知的请求类型'
            ret['status'] = False
            return ret
        data = BeautifulSoup(resp.text)
        data_diff = BeautifulSoup(resp_diff.text)
        diff = difflib.HtmlDiff()
        ret['data'] = diff.make_table(data.prettify().splitlines(), data_diff.prettify().splitlines()).replace(
            'nowrap="nowrap"', '')

    except Exception as e:
        print(e)
        print(sys.stderr, sys.exc_info()[0], sys.exc_info()[1])
        ret['error'] = "Error:" + str(e)
        ret['status'] = False
    return HttpResponse(json.dumps(ret))


def qo_req_info(request):
    ret = {
        'status': True,
        'error': None,
        'data': None
    }
    inputHost = request.POST.get('inputHost')
    inputExpId = request.POST.get('inputExpId')
    query_from = request.POST.get('query_from')
    query = request.POST.get('query')

    if inputExpId == '':
        inputExpId = 0
    else:
        inputExpId = inputExpId

    if query_from == '':
        query_from = 0
    else:
        query_from = query_from

    query_from = hex(int(query_from)).split('0x')[1] + "^0^0^0^0^0^0^0^0"
    query_from = query_from.encode('utf-16LE')

    exp_id = hex(int(inputExpId)).split('0x')[1] + "^0^0^0^0^0^0^0^0"
    exp_id = exp_id.encode('utf-16LE')

    utf16_query = query.encode('utf-16LE', 'ignore')

    params = {
        'queryString': utf16_query,
        'queryFrom': query_from,
        'exp_id': exp_id
    }

    headers = {"Content-type": "application/x-www-form-urlencoded;charset=UTF-16LE"}

    try:
        resp = requests.post(inputHost, data=params, headers=headers)
        status = resp.reason
        if status != 'OK':
            print(sys.stderr, query, status)
            ret['error'] = 'Error:未知的请求类型'
            ret['status'] = False
            return ret
        data = BeautifulSoup(resp.text)
        ret['data'] = data.prettify()

    except Exception as e:
        print(e)
        print(sys.stderr, sys.exc_info()[0], sys.exc_info()[1])
        ret['error'] = "Error:" + str(e)
        ret['status'] = False
    return HttpResponse(json.dumps(ret))


@auth
def qo_req_save(request):
    # user_id = "zhangjingjun"
    user_id = request.COOKIES.get('uid')
    ret = {
        'status': True,
        'error': None,
        'data': None
    }
    inputHost = request.POST.get('inputHost')
    inputExpId = request.POST.get('inputExpId')
    query_from = request.POST.get('query_from')
    query = request.POST.get('query')

    try:
        models.ReqInfo_QO.objects.create(host_ip=inputHost, exp_id=inputExpId, query_from=query_from, query=query,
                                         user_fk_id=user_id)

        ret['inputHost'] = inputHost
        ret['inputExpId'] = inputExpId
        ret['query_from'] = query_from
        ret['query'] = query
    except Exception as e:
        ret['error'] = "Error:" + str(e)
        print(e)
        ret['status'] = False
    return HttpResponse(json.dumps(ret))


@auth
def qo_req_del(request):
    ret = {
        'status': True,
        'error': None,
        'data': None
    }
    req_id = request.POST.get('line_id')
    try:
        models.ReqInfo_QO.objects.filter(id=req_id).delete()
    except Exception as e:
        ret['status'] = False
        ret['error'] = "Error:" + str(e)
        print(e)
    return HttpResponse(json.dumps(ret))


@auth
def qo_task_cancel(request):
    ret = {'status': True, 'errro': None, 'data': None}
    try:
        re_add_task_d = request.POST.get('task_id')
        models.webqoqps.objects.filter(id=re_add_task_d).update(status=6)
    except Exception as e:
        ret['error'] = 'error:' + str(e)
        ret['status'] = False
    return HttpResponse(json.dumps(ret))


@auth
def qo_task_readd(request):
    # user_id='gongyanli'
    user_id = request.COOKIES.get('uid')
    ret = {'status': True, 'errro': None, 'data': None}
    re_add_task_id = request.POST.get('task_id')
    try:
        task_detail = models.webqoqps.objects.get(id=re_add_task_id)
        testitem = models.webqoqps.objects.filter(id=re_add_task_id).values('testitem')

        if testitem.first()['testitem']==1:
            task_detail_todic = model_to_dict(task_detail)
            task_detail_todic.pop('id')
            task_detail_todic['create_time'] = get_now_time()
            task_detail_todic['start_time'] = ""
            task_detail_todic['end_time'] = ""
            task_detail_todic['testitem'] = 1
            task_detail_todic['status'] = 0
            task_detail_todic['errorlog'] = ""
            task_detail_todic['cost_test'] = ""
            task_detail_todic['cost_base'] = ""
            task_detail_todic['runningIP'] = ""
            task_detail_todic['user'] = user_id
            models.webqoqps.objects.create(**task_detail_todic)
        elif testitem.first()['testitem']==0:
            task_detail_todic = model_to_dict(task_detail)
            task_detail_todic.pop('id')
            task_detail_todic['create_time'] = get_now_time()
            task_detail_todic['start_time'] = ""
            task_detail_todic['end_time'] = ""
            task_detail_todic['testitem'] = 0
            task_detail_todic['status'] = 0
            task_detail_todic['errorlog'] = ""
            task_detail_todic['cost_test'] = ""
            task_detail_todic['cost_base'] = ""
            task_detail_todic['runningIP'] = ""
            task_detail_todic['user'] = user_id
            models.webqoqps.objects.create(**task_detail_todic)
    except Exception as e:
        print(e)
        ret['error'] = 'error:' + str(e)
        ret['status'] = False
    return HttpResponse(json.dumps(ret))


@auth
def qo_task_detail(request, task_id):
    # user_id="zhangjingjun"
    user_id = request.COOKIES.get('uid')
    task_detail = models.webqoqps.objects.filter(id=task_id)
    diff_detail = models.webqodiffcontent.objects.filter(diff_fk_id=task_id)
    business_lst = layout.Business.objects.all()
    app_lst = layout.Application.objects.all()
    user_app_lst = layout.UserToApp.objects.filter(user_name_id=user_id)

    testitem=models.webqoqps.objects.filter(id=task_id).values('testitem')

    page=request.GET.get('page')
    current_page=1
    if page:
        current_page=int(page)

    if testitem.first()['testitem']==1:

        return render(request, 'qo_task_tail.html',
                      {'business_lst': business_lst, 'app_lst': app_lst, 'user_id': user_id, 'user_app_lst': user_app_lst,
                       'businame': 'Webqo', 'app_name': "webqo性能对比自动化", 'topic': '任务详情', 'task_detail': task_detail})
    elif testitem.first()['testitem']==0:
        page_obj=pagination.Page(current_page,len(diff_detail),3,9)
        data=diff_detail[page_obj.start:page_obj.end]
        page_str=page_obj.page_str('qo_task_detail_'+task_id+'.html?page=')

        return render(request, 'qo_diff_detail.html',
                      {'business_lst': business_lst, 'app_lst': app_lst, 'user_id': user_id,
                       'user_app_lst': user_app_lst,
                       'businame': 'Webqo', 'app_name': "diff", 'topic': '任务详情', 'task_detail': task_detail,
                       'diff_detail':diff_detail,'li':data,'page_str':page_str})



@auth
def qo_automation_add(request):
    # user_id = "zhangjingjun"
    user_id = request.COOKIES.get('uid')
    ret = {'status': True, 'errro': None, 'data': None}
    test_svn = str_dos2unix(request.POST.get('qo_testsvn'))
    base_svn = str_dos2unix(request.POST.get('qo_basesvn'))
    newconfip = str_dos2unix(request.POST.get('new_conf_ip'))
    newconfuser = str_dos2unix(request.POST.get('new_conf_user'))
    newconfpassw = str_dos2unix(request.POST.get('new_conf_pass'))
    newconfpath = str_dos2unix(request.POST.get('new_conf_path'))
    newdataip = str_dos2unix(request.POST.get('new_data_ip'))
    newdatauser = str_dos2unix(request.POST.get('new_data_user'))
    newdatapassw = str_dos2unix(request.POST.get('new_data_pass'))
    newdatapath = str_dos2unix(request.POST.get('new_data_path'))
    press_qps = str_dos2unix(request.POST.get('qo_qps'))
    press_time = str_dos2unix(request.POST.get('qo_press_time'))
    press_expid = str_dos2unix(request.POST.get('qo_press_expid'))
    press_rate = str_dos2unix(request.POST.get('qo_press_rate'))

    query_ip = str_dos2unix(request.POST.get('query_ip'))
    query_user = str_dos2unix(request.POST.get('query_user'))
    query_pwd = str_dos2unix(request.POST.get('query_pwd'))
    query_path = str_dos2unix(request.POST.get('query_path'))

    testtag = str_dos2unix(request.POST.get('testtag'))

    flag=request.POST.get('radio_select')
    print("flag:",flag)
    print("press_expid", type(press_expid))
    print("press_rate", type(press_rate))

    if flag=='press':
        if press_qps == "":
            press_qps = 1000
        if press_time == "":
            press_time = 30
        if press_expid == "":
            press_expid = 0
        if press_rate == "":
            press_rate = 0
        # print('test_svn:'+test_svn,'base_svn:'+base_svn,'newconfip:'+newconfip,'newconfuser:'+newconfuser,'newconfpassw:'+newconfpassw,'newconfpath:'+newconfpath,'newdataip:'+newdataip,'newdatauser:'+newdatauser,'newdatapassw:'+newdatapassw,'newdatapath:'+newdatapath)
        try:
            models.webqoqps.objects.create(create_time=get_now_time(), user=user_id, testitem=1, testsvn=test_svn,
                                           basesvn=base_svn,
                                           newconfip=newconfip, newconfuser=newconfuser, newconfpassw=newconfpassw,
                                           newconfpath=newconfpath, newdataip=newdataip, newdatauser=newdatauser,
                                           newdatapassw=newdatapassw, newdatapath=newdatapath, press_qps=press_qps,
                                           press_time=press_time, press_expid=press_expid, press_rate=press_rate,
                                           testtag=testtag)
        except Exception as e:
            print(e)
            ret['error'] = 'error:' + str(e)
            ret['status'] = False
        return HttpResponse(json.dumps(ret))
    elif flag=='longdiff':
        if press_expid == "":
            press_expid = 0
        if press_rate == "":
            press_rate = 0
        try:
            models.webqoqps.objects.create(create_time=get_now_time(), user=user_id, testitem=0, testsvn=test_svn,
                                           basesvn=base_svn,
                                           newconfip=newconfip, newconfuser=newconfuser, newconfpassw=newconfpassw,
                                           newconfpath=newconfpath, newdataip=newdataip, newdatauser=newdatauser,
                                           newdatapassw=newdatapassw, newdatapath=newdatapath, press_expid=press_expid,
                                           press_rate=press_rate, query_ip=query_ip, query_user=query_user,
                                           query_pwd=query_pwd,
                                           query_path=query_path, testtag=testtag)
        except Exception as e:
            print(e)
            ret['error'] = 'error:' + str(e)
            ret['status'] = False
        return HttpResponse(json.dumps(ret))


@auth
def qo_automation(request, page_id):
    # user_id="zhangjingjun"
    user_id = request.COOKIES.get('uid')
    if page_id == '':
        page_id = 1
    task_list = models.webqoqps.objects.order_by('id')[::-1]
    current_page = page_id
    current_page = int(current_page)
    page_obj = pagination.Page(current_page, len(task_list), 16, 9)
    data = task_list[page_obj.start:page_obj.end]
    page_str = page_obj.page_str("/qo_automation")

    business_lst = layout.Business.objects.all()
    app_lst = layout.Application.objects.all()
    user_app_lst = layout.UserToApp.objects.filter(user_name_id=user_id)
    app_id_lst = list()
    for appid in user_app_lst:
        app_id_lst.append(appid.app_id_id)
    if 5 in app_id_lst:
        return render(request, 'qo_automation.html',
                      {'business_lst': business_lst, 'user_id': user_id, 'user_app_lst': user_app_lst,
                       'app_lst': app_lst, 'businame': 'Webqo', 'app_name': "webqo性能对比自动化", 'li': data,
                       'page_str': page_str})
    else:
        return render(request, 'no_limit.html',
                      {'business_lst': business_lst, 'user_app_lst': user_app_lst, 'user_id': user_id,
                       'app_lst': app_lst, 'businame': 'Webqo', 'app_name': "webqo性能对比自动化"})


def get_now_time():
    timeArray = time.localtime()
    return time.strftime("%Y-%m-%d %H:%M:%S", timeArray)


def str_dos2unix(input):
    return input.replace('\r\n', '\n').replace(' ', '')


def logout(request):
    response = redirect('https://login.sogou-inc.com/?appid=1162&sso_redirect=http://frontqa.web.sjs.ted/&targetUrl=')
    if ('uid' in request.COOKIES):
        response.delete_cookie("uid")
    return response
