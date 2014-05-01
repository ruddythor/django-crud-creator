import sys
import os

"""
Creates Django CRUD Model Methods and Views for an app.
usage:
python generate.py ModelName AppName

creates the given modelname and modelviews under the given app name. Run this at the project level.
This follows the project/app/models and project/app/views layout for a Django project
+

"""

#def print_args(arg_list):
#    """ generate CRUD views for a django model """
#    for arg in arg_list:
#        print arg

#print_args(sys.argv)



#pip install -e git+https://github.com/benthor/inflect.py#egg=inflect
# the above is for the pluralize library


def create_create_view(model=sys.argv[1]):

    func = """
def create_view(request):
    ''' creates a new %s instance.
    '''
    if request.POST:
        form = %sForm(request.POST)
        if form.is_valid():
            %s = form.save()
            return redirect('%s_list')
        else:

            context = {'form': form,}
            return render(request, '%s/add.html', context)
    else:
        form = %sForm()
        context = {'form': form,
                   }
        return render(request, '%s/add.html', context)
""" % (model.lower(), model, model, model.lower(), model.lower(), model, model.lower())

    return func


def create_info_view(model=sys.argv[1]):
    """ create info view """

    func = """
def info_view(request, id):
    ''' Info view for %s model
    '''
    %s = %s.objects.get(id=id)
    return render(request, 'attendee/info.html', {'%s': %s})
""" % (model, model.lower(), model, model.lower(), model.lower())
    return func


def create_list_view(model=sys.argv[1]):
    """ create list view """

    func = """
def list_view(request):
    ''' Get a list of all %s objects.
    '''
    %s = %s.objects.all()
    context = {'%s': %s,
               }
    return render(request, 'attendee/attendee_list.html', context)""" % (model, model.lower(), model, model.lower(), model.lower())
# TODO: pluralize these model string format variables

    return func


def create_update_view(model=sys.argv[1]):
    """ create the update view for a model """

    func = """
def update_view(request, id):
    ''' Updates a %s record
    '''
    %s = get_object_or_404(%s, id=id)

    if request.POST:
        form = %sForm(request.POST, instance=%s)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, '%s Information updated')
            return redirect('%s_list')
        else:
            return redirect('%s_info', id)
    else:
        form = %sForm(instance=%s)
        context = {'%s': %s,
                   'form': form,
                   }

    return render(request, '%s/update.html', context)""" % (model, model.lower(), model, model, model.lower(), model, model.lower(), model.lower(), model, model.lower(), model.lower(), model.lower(), model.lower())

    return func








path = os.path.realpath(__file__)
path = os.path.dirname(__file__)
print path, 'hiiii'
path = os.path.abspath(path)
print 'CWD', path


contents = create_create_view() + '\n' + create_update_view() + '\n' + create_list_view() + '\n' + create_info_view()



if sys.argv[1][0].isupper():
    f = open(str(sys.argv[1].lower())+'.py', 'w+')
    f.write(contents)
    f.close()
    if os.path.exists(os.path.join(path, sys.argv[2].lower())):
        model_file = open(os.path.join(path, str(sys.argv[2].lower()), str(sys.argv[1].lower()))+'.py', 'w+')
        model_file.write(contents)
        model_file.close()
    else:
        os.makedirs(os.path.join(path, sys.argv[2].lower()))
        model_file = open(os.path.join(path, str(sys.argv[2].lower()), str(sys.argv[1].lower()))+'.py', 'w+')
        model_file.write(contents)
        model_file.close()

else:
    print "Model name must be properly capitalized"












