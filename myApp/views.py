from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.db import models
from django.http import HttpResponseNotFound, JsonResponse
from django.http import HttpResponseBadRequest
import json

# Create your views here.
from .forms import CableMatrixForm, EditCableMatrixForm, DCSRequestForm, CableTraceForm, NetworkDesignForm, cmForm, deviceInstallationForm, portAssignmentForm, cableMeasurementForm
from .models import CableMatrixModel

# Create your views here.

def home_page(request):
    rows_count = CableMatrixModel.objects.count()
    cable_matrix_instance = CableMatrixModel.objects.all()
    # DCS Request Phase
    dcs_in_progress_count = cable_matrix_instance.filter(dcs_status='In Progress').count() + cable_matrix_instance.filter(dcs_status='Yet To Work').count() + cable_matrix_instance.filter(dcs_status='Not Required').count()
    dcs_not_yet_started_count = cable_matrix_instance.filter(dcs_status='Not yet Started').count()
    dcs_completed_count = cable_matrix_instance.filter(dcs_status='Completed').count()
    dcs_cancelled_count = cable_matrix_instance.filter(dcs_status='Cancelled').count()
    
    # Cable trace Phase
    ct_in_progress_count = cable_matrix_instance.filter(cable_trace_status='In Progress').count() + cable_matrix_instance.filter(cable_trace_status='Yet To Work').count() + cable_matrix_instance.filter(cable_trace_status='Not Required').count()
    ct_not_yet_started_count = cable_matrix_instance.filter(cable_trace_status='Not yet Started').count()
    ct_completed_count = cable_matrix_instance.filter(cable_trace_status='Completed').count()
    ct_cancelled_count = cable_matrix_instance.filter(cable_trace_status='Cancelled').count()
    
    
    
    context = {
        'rows_count': rows_count,
        'in_progress_count': dcs_in_progress_count + ct_in_progress_count,
        'not_yet_started_count': dcs_not_yet_started_count + ct_not_yet_started_count,
        'completed_count': dcs_completed_count + ct_completed_count,
        'cancelled_count': dcs_cancelled_count + ct_cancelled_count,
    }
    return render(request, 'home_page.html', context)

