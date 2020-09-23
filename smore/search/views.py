from django.db.models import Q
from django.shortcuts import render
from search.models import collegeCourse
from django.template.loader import render_to_string
from django.http import JsonResponse
# Create your views here.
# search/views.py
def course_view(request):
    ctx = {}
    url_param = request.GET.get("q")

    if url_param:
        courses = collegeCourse.objects.filter(
            Q(class_id__icontains=url_param) | Q(course_code__icontains=url_param) |
            Q(professor__icontains=url_param) | Q(day__icontains=url_param) |
            Q(time__icontains=url_param)
        )

    else:
        courses = collegeCourse.objects.all()

    ctx["courses"] = courses

    if request.is_ajax():
        html = render_to_string(
            template_name="partial-courses.html",
            context={"courses": courses}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)

    return render(request, "courses.html", context=ctx)
