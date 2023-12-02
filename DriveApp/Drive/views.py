from datetime import date
from django.shortcuts import render

data = {
    "files": [
        {
            "title": "Dosya adı 1",
            "decription": "Dosya açıklama 1 ",
            "imageUrl": "m1.jpg",
            "coverImage": "cover1.jpg",
            "slug": "file-name-1",
            "language": "english",
            "date" : date(2020,5,10)
        },
        {
            "title": "Dosya adı 2",
            "decription": "Dosya açıklama 2 ",
            "imageUrl": "m2.jpg",
            "coverImage": "cover2.jpg",
            "slug": "file-name-2",
            "language": "english",
            "date" : date(2021,6,1)
        },
        {
            "title": "Dosya adı 3",
            "decription": "Dosya açıklama 3 ",
            "imageUrl": "m3.jpg",
            "coverImage": "cover3.jpg",
            "slug": "file-name-3",
            "language": "english",
            "date" : date(2023,7,10)
        },
        {
            "title": "Dosya adı 4",
            "decription": "Dosya açıklama 4 ",
            "imageUrl": "m4.jpg",
            "coverImage": "cover1.jpg",
            "slug": "file-name-4",
            "language": "english",
            "date" : date(2022,8,25)
        }
    ],
    "sliders": [
        {
            "slider_image":"slider1.jpg",
            "url":"file-name-1"
        },
        {
            "slider_image":"slider2.jpg",
            "url":"file-name-2"
        },
        {
            "slider_image":"slider3.jpg",
            "url":"file-name-3"
        }
    ]
}

# Create your views here.
def index(request):
    files = data["files"][-4:]
    sliders=data["sliders"]
    return render(request, 'index.html',{
        "files": files,
        "sliders":sliders
    })

def files(request):
    files = data["files"]
    return render(request,'files.html',{
        "files": files
    })

def file_details(request, slug):
    files = data["files"]
    # selectedFile = None
    # for file in files:
    #    if file["slug"] == slug:
    #        selectedFile = file

    selectedFile = next(file for file in files if file["slug"]==slug)


    return render(request,'file-details.html',{
        "file": selectedFile
    })
