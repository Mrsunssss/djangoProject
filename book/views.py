from django.shortcuts import render,HttpResponse
# 通过查询字符串(query string)
def book_detail_query_string(request):
    book_id = request.GET.get('id')
    return HttpResponse(f"您查询的ID为：{book_id}")
# 通过path中携带：http://localhost:8000/1
def book_detail_path(request,book_id):
    return HttpResponse(f"您查询的ID为：{book_id}")

def book_html(request):
    # 普通变量
    user_name = '孙可宁'
    # 字典类型
    user_info = {
        'name':'孙可宁',
        'age':18,
        'gender':'男'
    }
    # 列表
    books = [
        {'name':'西游记','price':'100'},
        {'name':'水浒传','price':'200'},
        {'name':'三国演义','price':'300'},
        {'name':'红楼梦','price':'400'},
    ]
    # 对象
    class Book:
        def __init__(self,name):
            self.name = name
    context = {
        'user_name': user_name,
        'user_info': user_info,
        'books':books,
        'Book':Book('西行记'),
    }
    return render(request,'book.html',context=context)