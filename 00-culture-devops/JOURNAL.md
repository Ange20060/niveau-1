Le devOps est celui là qui s'occupe du deploiement et du bon fonctionnement des applocation oou des sites


# Que se passe-t-il quand je tape `https://exemple.com` ?

Quand je tape `https://exemple.com` dans mon navigateur, plusieurs étapes se déroulent avant que la page s'affiche.

```text
Je tape https://exemple.com
          │
          ▼
        DNS
          │
          │ trouve l'adresse IP
          ▼
   Adresse IP du serveur
          │
          │ connexion au port 443
          ▼
   Client ───────────► Serveur
          │
          │ requête HTTP
          ▼
   Serveur traite la demande
          │
          │ réponse HTTP
          │ + code de statut
          ▼
       Navigateur
          │
          ▼
    Page affichée
```

### 1. Le DNS trouve l'adresse IP

Le navigateur connaît le nom `exemple.com`, mais les ordinateurs communiquent entre eux grâce aux **adresses IP**.

Le **DNS** (Domain Name System) sert donc à traduire le nom de domaine en adresse IP.

```text
exemple.com
     ↓
adresse IP du serveur
```

Le navigateur peut alors savoir à quel serveur envoyer la demande.

### 2. Le navigateur utilise un port

Pour communiquer avec le serveur, il faut également utiliser un **port**.

Comme l'adresse commence par `https://`, le port utilisé par défaut est **443**.

```text
Adresse IP + port 443
```

Le port permet notamment de déterminer quel service réseau doit recevoir la communication.

### 3. Le client communique avec le serveur

Le navigateur joue le rôle de **client**.

Le serveur qui héberge le site joue le rôle de **serveur**.

```text
Navigateur (client)
        │
        │ demande
        ▼
Serveur web
```

Le client demande une ressource au serveur et le serveur lui répond.

### 4. Le navigateur envoie une requête HTTP

Une fois la connexion établie, le navigateur envoie une **requête HTTP** au serveur.

Par exemple, il peut demander la page d'accueil avec une requête `GET`.

```text
GET / HTTP/...
Host: exemple.com
```

Cela signifie essentiellement :

> « Donne-moi la ressource située à la racine du site `exemple.com`. »

### 5. Le serveur renvoie une réponse

Le serveur traite la requête puis renvoie une **réponse HTTP**.

Elle contient notamment un **code de statut**.

Par exemple :

```text
HTTP/1.1 200 OK
```

Le code `200` signifie que la demande a réussi.

La réponse contient également les données demandées, par exemple du HTML :

```text
HTTP/1.1 200 OK
Content-Type: text/html

<html>
    ...
</html>
```

Le navigateur reçoit ce HTML et construit ensuite la page visible à l'écran.

### 6. Pourquoi HTTPS et pas HTTP ?

`HTTPS` signifie **HTTP Secure**.

La différence principale est que les échanges HTTP sont protégés par **TLS** lorsqu'on utilise HTTPS.

Cela permet notamment de **chiffrer les données échangées** entre le client et le serveur et de vérifier l'identité du serveur grâce à son certificat.

```text
HTTP
Client ───────────────► Serveur
       données non chiffrées

HTTPS
Client ═══════════════► Serveur
       données chiffrées
```

HTTPS utilise généralement le **port 443**, tandis que HTTP utilise généralement le **port 80**.

### Résumé

Quand je tape `https://exemple.com` :

1. Le **DNS** transforme `exemple.com` en **adresse IP**.
2. Le navigateur se connecte au serveur sur le **port 443**.
3. Le navigateur est le **client** et le serveur héberge le site.
4. Le client envoie une **requête HTTP** pour demander la page.
5. Le serveur renvoie une **réponse HTTP** avec un **code de statut**, par exemple `200 OK`, et le contenu de la page.
6. Comme il s'agit de **HTTPS**, les échanges sont protégés par **TLS**.
7. Le navigateur interprète le contenu reçu et **affiche la page**.


# 05 EXO1

