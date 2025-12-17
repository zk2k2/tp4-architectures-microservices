"""
Commercial Service - Évaluation commerciale
Utilise OCR pour extraire données des documents
"""

class CommercialService:
    """Service d'évaluation de l'éligibilité"""

    def __init__(self, ocr_client, event_publisher):
        self.ocr_client = ocr_client
        self.event_publisher = event_publisher

    def handle_application_submitted(self, event):
        """
        Consomme ApplicationSubmittedEvent
        1. Récupère les documents
        2. Utilise OCR pour extraire revenus, situation professionnelle
        3. Calcule l'éligibilité et score initial
        4. Publie CommercialApproved ou CommercialRejected
        """
        pass

    def calculate_eligibility(self, monthly_income, requested_amount, loan_duration):
        """
        Vérifie éligibilité
        Règle: remboursement mensuel < 33% des revenus
        """
        pass

    def calculate_initial_score(self, income, employment_status, years_employed):
        """
        Calcule score commercial initial (0-100)
        Facteurs: revenus, stabilité emploi, dettes actuelles
        """
        pass


class OCRServiceClient:
    """Client pour communiquer avec OCR Service"""

    def extract_income_data(self, document_id):
        """Extrait revenus depuis fiche de paie"""
        pass

    def extract_bank_statement(self, document_id):
        """Extrait données bancaires depuis relevé"""
        pass


class CommercialEvaluation:
    """Résultat de l'évaluation commerciale"""
    def __init__(self):
        self.application_id = None
        self.monthly_income = None
        self.employment_status = None
        self.initial_score = None  # 0-100
        self.is_eligible = None
        self.reject_reason = None