def cb_home(request):
    try:
        query = request.GET.get('q', '')
        cable_matrix_instance = CableMatrixModel.objects.all()

        if request.method == 'POST':
            form_id = request.POST.get('form_id')
            if form_id:
                cb_form_instance = get_object_or_404(CableMatrixModel, pk=form_id)
                cb_form_instance.delete()
                messages.success(request, 'Item deleted successfully.')
                return redirect('cb_home')
        if query:
            filtered_requests = cable_matrix_instance.filter(
                models.Q(requestor__icontains=query) |
                models.Q(requesttype__icontains=query) |
                models.Q(olddevice__icontains=query) |
                models.Q(oldmodel__icontains=query) |
                models.Q(rrd__icontains=query) |
                models.Q(ipn__icontains=query) |
                models.Q(cpn__icontains=query) |
                models.Q(pn__icontains=query) |
                models.Q(pm__icontains=query) |
                models.Q(newdevice__icontains=query) |
                models.Q(newmodel__icontains=query) |
                models.Q(location__icontains=query) |
                models.Q(clli__icontains=query) |
                models.Q(domain__icontains=query) |
                
                models.Q(requested_date__icontains=query) |
                models.Q(request_id__icontains=query) |
                models.Q(approved_date__icontains=query) |
                models.Q(dcs_status__icontains=query) |
                models.Q(power_status__icontains=query) |
                models.Q(rack_status__icontains=query) |
                models.Q(dcs_comment__icontains=query) |
                
                models.Q(cable_trace_requested_date__icontains=query) |
                models.Q(cable_trace_received_date__icontains=query) |
                models.Q(tickets_required__icontains=query) |
                models.Q(tickets_requested_date__icontains=query) |
                models.Q(tickets_requested_id__icontains=query) |
                models.Q(tickets_closed_date__icontains=query) |
                models.Q(cable_trace_status__icontains=query) |
                models.Q(cable_trace_comment__icontains=query) |
                
                models.Q(network_design_start_date__icontains=query) |
                models.Q(network_design_close_date__icontains=query) |
                models.Q(network_design_status__icontains=query) |
                models.Q(network_design_comment__icontains=query) |
                
                models.Q(cable_matrix_started_date__icontains=query) |
                models.Q(cable_matrix_status__icontains=query) |
                models.Q(cable_matrix_completed_date__icontains=query) |
                models.Q(cable_matrix_comment__icontains=query)
            )
        else:
            filtered_requests = cable_matrix_instance

        rows_count = CableMatrixModel.objects.count()
        # in_progress_devices = list(CableMatrixModel.objects.filter(status="In Progress").values())
        
        # Count requests by status 
        # DCS Request Phase
        dcs_in_progress_count = filtered_requests.filter(dcs_status='In Progress').count() + filtered_requests.filter(dcs_status='Yet To Work').count() + filtered_requests.filter(dcs_status='Not Required').count()
        dcs_not_yet_started_count = filtered_requests.filter(dcs_status='Not yet Started').count()
        dcs_completed_count = filtered_requests.filter(dcs_status='Completed').count()
        dcs_cancelled_count = filtered_requests.filter(dcs_status='Cancelled').count()
        
        # Cable trace Phase
        ct_in_progress_count = filtered_requests.filter(cable_trace_status='In Progress').count() + filtered_requests.filter(cable_trace_status='Yet To Work').count() + filtered_requests.filter(cable_trace_status='Not Required').count()
        ct_not_yet_started_count = filtered_requests.filter(cable_trace_status='Not yet Started').count()
        ct_completed_count = filtered_requests.filter(cable_trace_status='Completed').count()
        ct_cancelled_count = filtered_requests.filter(cable_trace_status='Cancelled').count()
        
        # Network Design Phase
        nd_in_progress_count = filtered_requests.filter(network_design_status='In Progress').count() + filtered_requests.filter(network_design_status='Yet To Work').count() + filtered_requests.filter(network_design_status='Not Required').count()
        nd_not_yet_started_count = filtered_requests.filter(network_design_status='Not yet Started').count()
        nd_completed_count = filtered_requests.filter(network_design_status='Completed').count()
        nd_cancelled_count = filtered_requests.filter(network_design_status='Cancelled').count()
        
        # Cable Matrix Phase
        cm_in_progress_count = filtered_requests.filter(cable_matrix_status='In Progress').count() + filtered_requests.filter(cable_matrix_status='Yet To Work').count() + filtered_requests.filter(cable_matrix_status='Not Required').count()
        cm_not_yet_started_count = filtered_requests.filter(cable_matrix_status='Not yet Started').count()
        cm_completed_count = filtered_requests.filter(cable_matrix_status='Completed').count()
        cm_cancelled_count = filtered_requests.filter(cable_matrix_status='Cancelled').count()
        
        # Device Installation Phase
        dis_in_progress_count = filtered_requests.filter(device_installation_status='In Progress').count() + filtered_requests.filter(device_installation_status='Yet To Work').count() + filtered_requests.filter(device_installation_status='Not Required').count()
        dis_not_yet_started_count = filtered_requests.filter(device_installation_status='Not yet Started').count()
        dis_completed_count = filtered_requests.filter(device_installation_status='Completed').count()
        dis_cancelled_count = filtered_requests.filter(device_installation_status='Cancelled').count()
        # Port Assignment Phase
        port_assign_in_progress_count = filtered_requests.filter(port_assign_status='In Progress').count() + filtered_requests.filter(port_assignment_status='Yet To Work').count() + filtered_requests.filter(port_assignment_status='Not Required').count()
        port_assign_not_yet_started_count = filtered_requests.filter(port_assignment_status='Not yet Started').count()
        port_assign_completed_count = filtered_requests.filter(port_assignment_status='Completed').count()
        port_assign_cancelled_count = filtered_requests.filter(port_assignment_status='Cancelled').count()

        # cable Measurement phase
        cable_measurement_in_progress_count = filtered_requests.filter(cable_measurement_status='In Progress').count() + filtered_requests.filter(cable_measurement_status='Yet To Work').count() + filtered_requests.filter(cable_measurement_status='Not Required').count()
        cable_measurement_not_yet_started_count = filtered_requests.filter(cable_measurement_status='Not yet Started').count()
        cable_measurement_completed_count = filtered_requests.filter(cable_measurement_status='Completed').count()
        cable_measurement_cancelled_count = filtered_requests.filter(cable_measurement_status='Cancelled').count()
        
        context = {
            'filtered_requests': filtered_requests,
            'query': query,
            'rows_count': rows_count,
            'in_progress_count': dcs_in_progress_count + ct_in_progress_count + nd_in_progress_count + cm_in_progress_count + dis_in_progress_count,
            'not_yet_started_count': dcs_not_yet_started_count + ct_not_yet_started_count + nd_not_yet_started_count + cm_not_yet_started_count + dis_not_yet_started_count,
            'completed_count': dcs_completed_count + ct_completed_count + nd_completed_count + cm_completed_count + dis_completed_count,
            'cancelled_count': dcs_cancelled_count + ct_cancelled_count + nd_cancelled_count + cm_cancelled_count + dis_cancelled_count,
        }

    except Exception as e:
        messages.error(request, f"Error occurred: {str(e)}")
        return HttpResponseNotFound("An error occurred. Please try again later.")

    return render(request, 'cable_matrix/cb_home.html', context)

