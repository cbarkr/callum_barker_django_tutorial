from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id) -> HttpResponse | HttpResponseRedirect:
    question: Question = get_object_or_404(Question, pk=question_id)

    try:
        # request.POST["choice"] returns the ID of the selected choice as a string
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        context: dict[str, str | Question] = {
            "question": question,
            "error_message": "You didn't select a choice.",
        }

        # Route back to voting form
        return render(request, "polls/detail.html", context)
    else:
        selected_choice.votes += 1
        selected_choice.save()

    # Redirect
    # Note: Args *must* be a list
    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
