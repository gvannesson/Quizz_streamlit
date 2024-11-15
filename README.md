# Quiz App 🎉

## Description

Ce projet permet de créer un quiz interactif avec Streamlit. Il inclut une fonctionnalité de validation des entrées pour s'assurer que les utilisateurs créent des questions avec exactement quatre réponses, et que la bonne réponse est spécifiée par un chiffre entre 1 et 4. Le quiz stocke les données dans un fichier JSON et permet aux utilisateurs de répondre à des questions, de voir leur score et de recommencer le quiz.

### Fonctionnalités

- Création de quiz avec validation des données (question, réponses, bonne réponse).
- Sauvegarde des questions et réponses dans un fichier `quiz_data.json`.
- Affichage du quiz et calcul du score au fur et à mesure.
- Recommencement du quiz avec la possibilité de voir le score final.

## Prérequis

Pour faire fonctionner ce projet, vous devez avoir Python installé ainsi que les bibliothèques nécessaires. Vous pouvez installer les dépendances via `pip`.

```bash
pip install streamlit pydantic
```

## Installation

1. Clonez ce repository :

```bash
git clone https://github.com/votre-utilisateur/quiz-app.git
cd quiz-app
```

2. Installez les dépendances requises :

```bash
pip install -r requirements.txt
```

3. Lancez l'application Streamlit :

```bash
streamlit run quizz.streamlit.py
```

## Utilisation

### Créer un quiz :

1. Entrez une question dans le champ "Type a question".
2. Saisissez quatre réponses possibles dans les champs correspondants.
3. Indiquez le numéro de la bonne réponse (entre 1 et 4).
4. Cliquez sur le bouton **"Save your question"** pour ajouter la question au fichier JSON.

### Répondre au quiz :

1. Une fois une question enregistrée, le quiz commence.
2. L'utilisateur sélectionne une réponse et clique sur "Next question" pour passer à la question suivante.
3. Après avoir répondu à toutes les questions, le score final est affiché.
4. Il est possible de recommencer le quiz en cliquant sur le bouton **"Recommencer le quizz"**.

## Structure du projet

```
quiz-app/
│
├── app.py               # Application principale Streamlit
├── quiz_data.json       # Fichier JSON contenant les questions et réponses
├── requirements.txt     # Dépendances Python
└── README.md            # Documentation du projet
```

### Fichier `quiz_data.json`

Le fichier `quiz_data.json` est utilisé pour stocker les questions, les réponses et la bonne réponse sous la forme d'une liste de dictionnaires. Par exemple :

```json
[
    {
        "Question :": "What is the capital of France?",
        "Answers :": ["Paris", "Berlin", "Madrid", "Rome"],
        "good_answer :": "1"
    },
    {
        "Question :": "What is 2 + 2?",
        "Answers :": ["3", "4", "5", "6"],
        "good_answer :": "2"
    }
]
```

## Technologies utilisées

- **Streamlit** : Pour la création de l'application web interactive.
- **Pydantic** : Pour la validation des entrées (questions, réponses, bonne réponse).
- **JSON** : Pour le stockage des données du quiz.

## Validation des données

Les données sont validées via **Pydantic** pour garantir que :

1. La question n'est pas vide.
2. Il y a exactement 4 réponses.
3. La bonne réponse est un chiffre entre 1 et 4.

Les erreurs de validation sont affichées dans l'interface utilisateur sous forme de messages d'erreur.

## Contribuer

Si vous souhaitez contribuer à ce projet, vous pouvez fork ce repository, apporter vos modifications, et soumettre une pull request. Nous acceptons des améliorations, des corrections de bugs et des suggestions.

### Instructions pour contribuer :

1. Fork le repository.
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature-nom-fonctionnalité`).
3. Commitez vos modifications (`git commit -m 'Ajout d'une nouvelle fonctionnalité'`).
4. Poussez votre branche (`git push origin feature-nom-fonctionnalité`).
5. Ouvrez une pull request.

## License

Ce projet est sous la licence MIT. Voir le fichier `LICENSE` pour plus de détails.

---

### Explications des sections du README.md :

1. **Description** : Une brève présentation du projet et de ses fonctionnalités.
2. **Prérequis** : La liste des bibliothèques nécessaires pour faire fonctionner l'application.
3. **Installation** : Les étapes à suivre pour cloner le projet, installer les dépendances et exécuter l'application.
4. **Utilisation** : Des instructions détaillées pour utiliser l'application (création et réponse au quiz).
5. **Structure du projet** : Une vue d'ensemble de la structure des fichiers dans le projet.
6. **Technologies utilisées** : Les principales technologies utilisées pour développer l'application.
7. **Validation des données** : Une explication de la validation des entrées avec Pydantic.
8. **Contribuer** : Des instructions pour les personnes souhaitant contribuer au projet.
9. **License** : La licence du projet.

### Conclusion

Ce `README.md` sert à fournir une documentation complète pour les utilisateurs et développeurs qui souhaitent utiliser ou contribuer à votre projet de quiz.