def cb_static_form(request):
    return render(request, 'cable_matrix/cb_static_form.html')

@require_POST
def submit_cb_static_form(request):
    try:
        form = CableMatrixForm(request.POST)
        print(form)
        if form.is_valid():
            # Check if a record with the same olddevice and newdevice already exists
            if CableMatrixModel.objects.filter(olddevice=form.cleaned_data['olddevice'], newdevice=form.cleaned_data['newdevice']).exists():
                messages.error(request, 'Both olddevice and newdevice already exist in Cable Matrix records.', extra_tags='error')
                return redirect('cb_static_form')
            else:
                # Save the CableMatrixModel1 instance
                form.save()
                
                messages.success(request, 'Cable Matrix record entry created successfully!.')
                return redirect('cb_home')
        else:
            print(form.errors)
            messages.error(request, f'Please correct the errors below.{str(form.errors)}', extra_tags='error')
            return redirect('cb_static_form')

    except Exception as e:
        messages.error(request, f"Error submitting form: {str(e)}", extra_tags='error')

    return redirect('cb_home')  # Redirect back to cb_home regardless of success or failure

@require_POST
def delete_cb_form(request):
    try:
        form_id = request.POST.get('form_id')
        cb_form = get_object_or_404(CableMatrixModel, id=form_id)
        
        cb_form.delete()
        messages.success(request, 'Entry deleted successfully!')
    
    except Exception as e:
        messages.error(request, f"Error deleting entry: {str(e)}")
        return HttpResponseBadRequest("An error occurred while deleting.")

    return redirect('cb_home')

def edit_cb_static_form(request, pk):
    try:
        cb_form = get_object_or_404(CableMatrixModel, pk=pk)
        original_olddevice = cb_form.olddevice
        original_newdevice = cb_form.newdevice
        if request.method == 'POST':
            form = EditCableMatrixForm(request.POST, instance=cb_form)
            if form.is_valid():
                # Save CableMatrixModel1 instance
                if CableMatrixModel.objects.filter(olddevice=form.cleaned_data['olddevice'], newdevice=form.cleaned_data['olddevice']).exists():
                    messages.error(request, 'combination of olddevice and newdevice already exists in Cable Matrix records.', extra_tags='error')
                else:
                    form.save()
                    messages.success(request, 'Updated successfully!')
                    return redirect('cb_home')
            else:
                messages.error(request, 'Please correct the errors below.')
        else:
            form = EditCableMatrixForm(instance=cb_form)

    except Exception as e:
        messages.error(request, f"Error editing Cable Matrix form: {str(e)}")

    context = {
        'form': form,
    }
    return render(request, 'cable_matrix/edit_static_form.html', context)

