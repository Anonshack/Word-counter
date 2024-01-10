from django.shortcuts import render


def counter(request):
	if request.method == 'POST':
		text = request.POST['texttocount']
		if text != '':
			word = len(text.split())
			i = True
			return render(request, 'home.html', {'word': word, 'text': text, 'i': i, 'on': 'active'})
		else:
			return render(request, 'home.html', {'on': 'active'})
	else:
		return render(request, 'home.html', {'on': 'active'})
