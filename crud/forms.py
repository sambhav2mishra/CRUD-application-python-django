from dataclasses import field, fields
from django import forms   
from .models import Employee

class EmployeeForm(forms.ModelForm):     #forms.ModelForm is base class

    class Meta:
        model = Employee
        fields = '__all__'    #if we want all the properties in Employee model as fields in EmployeeForm.
        #fields = ('emp_code','fullname') #if we want some of the properties in Employee model as fields in EmployeeForm.
        labels = {
            'fullname':'Full Name',
            'emp_code':'Employee Code',
            'emp_email':'Employee Email',
            'mobile':'Mobile Number',
            'position':'Designation'
        }

    def __init__(self, *args, **kwargs):   
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"    
        self.fields['emp_code'].required = False   # not mandatory field while filling form.