def device_detail(request, pk):
    device = get_object_or_404(CableMatrixModel, id=pk)
    return render(request, 'cable_matrix/view_all_details.html', {'device': device})


def dcs_request(request):
    query = request.GET.get('q', '')  # Get the search query from the URL parameter 'q'
    dcs_requests = CableMatrixModel.objects.all()  # Query all DCS requests

    if query:
        # Filter DCS requests based on the search query
        filtered_requests = dcs_requests.filter(
            models.Q(newdevice__icontains=query) |
            models.Q(olddevice__icontains=query) |
            models.Q(requested_date__icontains=query) |
            models.Q(request_id__icontains=query) |
            models.Q(approved_date__icontains=query) |
            models.Q(dcs_status__icontains=query) |
            models.Q(power_status__icontains=query) | 
            models.Q(rack_status__icontains=query) |
            models.Q(dcs_comment__icontains=query)
        )
    else:
        filtered_requests = dcs_requests  # If no query, display all DCS requests

    # Count requests by status
    yet_to_work_count = filtered_requests.filter(dcs_status='Yet To Work').count()
    not_required_count = filtered_requests.filter(dcs_status='Not Required').count()
    in_progress_count = filtered_requests.filter(dcs_status='In Progress').count()
    
    not_yet_started_count = filtered_requests.filter(dcs_status='Not yet Started').count()
    completed_count = filtered_requests.filter(dcs_status='Completed').count()
    cancelled_count = filtered_requests.filter(dcs_status='Cancelled').count()
    rows_count = CableMatrixModel.objects.count()
    context = {
        'filtered_requests': filtered_requests,
        'query': query,  # Pass the query back to the template to maintain input value
        'in_progress_count': in_progress_count + not_required_count + yet_to_work_count,
        'completed_count': completed_count,
        'not_yet_started_count': not_yet_started_count,
        'cancelled_count': cancelled_count,
        'rows_count': rows_count
    }

    return render(request, 'cable_matrix/phase1/dcs_request.html', context)

def edit_dcs_request(request, pk):
    cb_form = get_object_or_404(CableMatrixModel, pk=pk)
    if request.method == 'POST':
        form = DCSRequestForm(request.POST, instance=cb_form)
        if form.is_valid():
            form.save()
            messages.success(request, 'DCS Request updated successfully!')
            return redirect('dcs_request')
        # else:
        #     messages.error(request, 'Please correct the errors below.')
    else:
        form = DCSRequestForm(instance=cb_form)

    context = {
        'form': form
    }

    return render(request, 'cable_matrix/phase1/edit_dcs_request.html', context)

def edit_dcs_request_copy(request, pk):
    cb_form = get_object_or_404(CableMatrixModel, pk=pk)
    if request.method == 'POST':
        form = DCSRequestForm(request.POST, instance=cb_form)
        if form.is_valid():
            form.save()
            messages.success(request, 'DCS Request updated successfully!')
            return redirect('device_detail', pk)
        # else:
        #     messages.error(request, 'Please correct the errors below.')
    else:
        form = DCSRequestForm(instance=cb_form)

    context = {
        'form': form
    }

    return render(request, 'cable_matrix/phase1/edit_dcs_request_copy.html', context)


