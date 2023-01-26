from django import forms

from app.models import Courses


class DateInput(forms.DateInput):
    input_type = "date"


class AddStudentForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class": "form-control"}))
    password = forms.CharField(label="Mot de Passe", max_length=50,
                               widget=forms.PasswordInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(label="Prénom", max_length=50,
                                 widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label="Nom", max_length=50,
                                widget=forms.TextInput(attrs={"class": "form-control"}))
    username = forms.CharField(label="Nom Utilisateur", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    address = forms.CharField(label="Adresse", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))

    courses = Courses.objects.all()
    course_list = []
    for course in courses:
        small_course = (course.id, course.course_name)
        course_list.append(small_course)

    gender_choice = (
        ("Male", "Masculin"),
        ("Female", "Feminin")
    )

    course = forms.ChoiceField(label="Classe", choices=course_list,
                               widget=forms.Select(attrs={"class": "form-control"}))
    sex = forms.ChoiceField(label="Sexe", choices=gender_choice, widget=forms.Select(attrs={"class": "form-control"}))
    session_start = forms.DateField(label="date de naissance", widget=DateInput(attrs={"class": "form-control"}))
    session_end = forms.DateField(label="debut d'année", widget=DateInput(attrs={"class": "form-control"}))
    profile_pic = forms.FileField(label="Photo de Profil", max_length=50,
                                  widget=forms.FileInput(attrs={"class": "form-control"}))


class EditStudentForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(label="Prénom", max_length=50,
                                 widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label="Nom", max_length=50,
                                widget=forms.TextInput(attrs={"class": "form-control"}))
    username = forms.CharField(label="Nom Utilisateur", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    address = forms.CharField(label="Adresse", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))

    courses = Courses.objects.all()
    course_list = []
    for course in courses:
        small_course = (course.id, course.course_name)
        course_list.append(small_course)

    gender_choice = (
        ("Male", "Masculin"),
        ("Female", "Feminin")
    )

    course = forms.ChoiceField(label="Classe", choices=course_list,
                               widget=forms.Select(attrs={"class": "form-control"}))
    sex = forms.ChoiceField(label="Sexe", choices=gender_choice, widget=forms.Select(attrs={"class": "form-control"}))
    session_start = forms.DateField(label="Date de Naissance", widget=DateInput(attrs={"class": "form-control"}))
    session_end = forms.DateField(label="Debut d'année", widget=DateInput(attrs={"class": "form-control"}))
    profile_pic = forms.FileField(label="Photo de Profil", max_length=50,
                                  widget=forms.FileInput(attrs={"class": "form-control"}), required=False)
