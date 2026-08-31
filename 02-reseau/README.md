# Partie 02 — Les bases du réseau

On ne peut pas déployer une application sans comprendre comment les machines se
parlent. Pas besoin de devenir expert réseau : il te faut les concepts
essentiels, bien compris.

## Objectifs

À la fin, tu sauras :

- expliquer ce qui se passe quand on ouvre une page web ;
- comprendre IP, ports, DNS, client/serveur ;
- lire un échange HTTP et ses codes de statut ;
- te connecter à une machine distante en SSH.

## Ce que tu dois apprendre

1. **Client / serveur.** Le modèle de base : un client demande, un serveur
   répond. Ton navigateur est un client.
2. **Adresse IP.** L'« adresse postale » d'une machine sur un réseau. Notion
   d'IPv4 (ex. `192.168.1.10`), d'IP locale vs publique, de `localhost`
   (`127.0.0.1`).
3. **Ports.** Une même machine peut faire tourner plusieurs services ; le port
   dit « à quel service je m'adresse ». Ports connus : 80 (HTTP), 443 (HTTPS),
   22 (SSH). C'est le fameux `IP:port`.
4. **DNS.** Le « répertoire » qui traduit un nom (`exemple.com`) en adresse IP.
   Personne ne retient des IP, on retient des noms.
5. **HTTP / HTTPS.** Le langage du web : une **requête** (méthode `GET`,
   `POST`...) et une **réponse** avec un **code de statut** (200 = ok, 404 =
   pas trouvé, 500 = erreur serveur, etc.). Le « S » de HTTPS = chiffré.
6. **SSH.** Se connecter en ligne de commande, de façon sécurisée, à une
   machine distante. C'est l'outil quotidien du DevOps pour administrer un
   serveur. Notion de clés SSH (publique/privée).
7. **Pare-feu (firewall).** Filtre ce qui a le droit d'entrer/sortir. Idée
   d'« ouvrir un port ».

## Recherches à faire

- « modèle client serveur expliqué »
- « adresse IP publique vs privée »
- « à quoi sert un port réseau »
- « comment fonctionne le DNS animation »
- « requête réponse HTTP codes de statut liste »
- « HTTP vs HTTPS différence »
- « SSH c'est quoi tutoriel débutant »
- « paire de clés SSH publique privée »

Question fil rouge : **que se passe-t-il, étape par étape, entre le moment où
tu tapes une URL et celui où la page s'affiche ?** C'est LA question à savoir
raconter à la fin de cette partie.

## Exercices

Détails dans [exercices/](exercices/) :

1. **Explore ta machine** — trouver ton IP, tester la connexion
   ([exercices/01-decouverte-reseau.md](exercices/01-decouverte-reseau.md)).
2. **Parler HTTP à la main** — utiliser `curl` pour voir requêtes et réponses
   ([exercices/02-http-curl.md](exercices/02-http-curl.md)).
3. **Le voyage d'une URL** — écrire le parcours complet d'une requête web
   ([exercices/03-voyage-url.md](exercices/03-voyage-url.md)).

## Projet de la partie

Rédige dans ton `JOURNAL.md` un texte illustré (schéma à la main accepté)
intitulé « Que se passe-t-il quand je tape google.com ? », qui fait
intervenir : DNS, IP, port, client/serveur, HTTP, code de statut.

## Auto-évaluation

Sans notes :

- Quelle est la différence entre une IP et un port ?
- À quoi sert le DNS ?
- Que signifie un code 404 ? Un 500 ?
- À quoi sert SSH et sur quel port par défaut ?

➡️ Partie suivante : [03 — Git](../03-git/)
