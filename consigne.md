# Django CREATE

### Partie une : INTERGRATION du template
- une navbar fonctionnelle :
    - un onglet home qui renvoie vers la page home
    - un onglet blog qui renvoie vers la page blog
    - un onglet portfolio qui renvoie vers la page portfolio
    - un onglet contact qui renvoie vers la page contact

- la page blog :
    - il doit y avoir maximum 4 articles affichés
    - le contenu des articles doit être rajouté manuellement dans votre DB
        - le titre sera en string, limité à 30 caractères
        - l'image sera en string, limité à 100 caractères
        - la description sera en text
- la page portfolio
    - il doit avoir maximum 15 projets affichés
    - le contenu des projets doit être rajouté manuellement dans votre DB
        - le titre sera en string, limité à 50 caractères
        - la description sera en text

- la page contact :
    - la garder telle quelle

- le footer
    - le garder tel quel



### Partie deux : REALISATION d'un backoffice

- Réaliser une page back office contenant :
    - un menu redirigeant vers les différentes pages du back offices ( blog & portfolio)
    - Sur chaque page, il faut des form pour pouvoir ajouter du contenu (CRUD create)
    - Rajouter également un tableau récapitulatif du contenu des tables
- Attention de bien organiser votre dossier templates ! (Création du dossier 'backoffice', à vous de gérer la structure de dossier d'une manière cohérente)
