"""
Application Service - Logique métier
"""

class ApplicationService:
    """Service de gestion des demandes de prêt"""

    def __init__(self, repository, document_client, event_publisher):
        self.repository = repository
        self.document_client = document_client
        self.event_publisher = event_publisher

    def submit_application(self, request):
        """
        Soumet une nouvelle demande de prêt
        1. Valide les données
        2. Upload les documents via Document Service
        3. Sauvegarde la demande (status: PENDING)
        4. Publie l'événement ApplicationSubmitted
        """
        pass

    def get_application_status(self, application_id):
        """Récupère le statut d'une demande"""
        pass

    def update_status(self, application_id, new_status):
        """Met à jour le statut (appelé par événements)"""
        pass


class DocumentServiceClient:
    """Client pour communiquer avec Document Service"""

    def upload_documents(self, documents):
        """Upload des documents, retourne les IDs"""
        pass

    def get_document(self, document_id):
        """Récupère un document par ID"""
        pass
