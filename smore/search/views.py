from django.shortcuts import render
from .models import collegeCourse
from django.template.loader import render_to_string
from django.http import JsonResponse
# Create your views here.
# core/views.py
def course_view(request):
    ctx = {}
    url_param = request.GET.get("q")

    if url_param:
        courses = collegeCourse.objects.filter(course_code__icontains=url_param)
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
