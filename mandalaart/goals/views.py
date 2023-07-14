from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import MainGoalForm, SubGoalForm, WayGoalForm
from .models import Plan, SubGoal, WayGoal
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
import pdfkit  # `pdfkit` 라이브러리를 설치


# 만다라트 리스트 조회
def main_page(request):
    plans = Plan.objects.all()
    return render(request, "goal_list.html", {"plans": plans})


# 메인 목표 입력
def main_goal_input(request):
    if request.method == "POST":
        form = MainGoalForm(request.POST)
        if form.is_valid():
            main_goal = form.cleaned_data["main_goal"]
            plan = Plan.objects.create(main_goal=main_goal)
            return redirect("sub_goal_input", plan_id=plan.id)
    else:
        form = MainGoalForm()
    return render(request, "main_goal_input.html", {"form": form})


# 서브 목표 입력
def sub_goal_input(request, plan_id):
    plan = Plan.objects.get(pk=plan_id)

    if request.method == "POST":
        sub_goals = []
        for i in range(1, 10):
            sub_goal_input = request.POST.get(f"sub_goal{i}")
            if sub_goal_input:
                sub_goals.append(sub_goal_input)

        # 기존의 SubGoal 객체들을 삭제
        SubGoal.objects.filter(plan=plan).delete()

        # 수정된 값들로 새로운 SubGoal 객체들 생성
        for sub_goal in sub_goals:
            SubGoal.objects.create(plan=plan, sub_goal=sub_goal)

        return redirect(reverse("3x3_table", kwargs={"plan_id": plan_id}))
    else:
        # 기존의 SubGoal 객체들을 가져와서 폼 초기값으로 사용
        sub_goal_initial_values = SubGoal.objects.filter(plan=plan).values_list(
            "sub_goal", flat=True
        )
        sub_goal_initial_list = list(sub_goal_initial_values)[:8]
        form = SubGoalForm(initial={"sub_goals": sub_goal_initial_list})

    return render(request, "sub_goal_input.html", {"form": form, "plan_id": plan_id})


# 메인 목표 및 서브 목표 수정
def goal_edit(request, plan_id):
    plan = Plan.objects.get(pk=plan_id)
    sub_goal_ids = plan.sub_goals.values_list("id", flat=True)[
        :8
    ]  # 최대 8개의 SubGoal ID 가져오기

    print(sub_goal_ids)  # Sub Goal ID 출력

    sub_goals = SubGoal.objects.filter(id__in=sub_goal_ids).order_by(
        "id"
    )  # SubGoal을 ID 기반으로 가져오기

    if request.method == "POST":
        main_goal_input = request.POST.get("main_goal")
        if main_goal_input.strip():
            plan.main_goal = main_goal_input.strip()
            plan.save()

        for sub_goal, i in zip(sub_goals, range(1, 9)):
            sub_goal_input = request.POST.get(f"sub_goal{i}")
            if sub_goal_input.strip():
                sub_goal.sub_goal = sub_goal_input.strip()
                sub_goal.save()

        return redirect(reverse("3x3_table", kwargs={"plan_id": plan_id}))

    return render(
        request,
        "goal_edit.html",
        {"sub_goals": sub_goals, "main_goal": plan.main_goal, "plan_id": plan_id},
    )


# 3x3 테이블 형식
def three_by_three_table(request, plan_id):
    plan = Plan.objects.get(pk=plan_id)
    sub_goals = SubGoal.objects.filter(plan=plan)[:8]  # 최대 8개의 SubGoal 가져오기

    # 8개의 SubGoal을 3x3 행렬 형태로 나누기
    sub_goal_rows = [sub_goals[i : i + 3] for i in range(0, len(sub_goals), 3)]

    return render(
        request,
        "3x3_table.html",
        {"plan": plan, "sub_goal_rows": sub_goal_rows, "main_goal": plan.main_goal},
    )


# 세부 목표 입력
def way_goal_input(request, plan_id, sub_goal_id):
    plan = Plan.objects.get(pk=plan_id)
    sub_goal = get_object_or_404(SubGoal, pk=sub_goal_id)

    if request.method == "POST":
        form = WayGoalForm(request.POST)
        if form.is_valid():
            way_goal = form.cleaned_data["way_goal"]
            WayGoal.objects.create(sub=sub_goal, way_goal=way_goal)
            return redirect(
                reverse(
                    "way_goal_input",
                    kwargs={"plan_id": plan_id, "sub_goal_id": sub_goal_id},
                )
            )
    else:
        form = WayGoalForm()

    way_goals = WayGoal.objects.filter(sub=sub_goal)

    return render(
        request,
        "way_goal_input.html",
        {
            "form": form,
            "plan_id": plan_id,
            "sub_goal_id": sub_goal_id,
            "way_goals": way_goals,
            "main_goal": plan.main_goal,
        },
    )
