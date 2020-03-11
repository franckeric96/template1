from django.shortcuts import render

# Create your views here.
def index(request):
    datas = {
        
    }
    return render(request, 'index.html', datas)

def club(request):
    datas = {
        
    }
    return render(request, 'club.html', datas)


def schedule(request):
    datas = {
        
    }
    return render(request, 'schedule.html', datas)



def result(request):
    datas = {
        
    }
    return render(request, 'result.html', datas)


def blog(request):
    datas = {
        
    }
    return render(request, 'blog.html', datas)


def blogdetails(request):
    datas = {
        
    }
    return render(request, 'blog-details.html', datas)



def contact(request):
    datas = {
        
    }
    return render(request, 'contact.html', datas)