from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Part

# Create your views here.


def part_list(request):
    parts = Part.objects.order_by('part_id')
    return render(request, 'store/part_list.html',{
        'parts': parts
    })


def part_detail(request, pk):
    part = get_object_or_404(Part, pk=pk)
    return render(request,'store/part_detail.html', {'part':part})