def cable_trace(request):
    query = request.GET.get('q', '')  # Get the search query from the URL parameter 'q'
    cable_trace = CableMatrixModel.objects.all()  # Query all DCS requests

    if query:
        # Filter Cable Trace based on the search query
        filtered_requests = cable_trace.filter(
            models.Q(newdevice__icontains=query) |
            models.Q(olddevice__icontains=query) |
            models.Q(cable_trace_requested_date__icontains=query) |
            models.Q(cable_trace_received_date__icontains=query) |
            models.Q(tickets_required__icontains=query) |
            models.Q(tickets_requested_date__icontains=query) |
            models.Q(tickets_requested_id__icontains=query) |
            models.Q(tickets_closed_date__icontains=query) |
            models.Q(cable_trace_status__icontains=query) |
            models.Q(cable_trace_comment__icontains=query)
        )
    else:
        filtered_requests = cable_trace  # If no query, display all DCS requests

    # Count requests by status
    yet_to_work_count = filtered_requests.filter(cable_trace_status='Yet To Work').count()
    not_required_count = filtered_requests.filter(cable_trace_status='Not Required').count()
    in_progress_count = filtered_requests.filter(cable_trace_status='In Progress').count()
    
    not_yet_started_count = filtered_requests.filter(cable_trace_status='Not yet Started').count()
    completed_count = filtered_requests.filter(cable_trace_status='Completed').count()
    cancelled_count = filtered_requests.filter(cable_trace_status='Cancelled').count()
    rows_count = CableMatrixModel.objects.count()
    
    context = {
        'filtered_requests': filtered_requests,
        'query': query,
        'in_progress_count': in_progress_count + not_required_count + yet_to_work_count,
        'completed_count': completed_count,
        'not_yet_started_count': not_yet_started_count,
        'cancelled_count': cancelled_count,
        'rows_count': rows_count
    }

    return render(request, 'cable_matrix/phase2/cable_trace.html', context)

def edit_cable_trace(request, pk):
    try:
        cb_form = get_object_or_404(CableMatrixModel, pk=pk)
        if request.method == 'POST':
            form = CableTraceForm(request.POST, instance=cb_form)
            # print(form)
            if form.is_valid():
                form.save()
                messages.success(request, 'Updated successfully!')
                return redirect('cable_trace')
            else:
                messages.error(request, 'Please correct the errors below.')
        else:
            form = CableTraceForm(instance=cb_form)

    except Exception as e:
        messages.error(request, f"Error editing Cable Trace form: {str(e)}")

    context = {
        'form': form
    }
    return render(request, 'cable_matrix/phase2/edit_cable_trace.html', context)

def edit_cable_trace_copy(request, pk):
    try:
        cb_form = get_object_or_404(CableMatrixModel, pk=pk)
        if request.method == 'POST':
            form = CableTraceForm(request.POST, instance=cb_form)
            print(form)
            if form.is_valid():
                form.save()
                messages.success(request, 'Updated successfully!')
                return redirect('device_detail', pk)
            else:
                messages.error(request, 'Please correct the errors below.')
        else:
            form = CableTraceForm(instance=cb_form)

    except Exception as e:
        messages.error(request, f"Error editing Cable Trace form: {str(e)}")

    context = {
        'form': form
    }
    return render(request, 'cable_matrix/phase2/edit_cable_trace_copy.html', context)



def network_design(request):
    query = request.GET.get('q', '')  # Get the search query from the URL parameter 'q'
    network_design = CableMatrixModel.objects.all()  # Query all DCS requests

    if query:
        # Filter DCS requests based on the search query
        filtered_requests = network_design.filter(
            models.Q(newdevice__icontains=query) |
            models.Q(olddevice__icontains=query) |
            models.Q(network_design_start_date__icontains=query) |
            models.Q(network_design_close_date__icontains=query) |
            models.Q(network_design_status__icontains=query)
        )
    else:
        filtered_requests = network_design  # If no query, display all DCS requests

    # Count requests by status
    yet_to_work_count = filtered_requests.filter(network_design_status='Yet To Work').count()
    not_required_count = filtered_requests.filter(network_design_status='Not Required').count()
    in_progress_count = filtered_requests.filter(network_design_status='In Progress').count()
    
    not_yet_started_count = filtered_requests.filter(network_design_status='Not yet Started').count()
    completed_count = filtered_requests.filter(network_design_status='Completed').count()
    cancelled_count = filtered_requests.filter(network_design_status='Cancelled').count()
    rows_count = CableMatrixModel.objects.count()
    context = {
        'filtered_requests': filtered_requests,
        'query': query,  # Pass the query back to the template to maintain input value
        'in_progress_count': in_progress_count + not_required_count + yet_to_work_count,
        'completed_count': completed_count,
        'not_yet_started_count': not_yet_started_count,
        'cancelled_count': cancelled_count,
        'rows_count': rows_count
    }
    
    return render(request, 'cable_matrix/phase3/network_design.html', context)

