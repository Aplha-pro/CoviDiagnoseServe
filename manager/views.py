from django.http import JsonResponse
from django.shortcuts import render
from . import main


def manager(request):
    return render(request, 'index.html')


def upload_image(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        
        with open(main.path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        result = main.predict()
        

        return JsonResponse({'message': f'This image is belongs to the class "{result}".'}, status=200)
    else:
        return JsonResponse({'error': 'No image uploaded'}, status=400)


