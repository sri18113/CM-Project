from django.db import models

class CableMatrixModel(models.Model):
    status_choices = [
        ('Completed', 'Completed'),
        ('In Progress', 'In Progress'),
        ('Not Required', 'Not Required'),
        ('Yet To Work', 'Yet To Work'),
        ('Not yet Started', 'Not yet Started'),
        ('Cancelled', 'Cancelled'),
    ]
    tickets_required_choices = [
        ('EMAIL', 'EMAIL'),
        ('ESS', 'ESS'),
        ('ITONS', 'ITONS'),
        ('AORTS', 'AORTS'),
    ]

    # Define all fields with max_length=100 as CharField
    requestor = models.CharField(max_length=100)
    requesttype = models.CharField(max_length=100)
    olddevice = models.CharField(max_length=100)
    oldmodel = models.CharField(max_length=100)
    rrd = models.DateField()
    ipn = models.CharField(max_length=100)
    cpn = models.CharField(max_length=100)
    pn = models.CharField(max_length=100)
    pm = models.CharField(max_length=100)
    newdevice = models.CharField(max_length=100)
    newmodel = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    clli = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)

    # DCS Request Phase fields
    requested_date = models.DateField(null=True, blank=True)
    request_id = models.CharField(max_length=100, default='NA', blank=True)
    approved_date = models.DateField(null=True, blank=True)
    dcs_status = models.CharField(max_length=20, choices=status_choices, null=True, blank=True)
    power_status = models.CharField(max_length=20, choices=status_choices, null=True, blank=True)
    rack_status = models.CharField(max_length=20, choices=status_choices, null=True, blank=True)
    dcs_comment = models.TextField(default='NA', blank=True)

    # Cable Trace Phase fields
    cable_trace_requested_date = models.DateField(null=True, blank=True)
    cable_trace_received_date = models.DateField(null=True, blank=True)
    
    tickets_required = models.CharField(max_length=20, choices=tickets_required_choices,  null=True, blank=True)
    tickets_requested_date = models.DateField(null=True, blank=True)
    tickets_requested_id = models.CharField(max_length=100, default='NA', blank=True)
    tickets_closed_date = models.DateField(null=True, blank=True)
    cable_trace_status = models.CharField(max_length=20, choices=status_choices,  null=True, blank=True)
    cable_trace_comment = models.TextField(null=True, default='NA', blank=True)

    # Network Design Phase fields
    network_design_start_date = models.DateField(null=True, blank=True)
    network_design_close_date = models.DateField(null=True, blank=True)
    network_design_status = models.CharField(max_length=20, choices=status_choices,  null=True, blank=True)
    network_design_comment = models.TextField(default='NA', blank=True)

    # Cable Matrix Phase fields
    cable_matrix_started_date = models.DateField(null=True, blank=True)
    cable_matrix_status = models.CharField(max_length=20, choices=status_choices,  null=True, blank=True)
    cable_matrix_completed_date = models.DateField(null=True, blank=True)
    cable_matrix_comment = models.TextField(default='NA', blank=True)

    # Device Installation Status
    device_installation_requested_date = models.DateField(null=True, blank=True)
    installation_tickets_requested_date = models.DateField(null=True, blank=True)
    installation_tickets_closed_date = models.DateField(null=True, blank=True)
    device_installation_completion_date = models.DateField(null=True, blank=True)
    installation_tickets_requested_id = models.CharField(max_length=100, default='NA', blank=True)
    installation_tickets_required = models.CharField(max_length=20, choices=tickets_required_choices,  null=True, blank=True)
    device_installation_status = models.CharField(max_length=20, choices=status_choices,  null=True, blank=True)
    installation_comment = models.TextField(default='NA', blank=True)

    #Port Assignment fields
    port_tickets_required = models.CharField(max_length=20, choices=tickets_required_choices,  null=True, blank=True)
    port_tickets_requested_date = models.DateField(null=True, blank=True)
    port_tickets_requested_id = models.CharField(max_length=100, default='NA', blank=True)
    port_tickets_closed_date = models.DateField(null=True, blank=True)
    port_assignment_status = models.CharField(max_length=20, choices=status_choices,  null=True, blank=True)
    port_assignment_comment = models.TextField(null=True, default='NA', blank=True)

    #Cable Measurement  
    cable_measurement_tickets_required = models.CharField(max_length=20, choices=tickets_required_choices,  null=True, blank=True)
    cable_measurement_tickets_requested_date = models.DateField(null=True, blank=True)
    cable_measurement_tickets_requested_id = models.CharField(max_length=100, default='NA', blank=True)
    cable_measurement_tickets_closed_date = models.DateField(null=True, blank=True)
    cable_measurement_assignment_status = models.CharField(max_length=20, choices=status_choices,  null=True, blank=True)
    cable_measurement_assignment_comment = models.TextField(null=True, default='NA', blank=True)


    # def save(self, *args, **kwargs):
    #     # Convert all CharField data to lowercase before saving
    #     self.requestor = self.requestor.lower()
    #     self.requesttype = self.requesttype.lower()
    #     self.olddevice = self.olddevice.lower()
    #     self.oldmodel = self.oldmodel.lower()
    #     # self.rrd = self.rrd.lower()
    #     self.ipn = self.ipn.lower()
    #     self.cpn = self.cpn.lower()
    #     self.pn = self.pn.lower()
    #     self.pm = self.pm.lower()
    #     self.newdevice = self.newdevice.lower()
    #     self.newmodel = self.newmodel.lower()
    #     self.location = self.location.lower()
    #     self.clli = self.clli.lower()
    #     self.domain = self.domain.lower()

    #     # Call the original save method
    #     super(CableMatrixModel, self).save(*args, **kwargs)

    def __str__(self):
        return f"Form Data for {self.requestor} - {self.pn}"




