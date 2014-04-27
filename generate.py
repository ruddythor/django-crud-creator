import sys

#def print_args(arg_list):
#    """ generate CRUD views for a django model """
#    for arg in arg_list:
#        print arg

#print_args(sys.argv)



def create_function(arg=sys.argv[1]):
  string = """
def create(request):
    ''' creates a new attendee for the current year's auction.
    '''
    if request.POST:
        form = AttendeeForm(request.POST)
        if form.is_valid():
            attendee = form.save()
            invoice = Invoice(total_amount=0)
            invoice.attendee = attendee
            invoice.save()
            messages.add_message(request, messages.SUCCESS, 'New Attendee Added. Invoice added and associated with attendee.')
            return redirect('attendee_list')
        else:
            if len(Attendee.objects.filter(year=lambda: datetime.datetime.now().year)) > 0:
                latest = Attendee.objects.latest('bid_number')
                bid_number = latest.bid_number + 1
            context = {'form': form,
                       'bid_number': bid_number,
                       'table_assignment': form.cleaned_data['table_assignment']}
            return render(request, 'attendee/add.html', context)
    else:
        form = AttendeeForm()
        # Check to see if there are attendees for this year's auction. If there are, set the default bid number
        # to one more than the highest bid number. If no attendees, set bid number to 1.
        if len(Attendee.objects.filter(year=lambda: datetime.datetime.now().year)) > 0:
            latest = Attendee.objects.latest('bid_number')
            bid_number = latest.bid_number + 1
        else:
            bid_number = 1
        context = {'form': form,
                   'bid_number': bid_number,
                   }
        return render(request, 'attendee/add.html', context)
"""

#create_function()



def create_info_view(model=sys.argv[1]):
    """ create info view """
    func = """
def info(request, id):
    ''' Info view for %s model
    '''
    attendee = %s.objects.get(id=id)
    return render(request, 'attendee/info.html', {'%s': %s})
""" % (model, model, model.lower(), model.lower())
    return func

if sys.argv[1][0].isupper():
    print create_info_view()
else:
    print "Model name must be properly capitalized"











