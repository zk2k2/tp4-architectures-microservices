"""
Document Service - Gestion centralisée des documents
Stockage: S3/MinIO
"""

class DocumentService:
    """Service de gestion documentaire"""

    def __init__(self, storage_client):
        self.storage_client = storage_client  # S3/MinIO client

    def upload_document(self, file_name, file_type, content):
        """
        Upload un document sur le stockage objet
        Retourne: document_id
        """
        pass

    def get_document(self, document_id):
        """Récupère un document par ID"""
        pass

    def delete_document(self, document_id):
        """Supprime un document"""
        pass

    def list_documents_for_application(self, application_id):
        """Liste tous les documents d'une demande"""
        pass


class Document:
    """Métadonnées d'un document"""
    def __init__(self):
        self.id = None
        self.file_name = None
        self.file_type = None  # PDF, JPEG, PNG
        self.size_bytes = None
        self.storage_path = None
        self.uploaded_at = None
        self.application_id = None
