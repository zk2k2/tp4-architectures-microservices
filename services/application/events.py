"""
Application Service - Événements
Pattern: Event-Driven Architecture
"""

class ApplicationSubmittedEvent:
    """Événement publié quand une demande est soumise"""
    def __init__(self):
        self.application_id = None
        self.application_number = None
        self.client_name = None
        self.requested_amount = None
        self.loan_duration_months = None
        self.document_ids = []
        self.timestamp = None


class ApplicationStatusChangedEvent:
    """Événement publié quand le statut change"""
    def __init__(self):
        self.application_id = None
        self.old_status = None
        self.new_status = None
        self.timestamp = None
