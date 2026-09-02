# Partie 08 — Notions de cloud

Dernière partie des fondations. L'objectif ici n'est **pas** de devenir expert
cloud, mais de comprendre les concepts et de réussir à mettre ta petite
application en ligne, accessible depuis Internet. C'est la conclusion logique de
tout le parcours.

## Objectifs

À la fin, tu sauras :

- expliquer ce qu'est le cloud et son modèle économique ;
- distinguer VM et conteneur, et les grands types de services cloud ;
- déployer ton application conteneurisée sur un serveur distant.

## Ce que tu dois apprendre

1. **Le cloud, c'est quoi ?** L'idée de louer des ressources informatiques
   (serveurs, stockage, réseau) à la demande, plutôt que d'acheter et gérer ses
   propres machines. Le modèle « on paie ce qu'on utilise ».
2. **Les grands acteurs :** AWS, Microsoft Azure, Google Cloud (GCP), et des
   acteurs plus simples/abordables pour débuter (cherche des fournisseurs avec
   une offre gratuite pour étudiant).
3. **Les modèles de service :** IaaS, PaaS, SaaS — comprendre la différence
   (qui gère quoi).
4. **VM vs conteneur (rappel et approfondissement) :** une VM émule une machine
   complète ; un conteneur partage le noyau de l'hôte. Quand utiliser l'un ou
   l'autre.
5. **Déployer pour de vrai :**

   - louer/créer un petit serveur (une VM) chez un fournisseur ;
   - s'y connecter en **SSH** (partie 02 !) ;
   - y installer Docker ;
   - y faire tourner ton conteneur ;
   - ouvrir le bon **port** dans le pare-feu pour y accéder depuis Internet
     (parties 01 et 02 !).

## Recherches à faire

- « cloud computing expliqué simplement »
- « IaaS PaaS SaaS différence »
- « AWS Azure GCP comparaison débutant »
- « fournisseur cloud offre gratuite étudiant »
- « déployer une application docker sur un serveur »
- « se connecter en ssh à un serveur distant »
- « ouvrir un port firewall serveur »

> ⚠️ Attention aux coûts : sur les grandes plateformes, on peut vite payer sans
> le vouloir. Utilise les offres gratuites, mets des alertes de budget, et
> **éteins/supprime** ce que tu n'utilises plus.

## Exercices

Cette partie est surtout un **projet** pratique (voir ci-dessous). Avant de te
lancer, réponds d'abord dans ton `JOURNAL.md` :

1. Explique avec tes mots la différence entre IaaS, PaaS et SaaS, avec un
   exemple concret pour chacun.
2. Explique la différence entre une VM et un conteneur, et dans quel cas tu
   choisirais l'un plutôt que l'autre.

## Projet de la partie (le grand final)

Mets **en ligne** ton application conteneurisée de la partie 06 :

1. Crée un petit serveur chez un fournisseur cloud (offre gratuite).
2. Connecte-toi dessus en SSH.
3. Installe Docker sur le serveur.
4. Récupère ton projet (via Git !) et lance-le avec Docker / Docker Compose.
5. Ouvre le port nécessaire et vérifie que ton appli est accessible depuis ton
   navigateur, via l'IP publique du serveur.
6. Documente toute la démarche dans ton `JOURNAL.md` : chaque commande, chaque
   blocage, chaque solution.

C'est l'aboutissement de tout le guide : ton code, conteneurisé, versionné, et
tournant sur une machine distante que tu administres toi-même.

## Auto-évaluation

Sans notes :

- Qu'est-ce que le cloud et quel est son modèle économique ?
- Différence entre IaaS, PaaS et SaaS ?
- Différence entre une VM et un conteneur ?
- Quelles étapes pour rendre une appli Docker accessible depuis Internet ?

## Et après ?

Tu as posé toutes les fondations. La suite, c'est le **[niveau 2](../../niveau-2/)** :
Infrastructure as Code (Terraform, Ansible), orchestration (Kubernetes),
monitoring (Prometheus, Grafana), sécurité (DevSecOps), et approfondissement.
Ressources générales : [ressources/](../../ressources/).

Bravo d'être arrivé jusqu'ici. 🎓
