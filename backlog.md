# Django Backlog

## Homepage OK

En tant qu'utilisateur non connecté
Je peux accéder à la page d'accueil
Afin de découvrir le site et d'avoir accès au login et inscription

CA :

- Je vois le nom et la présentation du site
- Je vois les boutons de login et d'inscription

## Inscription OK

En tant qu'utilisateur non connecté
Je peux accéder au formulaire d'inscription
Afin de créer un compte

CA :

- Je vois un formulaire d'inscription
- Je peux saisir mon email et mot de passe
- Je peux valider le formulaire
- Je suis redirigé vers la page de login
- Je reçois un email de confirmation

## Login OK

En tant qu'utilisateur non connecté
Je peux accéder au formulaire de login
Afin de me connecter à mon compte

CA :

- Je vois un formulaire de login
- Je peux saisir mon email et mot de passe
- Je peux valider le formulaire
- Je suis redirigé vers page organisations

## Logout OK

En tant qu'utilisateur connecté
Je peux me déconnecter
Afin de quitter mon compte

CA :

- Je vois un bouton de logout
- Je peux cliquer sur le bouton
- Je suis redirigé vers la page d'accueil

## Mot de passe oublié

En tant qu'utilisateur non connecté
Je peux accéder au formulaire de mot de passe oublié
Afin de recevoir un email de réinitialisation
$$
CA

- Je vois un lien "mot de passe oublié"
- Je peux cliquer sur le lien
- Je suis redirigé vers un formulaire
- Je peux saisir mon email
- Je reçois un email de réinitialisation

## Modification du mot de passe

En tant qu'utilisateur connecté
Je peux accéder au formulaire de modification du mot de passe
Afin de changer mon mot de passe

CA

- Je vois un lien "modifier mon mot de passe"
- Je peux cliquer sur le lien
- Je suis redirigé vers un formulaire
- Je peux saisir mon ancien mot de passe, le nouveau et le confirmer
- Je peux valider le formulaire
- Je suis redirigé vers la page princiaple avec un message de confirmation

## Admin django

En tant qu'admin django
Je peux accéder à l'interface d'administration
Afin de gérer les utilisateurs et les données

CA

- Je peux me connecter à l'interface d'administration
- Je peux voir la liste des utilisateurs
- Je peux modifier un utilisateur
- Je peux supprimer un utilisateur
- Je peux voir la liste des données
- Je peux modifier une donnée
- Je peux supprimer une donnée

## Administration d'une organisation

En tant qu'admin d'une organisation
Je peux accéder à l'interface d'administration de mon organisation
Afin de gérer les utilisateurs et les données de mon organisation

CA

- Je vois un lien d'accès à l'interface d'administration de mon organisation

## Creation d'un événement

En tant qu'admin d'une organisation
Je peux accéder au formulaire de création d'un événement
Afin de créer un événement

CA :

- Je vois un lien "créer un événement" dans mon interface d'administration de mon organisation
- Je peux cliquer sur le lien
- Je suis redirigé vers un formulaire
- Je peux saisir les données de l'événement
- Je peux valider le formulaire

## Modification d'un événement

En tant qu'admin d'une organisation
Je peux accéder au formulaire de modification d'un événement
Afin de modifier un événement

## Liste des organisations

En tant qu'utilisateur connecté
Je peux accéder à la liste des organisations
Afin d'accéder à une organisation donnée

CA

- Je vois la liste des organisations
- Je peux cliquer sur une organisation
- Je suis redirigé vers la page de l'organisation
- Si je n'ai qu'une seule organisation, je suis redirigé directement vers la page de l'organisation
- Si je n'ai pas d'organisation, je vois un message m'invitant à contacter l'admin de mon organisation pour qu'il m'
  ajoute

## Page d'une organisation

En tant qu'utilisateur connecté
Je peux accéder à la page d'une organisation
Afin de voir les informations de l'organisation

CA

- Je vois les informations de l'organisation
- Je vois la liste des événements de l'organisation

## Inscription à un événement

En tant qu'utilisateur connecté
Je peux m'inscrire à un événement
Afin d'indiquer ma participation aux organisateurs

CA

- Je vois un bouton "s'inscrire" sur la page de l'événement
- Je peux cliquer sur le bouton
- Je vois que mon inscription est enregistrée
- Les organisateurs reçoivent un email de notification

## Désinscription à un événement

En tant qu'utilisateur connecté et inscrit à un événement
Je peux me désinscrire d'un événement
Afin d'informer les organisateurs de mon absence

CA

- Je vois un bouton "se désinscrire" sur la page de l'événement
- Je peux cliquer sur le bouton
- Je vois que ma désinscription est enregistrée
- Les organisateurs reçoivent un email de notification

## Invitation d'un utilisateur

En tant qu'admin d'une organisation
Je peux inviter un utilisateur à rejoindre mon organisation
Afin de lui donner accès aux informations de mon organisation

CA

- Je vois un lien "inviter un utilisateur" dans mon interface d'administration de mon organisation
- Je peux inviter un utilisateur en saisissant son email
- L'utilisateur reçoit un email d'invitation
- L'utilisateur peut cliquer sur le lien de l'email pour rejoindre l'organisation
    - Si l'utilisateur n'est pas inscrit, il est invité à s'inscrire
    - Si l'utilisateur est inscrit, il est invité à se connecter
- L'utilisateur est redirigé vers la page de l'organisation