"""
Application Service - Entités
Gère les demandes de prêt
"""

class LoanApplication:
    """Entité représentant une demande de prêt"""
    def __init__(self):
        self.id = None
        self.application_number = None
        self.client_name = None
        self.client_email = None
        self.requested_amount = None
        self.loan_duration_months = None
        self.status = None  # PENDING, COMMERCIAL_REVIEW, RISK_ASSESSMENT, APPROVED, REJECTED
        self.document_ids = []
        self.submitted_at = None


class ApplicationRequest:
    """DTO pour soumission de demande"""
    def __init__(self):
        self.client_name = None
        self.client_email = None
        self.monthly_income = None
        self.requested_amount = None
        self.loan_duration_months = None
        self.documents = []  # Liste de documents uploadés
