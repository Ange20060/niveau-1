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
