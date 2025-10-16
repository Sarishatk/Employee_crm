from django.shortcuts import render
from django.views.generic import View
from crm.models import Employeecrm
# Create your views here.

class CreateEmployeeView(View):

        def get(self, request):
                
                return render(request,"add_employee.html")
        
        def post(self, request):
                
                print(request.POST)

                Employeecrm.objects.create(name = request.POST.get('username'),
                                           role = request.POST.get('user_role'),
                                           place = request.POST.get('user_place'),
                                           salary = request.POST.get('user_salary')
                                           )

                return render(request,"add_employee.html")
                

class EmployeeListView(View):
        
        def get(self,request):
                
                data = Employeecrm.objects.all()

                return render(request,"employee_list.html",{"data":data})
        

class EmployeeUpdate(View):

        def get(self, request):

                emp_data = Employeecrm.objects.get(id = 1)

                return render (request,"update_emp.html",{ " emp_data":  emp_data})


        