# Exercice — Disséquer une application de commande de repas

## 1. Front-end

Le front-end est la partie visible par l'utilisateur dans son navigateur ou son application.

Trois exemples d'écrans :

1. **Écran d'accueil** : affiche les restaurants disponibles, les catégories et les plats.
2. **Écran du restaurant** : affiche les plats, leurs prix, leurs descriptions et permet de les ajouter au panier.
3. **Écran de commande** : affiche le panier, l'adresse de livraison, le prix total et le bouton « Commander ».

Le front-end permet donc à l'utilisateur d'interagir avec l'application et d'envoyer des demandes au back-end.

## 2. Back-end

Le back-end est la partie qui traite les demandes et applique les règles de l'application.

Exemples de traitements :

1. Vérifier qu'un restaurant est ouvert avant d'accepter une commande.
2. Calculer et vérifier le montant total d'une commande.
3. Enregistrer la commande et mettre à jour son statut.

Le back-end communique également avec la base de données et renvoie les résultats au front-end, généralement sous forme de JSON.

## 3. Base de données

La base de données conserve les informations nécessaires au fonctionnement de l'application.

Elle pourrait contenir notamment :

* les utilisateurs et leurs informations ;
* les restaurants ;
* les plats et leurs prix ;
* les commandes ;
* les produits contenus dans chaque commande ;
* les adresses de livraison ;
* les paiements et leurs statuts.

## 4. Aller-retour : cliquer sur « Commander »

Lorsqu'un utilisateur clique sur « Commander », plusieurs étapes se produisent.

```text
Utilisateur
    ↓
Front-end
    ↓
Requête HTTP
    ↓
Back-end
    ↓
Vérifications
    ↓
Base de données
    ↓
Enregistrement de la commande
    ↓
Réponse du back-end
    ↓
Front-end
    ↓
Affichage de la confirmation
```

Plus précisément :

1. L'utilisateur clique sur « Commander » dans le front-end.
2. Le front-end rassemble les informations nécessaires : utilisateur, restaurant, plats, adresse, etc.
3. Il envoie une requête HTTP au back-end, par exemple avec `POST /api/orders`.
4. Le back-end reçoit la requête.
5. Il vérifie les informations et applique les règles métier : restaurant ouvert, plats disponibles, utilisateur autorisé, prix cohérents, etc.
6. Si tout est correct, le back-end enregistre la commande dans la base de données.
7. La base de données confirme l'enregistrement.
8. Le back-end renvoie une réponse HTTP au front-end, généralement avec les informations de la commande et un code de statut comme `201 Created`.
9. Le front-end reçoit la réponse et affiche la confirmation à l'utilisateur.

## Où appliquer la règle « restaurant fermé » ?

La règle doit être appliquée **côté back-end**, même si le front-end peut également l'afficher pour informer l'utilisateur.

Le front-end n'est pas suffisamment fiable pour garantir une règle de sécurité ou métier, car son code est exécuté du côté de l'utilisateur et peut être modifié ou contourné.

Le back-end est donc la source de vérité.

Par exemple :

```text
Front-end
Restaurant fermé
→ désactive « Commander »

          MAIS

Back-end
Restaurant fermé ?
→ refuse la commande
```

Même si quelqu'un contourne le blocage du front-end et envoie directement une requête HTTP, le back-end doit refuser la commande.

## Pourquoi séparer front-end, back-end et base de données ?

La séparation permet de donner une responsabilité différente à chaque couche.

* **Front-end** : gérer l'interface et les interactions avec l'utilisateur.
* **Back-end** : gérer la logique métier, les règles et les traitements.
* **Base de données** : stocker durablement les informations.

Cette séparation rend l'application plus facile à développer, tester, maintenir et faire évoluer.

Par exemple, on peut remplacer le front-end React par une application mobile sans devoir réécrire toute la logique du back-end.

La séparation permet donc d'éviter de mélanger l'interface, la logique métier et le stockage des données dans un seul bloc difficile à maintenir.
