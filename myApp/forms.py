from typing import Any
from django import forms
from .models import CableMatrixModel
from django.core.exceptions import ValidationError
from datetime import datetime
from django.utils.translation import gettext_lazy as _

class CableMatrixForm(forms.ModelForm):
    rrd = forms.DateField(input_formats=['%m/%d/%Y'],widget=forms.DateInput(format='%m/%d/%Y', attrs={'class':'date-input', 'placeholder':'MM/DD/YYYY'}))
    
    
    class Meta:
        model = CableMatrixModel
        fields = [
            'requestor',
            'requesttype',
            'olddevice',
            'oldmodel',
            'rrd',
            'ipn',
            'cpn',
            'pn',
            'pm',
            'newdevice',
            'newmodel',
            'location',
            'clli',
            'domain',
            'requested_date',
            'request_id',
            'approved_date',
            'dcs_status',
            'power_status',
            'rack_status',
            'dcs_comment',
            'cable_trace_requested_date',
            'cable_trace_received_date',
            'tickets_required',
            'tickets_requested_date',
            'tickets_requested_id',
            'tickets_closed_date',
            'cable_trace_status',
            'cable_trace_comment',
            'network_design_start_date',
            'network_design_close_date',
            'network_design_status',
            'network_design_comment',
            'cable_matrix_started_date',
            'cable_matrix_status',
            'cable_matrix_completed_date',
            'cable_matrix_comment'
        ]

class EditCableMatrixForm(forms.ModelForm):
    rrd = forms.DateField(input_formats=['%m/%d/%Y'],widget=forms.DateInput(format='%m/%d/%Y', attrs={'class':'date-input', 'placeholder':'MM/DD/YYYY'}))
    class Meta:
        model = CableMatrixModel
        fields = [
            'requestor',
            'requesttype',
            'olddevice',
            'oldmodel',
            'rrd',
            'ipn',
            'cpn',
            'pn',
            'pm',
            'newdevice',
            'newmodel',
            'location',
            'clli',
            'domain'
        ]
        

class DCSRequestForm(forms.ModelForm):
    class Meta:
        model = CableMatrixModel
        fields = ['olddevice', 'newdevice', 'requested_date', 'request_id', 'approved_date', 'dcs_status', 'power_status', 'rack_status', 'dcs_comment']

    requested_date = forms.DateField(
        input_formats=['%m/%d/%Y'],
        required=False,
        error_messages={
            'invalid': 'Enter valid date format is MM/DD/YYYY.'
        }
    )
    
    approved_date = forms.DateField(
        input_formats=['%m/%d/%Y'],
        required=False,
        error_messages={
            'invalid': 'Enter valid date format is MM/DD/YYYY.'
        }
    )
    
        
class CableTraceForm(forms.ModelForm):
    class Meta:
        model = CableMatrixModel
        fields = [
            'olddevice', 'newdevice', 'cable_trace_requested_date', 'cable_trace_received_date', 'tickets_required',
            'tickets_requested_date', 'tickets_requested_id', 'tickets_closed_date', 'cable_trace_status',
            'cable_trace_comment'
        ]
        
    cable_trace_requested_date = forms.DateField(
        input_formats=['%m/%d/%Y'],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'}),
        error_messages={
            'invalid': 'Enter valid date format MM/DD/YYYY.'
        }
    )
    
    cable_trace_received_date = forms.DateField(
        input_formats=['%m/%d/%Y'],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'}),
        error_messages={
            'invalid': 'Enter valid date format MM/DD/YYYY.'
        }
    )
    tickets_closed_date = forms.DateField(
        input_formats=['%m/%d/%Y'],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'}),
        error_messages={
            'invalid': 'Enter valid date format MM/DD/YYYY.'
        }
    )
    tickets_requested_date = forms.DateField(
        input_formats=['%m/%d/%Y'],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'}),
        error_messages={
            'invalid': 'Enter valid date format MM/DD/YYYY.'
        }
    )
    
    
        
class NetworkDesignForm(forms.ModelForm):
    class Meta:
        model = CableMatrixModel
        fields = [
            'olddevice', 'newdevice', 'network_design_start_date', 'network_design_close_date', 'network_design_status',
            'network_design_comment'
        ]
    
    network_design_start_date = forms.DateField(
        input_formats=['%m/%d/%Y'],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'}),
        error_messages={
            'invalid': 'Enter valid date format MM/DD/YYYY.'
        }
    )
    
    network_design_close_date = forms.DateField(
        input_formats=['%m/%d/%Y'],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'}),
        error_messages={
            'invalid': 'Enter valid date format MM/DD/YYYY.'
        }
    )

class cmForm(forms.ModelForm):
    class Meta:
        model = CableMatrixModel  
        fields = [
            'olddevice', 'newdevice', 'cable_matrix_started_date', 'cable_matrix_status', 'cable_matrix_completed_date',
            'cable_matrix_comment'
        ]
    
    cable_matrix_started_date = forms.DateField(
        input_formats=['%m/%d/%Y'],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'}),
        error_messages={
            'invalid': 'Enter valid date format MM/DD/YYYY.'
        }
    )
    
    cable_matrix_completed_date = forms.DateField(
        input_formats=['%m/%d/%Y'],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'}),
        error_messages={
            'invalid': 'Enter valid date format MM/DD/YYYY.'
        }
    )

class deviceInstallationForm(forms.ModelForm):
    class Meta:
        model = CableMatrixModel  
        fields = [
            'olddevice', 'newdevice', 'device_installation_requested_date', 'installation_tickets_required', 'installation_tickets_requested_date', 'installation_tickets_requested_id', 'installation_tickets_closed_date', 'device_installation_status', 'device_installation_completion_date', 'installation_comment'
        ]


class portAssignmentForm(forms.ModelForm):
    class Meta:
        model = CableMatrixModel  
        fields = [
            'olddevice', 'newdevice', 'port_tickets_required', 'port_tickets_requested_date', 'port_tickets_requested_id', 'port_tickets_closed_date', 'port_assignment_status', 'port_assignment_comment'
        ]


    port_tickets_requested_date = forms.DateField(
        input_formats=['%m/%d/%Y'],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'}),
        error_messages={
            'invalid': 'Enter valid date format MM/DD/YYYY.'
        }
    )
    
    port_tickets_closed_date = forms.DateField(
        input_formats=['%m/%d/%Y'],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'}),
        error_messages={
            'invalid': 'Enter valid date format MM/DD/YYYY.'
        }
    )


class cableMeasurementForm(forms.ModelForm):
    class Meta:
        model = CableMatrixModel  
        fields = [
            'olddevice', 'newdevice', 'cable_measurement_tickets_required', 'cable_measurement_tickets_requested_date', 'cable_measurement_tickets_requested_id', 'cable_measurement_tickets_closed_date', 'cable_measurement_assignment_status', 'cable_measurement_assignment_comment'
        ]


    cable_measurement_tickets_requested_date = forms.DateField(
        input_formats=['%m/%d/%Y'],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'}),
        error_messages={
            'invalid': 'Enter valid date format MM/DD/YYYY.'
        }
    )
    
    cable_measurement_tickets_closed_date = forms.DateField(
        input_formats=['%m/%d/%Y'],
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'}),
        error_messages={
            'invalid': 'Enter valid date format MM/DD/YYYY.'
        }
    )
    
     
    