def edit_network_design(request, pk):
    cb_form = get_object_or_404(CableMatrixModel, pk=pk)
    if request.method == 'POST':
        form = NetworkDesignForm(request.POST, instance=cb_form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Network Design updated successfully!')
            return redirect('network_design')
    else:
        form = NetworkDesignForm(instance=cb_form)

    context = {
        'form': form
    }

    return render(request, 'cable_matrix/phase3/edit_network_design.html', context)

def edit_network_design_copy(request, pk):
    cb_form = get_object_or_404(CableMatrixModel, pk=pk)
    if request.method == 'POST':
        form = NetworkDesignForm(request.POST, instance=cb_form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Network Design updated successfully!')
            return redirect('device_detail', pk)
    else:
        form = NetworkDesignForm(instance=cb_form)

    context = {
        'form': form
    }

    return render(request, 'cable_matrix/phase3/edit_network_design_copy.html', context)


def cm(request):
    query = request.GET.get('q', '')  # Get the search query from the URL parameter 'q'
    cm = CableMatrixModel.objects.all()  # Query all DCS requests

    if query:
        # Filter DCS requests based on the search query
        filtered_requests = cm.filter(
            models.Q(newdevice__icontains=query) |
            models.Q(olddevice__icontains=query) |
            models.Q(cable_matrix_started_date__icontains=query) |
            models.Q(cable_matrix_status__icontains=query) |
            models.Q(cable_matrix_completed_date__icontains=query) |
            models.Q(cable_matrix_comment__icontains=query)
        )
    else:
        filtered_requests = cm  # If no query, display all DCS requests

    # Count requests by status
    yet_to_work_count = filtered_requests.filter(cable_matrix_status='Yet To Work').count()
    not_required_count = filtered_requests.filter(cable_matrix_status='Not Required').count()
    in_progress_count = filtered_requests.filter(cable_matrix_status='In Progress').count()
    
    not_yet_started_count = filtered_requests.filter(cable_matrix_status='Not yet Started').count()
    completed_count = filtered_requests.filter(cable_matrix_status='Completed').count()
    cancelled_count = filtered_requests.filter(cable_matrix_status='Cancelled').count()
    rows_count = CableMatrixModel.objects.count()
    context = {
        'filtered_requests': filtered_requests,
        'query': query,  # Pass the query back to the template to maintain input value
        'in_progress_count': in_progress_count + not_required_count + yet_to_work_count,
        'completed_count': completed_count,
        'not_yet_started_count': not_yet_started_count,
        'cancelled_count': cancelled_count,
        'rows_count': rows_count
    }

    return render(request, 'cable_matrix/phase4/cm.html', context)

def edit_cm(request, pk):
    cb_form = get_object_or_404(CableMatrixModel, pk=pk)
    if request.method == 'POST':
        form = cmForm(request.POST, instance=cb_form)
        if form.is_valid():
            form.save()
            messages.success(request, 'DCS Request updated successfully!')
            return redirect('cm')
    else:
        form = cmForm(instance=cb_form)

    context = {
        'form': form
    }

    return render(request, 'cable_matrix/phase4/edit_cm.html', context)

def edit_cm_copy(request, pk):
    cb_form = get_object_or_404(CableMatrixModel, pk=pk)
    if request.method == 'POST':
        form = cmForm(request.POST, instance=cb_form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cable Matrix form updated successfully!')
            return redirect('device_detail', pk)
        # else:
        #     messages.error(request, 'Please correct the errors below.')
    else:
        form = cmForm(instance=cb_form)

    context = {
        'form': form
    }

    return render(request, 'cable_matrix/phase4/edit_cm_copy.html', context)


def dis(request):
    query = request.GET.get('q', '')  # Get the search query from the URL parameter 'q'
    dis = CableMatrixModel.objects.all()  # Query all DCS requests

    if query:
        # Filter DCS requests based on the search query
        filtered_requests = dis.filter(
            models.Q(newdevice__icontains=query) |
            models.Q(olddevice__icontains=query) |
            models.Q(requested_date__icontains=query) |
            models.Q(request_id__icontains=query) |
            models.Q(approved_date__icontains=query) |
            models.Q(dcs_status__icontains=query) |
            models.Q(power_status__icontains=query) | 
            models.Q(rack_status__icontains=query) |
            models.Q(dcs_comment__icontains=query)
        )
    else:
        filtered_requests = dis  # If no query, display all DCS requests

    # Count requests by status
    yet_to_work_count = filtered_requests.filter(device_installation_status='Yet To Work').count()
    not_required_count = filtered_requests.filter(device_installation_status='Not Required').count()
    in_progress_count = filtered_requests.filter(device_installation_status='In Progress').count()
    
    not_yet_started_count = filtered_requests.filter(device_installation_status='Not yet Started').count()
    completed_count = filtered_requests.filter(device_installation_status='Completed').count()
    cancelled_count = filtered_requests.filter(device_installation_status='Cancelled').count()
    rows_count = CableMatrixModel.objects.count()
    context = {
        'filtered_requests': filtered_requests,
        'query': query,  # Pass the query back to the template to maintain input value
        'in_progress_count': in_progress_count + not_required_count + yet_to_work_count,
        'completed_count': completed_count,
        'not_yet_started_count': not_yet_started_count,
        'cancelled_count': cancelled_count,
        'rows_count': rows_count
    }

    return render(request, 'cable_matrix/phase5/dis.html', context)

def edit_dis(request, pk):
    cb_form = get_object_or_404(CableMatrixModel, pk=pk)
    if request.method == 'POST':
        form = deviceInstallationForm(request.POST, instance=cb_form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Device Installation Status updated successfully!')
            return redirect('dis')
    else:
        form = deviceInstallationForm(instance=cb_form)

    context = {
        'form': form
    }

    return render(request, 'cable_matrix/phase5/edit_dis.html', context)

def edit_dis_copy(request, pk):
    cb_form = get_object_or_404(CableMatrixModel, pk=pk)
    if request.method == 'POST':
        form = deviceInstallationForm(request.POST, instance=cb_form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Device Installation Status updated successfully!')
            return redirect('device_detail', pk)
    else:
        form = deviceInstallationForm(instance=cb_form)

    context = {
        'form': form
    }

    return render(request, 'cable_matrix/phase5/edit_dis_copy.html', context)

def port_assign(request):
    query = request.GET.get('q', '')  # Get the search query from the URL parameter 'q'
    port_assignment = CableMatrixModel.objects.all()  # Query all DCS requests

    if query:
        # Filter DCS requests based on the search query
        filtered_requests = port_assignment.filter(
            models.Q(newdevice__icontains=query) |
            models.Q(olddevice__icontains=query) |
            models.Q(port_tickets_required__icontains=query) |
            models.Q(port_tickets_requested_date__icontains=query) |
            models.Q(port_tickets_requested_id__icontains=query) |
            models.Q(port_assignment_status__icontains=query) |
            models.Q(port_assignment_comment__icontains=query)
            
        )
    else:
        filtered_requests = port_assignment  # If no query, display all DCS requests

    # Count requests by status
    yet_to_work_count = filtered_requests.filter(dcs_status='Yet To Work').count()
    not_required_count = filtered_requests.filter(dcs_status='Not Required').count()
    in_progress_count = filtered_requests.filter(dcs_status='In Progress').count()
    
    not_yet_started_count = filtered_requests.filter(dcs_status='Not yet Started').count()
    completed_count = filtered_requests.filter(dcs_status='Completed').count()
    cancelled_count = filtered_requests.filter(dcs_status='Cancelled').count()
    rows_count = CableMatrixModel.objects.count()
    context = {
        'filtered_requests': filtered_requests,
        'query': query,  # Pass the query back to the template to maintain input value
        'in_progress_count': in_progress_count + not_required_count + yet_to_work_count,
        'completed_count': completed_count,
        'not_yet_started_count': not_yet_started_count,
        'cancelled_count': cancelled_count,
        'rows_count': rows_count
    }

    return render(request, 'cable_matrix/phase6/port_assignment.html', context)

def edit_port_assign(request, pk):
    cb_form = get_object_or_404(CableMatrixModel, pk=pk)
    if request.method == 'POST':
        form = portAssignmentForm(request.POST, instance=cb_form)
        if form.is_valid():
            form.save()
            messages.success(request, 'port_assignment updated successfully!')
            return redirect('port_assign')
        # else:
        #     messages.error(request, 'Please correct the errors below.')
    else:
        form = portAssignmentForm(instance=cb_form)

    context = {
        'form': form
    }

    return render(request, 'cable_matrix/phase6/edit_port_assignment.html', context)

def edit_port_assign_copy(request, pk):
    cb_form = get_object_or_404(CableMatrixModel, pk=pk)
    if request.method == 'POST':
        form = portAssignmentForm(request.POST, instance=cb_form)
        if form.is_valid():
            form.save()
            messages.success(request, 'port_assignment updated successfully!')
            return redirect('device_detail', pk)
        # else:
        #     messages.error(request, 'Please correct the errors below.')
    else:
        form = portAssignmentForm(instance=cb_form)

    context = {
        'form': form
    }

    return render(request, 'cable_matrix/phase6/edit_port_assignment_copy.html', context)


def cable_measurement(request):
    query = request.GET.get('q', '')  # Get the search query from the URL parameter 'q'
    cable_measurement = CableMatrixModel.objects.all()  # Query all DCS requests

    if query:
        # Filter DCS requests based on the search query
        filtered_requests = cable_measurement.filter(
            models.Q(newdevice__icontains=query) |
            models.Q(olddevice__icontains=query) |
            models.Q(cable_measurement_tickets_required__icontains=query) |
            models.Q(cable_measurement_tickets_requested_date__icontains=query) |
            models.Q(cable_measurement_tickets_requested_id__icontains=query) |
            models.Q(cable_measurement_assignment_status__icontains=query) |
            models.Q(cable_measurement_assignment_comment__icontains=query)
            
        )
    else:
        filtered_requests = cable_measurement  # If no query, display all DCS requests

    # Count requests by status
    yet_to_work_count = filtered_requests.filter(dcs_status='Yet To Work').count()
    not_required_count = filtered_requests.filter(dcs_status='Not Required').count()
    in_progress_count = filtered_requests.filter(dcs_status='In Progress').count()
    
    not_yet_started_count = filtered_requests.filter(dcs_status='Not yet Started').count()
    completed_count = filtered_requests.filter(dcs_status='Completed').count()
    cancelled_count = filtered_requests.filter(dcs_status='Cancelled').count()
    rows_count = CableMatrixModel.objects.count()
    context = {
        'filtered_requests': filtered_requests,
        'query': query,  # Pass the query back to the template to maintain input value
        'in_progress_count': in_progress_count + not_required_count + yet_to_work_count,
        'completed_count': completed_count,
        'not_yet_started_count': not_yet_started_count,
        'cancelled_count': cancelled_count,
        'rows_count': rows_count
    }

    return render(request, 'cable_matrix/phase7/cable_measurement.html', context)

def edit_cable_measurement(request, pk):
    cb_form = get_object_or_404(CableMatrixModel, pk=pk)
    if request.method == 'POST':
        form = cableMeasurementForm(request.POST, instance=cb_form)
        if form.is_valid():
            form.save()
            messages.success(request, 'cable_measurement updated successfully!')
            return redirect('cable_measurement')
        # else:
        #     messages.error(request, 'Please correct the errors below.')
    else:
        form = cableMeasurementForm(instance=cb_form)

    context = {
        'form': form
    }

    return render(request, 'cable_matrix/phase7/edit_cable_measurement.html', context)

def edit_cable_measurement_copy(request, pk):
    cb_form = get_object_or_404(CableMatrixModel, pk=pk)
    if request.method == 'POST':
        form = cableMeasurementForm(request.POST, instance=cb_form)
        if form.is_valid():
            form.save()
            messages.success(request, 'cable_measurement updated successfully!')
            return redirect('device_detail', pk)
        # else:
        #     messages.error(request, 'Please correct the errors below.')
    else:
        form = cableMeasurementForm(instance=cb_form)

    context = {
        'form': form
    }

    return render(request, 'cable_matrix/phase7/edit_cable_measurement_copy.html', context)




