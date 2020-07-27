from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

def default(requests) :
    return render(requests, 'home.html')
def output(requests):
    import requests
    data = requests.get('https://reqres.in/api/users')
    print(data.text)
    data=data.text
    return render(requests, 'home.html', {'data':data})
def upload(requests) :
    return render(requests, 'upload.html')
def home(requests) :
    return render(requests, 'home.html')
def summarize(request) :
        if request.method == 'POST' and request.FILES['videoFile']:
            videoFile = request.FILES['videoFile']
            print(videoFile)
            print(videoFile.size)
            fs = FileSystemStorage()
            filename = fs.save(videoFile.name, videoFile)
            uploaded_file_url = fs.url(filename)
            return render(request, 'summarize.html', {
                'uploaded_file_url': uploaded_file_url
            })
        return render(request, 'upload.html')
