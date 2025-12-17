"""
Notification Service - Notifications client
Multi-canal: Email, SMS
"""

class NotificationService:
    """Service de notification client"""

    def __init__(self, email_provider, sms_provider):
        self.email_provider = email_provider
        self.sms_provider = sms_provider

    def handle_risk_approved(self, event):
        """Notifie le client que sa demande est approuvée"""
        pass

    def handle_risk_rejected(self, event):
        """Notifie le client que sa demande est rejetée"""
        pass

    def handle_credit_generated(self, event):
        """Notifie le client que ses documents sont prêts"""
        pass

    def send_email(self, to, subject, body):
        """Envoie un email"""
        pass

    def send_sms(self, phone_number, message):
        """Envoie un SMS"""
        pass
