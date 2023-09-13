# The external link need ti be changed in run([{this need to be changed}])
from django.shortcuts import render
from subprocess import run
import sys
def button(request):
    return render(request,"home1.html")
def output(request):
    data = 2 * 2
    return render(request,'home1.html')
def external(request):
    out = run([sys.executable,'C:\\Users\\prave\\Desktop\\kaksha_Svachaalan2\\App.py'],shell=False)
    return render(request,"home1.html")