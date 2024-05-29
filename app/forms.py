# courses/forms.py
from django import forms
from .models import Course, CourseSchedule

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['code', 'name', 'description', 'instructor', 'capacity', 'schedule']

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.fields['code'].widget = forms.TextInput(attrs={
            'class': 'form-input mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50',
           
        })
        self.fields['name'].widget = forms.TextInput(attrs={
            'class': 'form-input mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50',
            
        })
        self.fields['description'].widget = forms.Textarea(attrs={
            'class': 'form-textarea mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50',
            
            'rows': 3
        })
        # self.fields['prerequisites'].widget = forms.CheckboxSelectMultiple(attrs={
        #     'class': 'form-checkbox mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'
        # })
        self.fields['instructor'].widget = forms.TextInput(attrs={
            'class': 'form-input mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50',
            
        })
        self.fields['capacity'].widget = forms.NumberInput(attrs={
            'class': 'form-input mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50',
            
        })
        self.fields['schedule'].widget = forms.TextInput(attrs={
            'class': 'form-input mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'
        })
