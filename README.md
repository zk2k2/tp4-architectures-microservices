# Architecture Microservices - Module de Gestion de Prêts Bancaires

## Vue d'ensemble

Prototype architectural (non fonctionnel) présentant la conception d'un système de gestion de prêts bancaires basé sur une architecture microservices événementielle.

**Note**: Ce projet est un **showcase architectural** montrant la structure, les classes et les patterns de conception. Il n'est pas destiné à être exécuté.

## Structure du Projet

```
tp4-architectures-microservices/
├── services/
│   ├── application/          # Service de gestion des demandes
│   │   ├── models.py         # Entités (LoanApplication)
│   │   ├── service.py        # Logique métier
│   │   └── events.py         # Événements publiés
│   │
│   ├── commercial/           # Service d'évaluation commerciale
│   │   └── service.py        # Scoring initial + OCR
│   │
│   ├── risk/                 # Service de gestion des risques
│   │   └── service.py        # Scoring final + Banque Centrale
│   │
│   ├── credit/               # Service de génération documentaire
│   │   └── service.py        # Contrat + Amortissement
│   │
│   ├── notification/         # Service de notification
│   │   └── service.py        # Email/SMS
│   │
│   ├── document/             # Service de gestion documentaire
│   │   └── service.py        # Stockage S3/MinIO
│   │
│   └── ocr/                  # Service OCR partagé
│       └── service.py        # Extraction données documents
│
├── infrastructure/
│   └── docker-compose.yml    # Infrastructure (DB, RabbitMQ, MinIO)
│
└── README.md
```

## Microservices

### 1. Application Service
**Responsabilité**: Gestion du cycle de vie des demandes de prêt

**Classes clés**:
- `LoanApplication`: Entité demande
- `ApplicationService`: Logique métier
- `ApplicationSubmittedEvent`: Événement déclenché

**Workflow**:
1. Reçoit soumission client via API Gateway
2. Upload documents → Document Service
3. Sauvegarde demande (status: PENDING)
4. Publie `ApplicationSubmittedEvent` → RabbitMQ

---

### 2. Commercial Service
**Responsabilité**: Évaluation de l'éligibilité et scoring initial

**Workflow**:
1. Consomme `ApplicationSubmittedEvent`
2. Récupère documents → OCR Service
3. Extrait revenus, situation professionnelle
4. Calcule éligibilité (règle: remboursement < 33% revenus)
5. Génère score initial (0-100)
6. Publie `CommercialApproved` ou `CommercialRejected`

---

### 3. Risk Management Service
**Responsabilité**: Analyse de risque approfondie et scoring final

**Workflow**:
1. Consomme `CommercialApprovedEvent`
2. Consulte Banque Centrale (engagements cachés)
3. Calcule ratio d'endettement
4. Génère score final (0-100)
5. Publie `RiskApproved` ou `RiskRejected`

**Intégration externe**: API Banque Centrale

---

### 4. Credit Service
**Responsabilité**: Génération des documents contractuels

**Workflow**:
1. Consomme `RiskApprovedEvent`
2. Génère contrat de crédit (PDF)
3. Génère tableau d'amortissement
4. Stocke documents → Document Service
5. Publie `CreditGeneratedEvent`

---

### 5. Notification Service
**Responsabilité**: Communication avec le client (Email/SMS)

---

### 6. Document Service
**Responsabilité**: Gestion centralisée des documents (MinIO/S3)

---

### 7. OCR Service
**Responsabilité**: Extraction de données depuis documents (Tesseract/AWS Textract)

---

## Patterns Architecturaux

### Event-Driven Architecture
- Communication asynchrone via RabbitMQ
- Découplage temporel entre services
- Résilience: retry automatique

**Flux d'événements**:
```
ApplicationSubmitted → Commercial Service
CommercialApproved → Risk Service
RiskApproved → Credit + Notification Services
CreditGenerated → Notification Service
```

### Database-per-Service
- Chaque service possède sa propre base de données
- Autonomie des équipes
- Scaling indépendant

### Shared Services
- OCR Service: Mutualisé entre Commercial et Risk
- Document Service: Accès centralisé aux documents

---

## Infrastructure

**Message Broker**: RabbitMQ
**Bases de données**: PostgreSQL (4 instances séparées)
**Stockage objet**: MinIO (dev) / S3 (prod)
**API Gateway**: Point d'entrée unique

Voir `infrastructure/docker-compose.yml` pour la configuration.

---

## Workflow Complet

```
Client → Application Service → [ApplicationSubmitted]
         ↓
Commercial Service → OCR → [CommercialApproved]
         ↓
Risk Service → Banque Centrale → [RiskApproved]
         ↓
Credit Service → [CreditGenerated]
         ↓
Notification Service → Email/SMS Client
```

---

## Choix d'Architecture

### Event-Driven
Workflow séquentiel sans besoin de réponse immédiate. Résilience et scalabilité.

### Database-per-Service
Autonomie des équipes, isolation des pannes.

### OCR Service séparé
Partagé, CPU-intensif, évolution technologique indépendante.

### Document Service centralisé
Sécurité uniforme, conformité RGPD.

---
