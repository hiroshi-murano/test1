from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import sqlite3
import json
from django.views.decorators.csrf import csrf_protect, csrf_exempt


DB = 'plot_data.sqlite3'

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    """
    """


    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cmd = "select * from sagyo_log"
    cur.execute(cmd)
    lst = cur.fetchall()

    data_x=[]
    data_y=[]
    for row in lst:
        print(row)
        data_x.append(row[3])
        data_y.append(row[4])

    cur.close()
    conn.close()

    # data_x=['2019-04-18 16:00:00','2019-04-18 16:00:10','2019-04-18 16:00:13','2019-04-18 16:00:20',]
    # data_y=[1,0,1,0,]
    context = {'title': 'タイトルです',
    'data_x':data_x,
    'data_y':data_y}

    return render(request, 'app/index.html', context)



def data_input(request):
    """
    """

    context={}

    return render(request, 'app/data_input.html', context)

@csrf_exempt
def api_01(request):
    """
    JSON返すAPI
    """

    method = request.method
    # print('メソッド={}'.format(method))

    if request.method == 'GET':
        keyword1 = request.GET['keyword1']
        dt = request.GET['date']
        dictData = {}
        dictData['データ'] = '送信されたキーワードは「{}」です'.format(keyword1)
        dictData['date'] = '送信された時刻は「{}」です'.format(dt)

        json_str = json.dumps(dictData, ensure_ascii=False, indent=2,)
        status = 200
        return HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=status)
    elif request.method == 'POST':
        keyword1 = request.POST['keyword1']
        keyword2 = request.POST['keyword2']

        insert_date(keyword2,keyword1)


        dictData = {}
        dictData['データ'] = '送信されたキーワードは「{}+{}」です'.format(keyword1, keyword2)

        json_str = json.dumps(dictData, ensure_ascii=False, indent=2,)
        status = 200
        return HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=status)



def insert_date(dt,status):
    """
    """

    conn = sqlite3.connect(DB)
    cur = conn.cursor()
  
    sql="insert into sagyo_log('user_id','sagyo','dt','status') values (?,?,?,?)"
    # dt1=datetime.datetime.now()
  
    lstData=['hoge','foo',dt,status]
    cur.execute(sql, lstData)
    conn.commit()

    cur.close()
    conn.close()



