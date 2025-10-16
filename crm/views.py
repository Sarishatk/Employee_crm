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

        def get(self, request,**kwargs):

                update_id = kwargs.get('pk')

                emp_data = Employeecrm.objects.get(id = update_id )

                return render(request,"update_emp.html",{"emp_data": emp_data})
        
        def post(self,request,**kwargs):
 
                update_id = kwargs.get('pk')


                emp_data = Employeecrm.objects.get(id = update_id)

                print(request.POST)

                emp_data.name = request.POST.get("username")

                emp_data.role = request.POST.get("user_role")

                emp_data.place = request.POST.get("user_place")

                emp_data.salary = request.POST.get("user_salary")

                emp_data.save()

                return render(request,"update_emp.html")
        

class DeleteEmployeeVIew(View):

        def get(self,request,**kwargs):

                delete_id = kwargs.get('pk')

                emp_data = Employeecrm.objects.get(id = delete_id )

                emp_data.delete()

                return render(request,"add_employee.html")
        

class EmployeeRetriev(View):

        def get(self,request,**kwargs):

                retriev_id = kwargs.get('pk')

                emp_data = Employeecrm.objects.get(id =  retriev_id )





